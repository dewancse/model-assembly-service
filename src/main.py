import requests
from libcellml import *
from miscellaneous import *
from SPARQLWrapper import SPARQLWrapper, JSON

# Instantiate a model
m = Model()

# model ID
modelId = "epithelialModelID"
m.setId(modelId)

# model name
modelName = "epithelialModel"
m.setName(modelName)

print("Model: ", m, "\nModel Id: ", m.getId(), "\nModel Name: ", m.getName())

# iterate through model recipe to import components from source models
for item in model_recipe:
    if item["model_entity"] != "":
        processModelEntity(item["model_entity"], m)
    if item['model_entity2'] != "":
        processModelEntity(item["model_entity2"], m)
    if item["model_entity3"] != "":
        processModelEntity(item["model_entity3"], m)


# create imported components from source model into the new model
def addImportedComponent(modelentity, fma, chebi, compartment, source_fma2, source_fma, sink_fma, epithelial):
    # component and variable for fluxes
    component_variable_flux = modelentity[modelentity.find('#') + 1:len(modelentity)]
    name_of_component_flux = component_variable_flux[:component_variable_flux.find('.')]
    name_of_variable_flux = component_variable_flux[component_variable_flux.find('.') + 1:]

    # uncomment if want to include imported components inside epithelial's encapsulation
    if compartment.getName() != "epithelial":
        compartment.addComponent(m.getComponent(name_of_component_flux))

    print("\n")
    print("MODELENTITY FLUX:", modelentity)

    # sparql
    query = concentrationSparql(fma, chebi)

    sparql = SPARQLWrapper(sparqlendpoint)
    sparql.setQuery(query)

    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    # load this cellml model
    model_name_flux = modelentity[0:modelentity.find('#')]
    r = requests.get(workspaceURL + model_name_flux)

    # parse the string representation of the model to access by libcellml
    p = Parser()
    importedModel = p.parseModel(r.text)

    for result in results["results"]["bindings"]:
        model_entity_cons = result["modelEntity"]["value"]
        model_name_cons = model_entity_cons[0:model_entity_cons.find('#')]

        print("MODELENTITY CONCENTRATION:", modelentity)

        flag_flux = False
        flag_concentration = False
        if model_name_cons == model_name_flux:
            # component and variable for concentrations
            component_variable_cons = model_entity_cons[model_entity_cons.find('#') + 1:len(model_entity_cons)]
            name_of_component_cons = component_variable_cons[:component_variable_cons.find('.')]
            name_of_variable_cons = component_variable_cons[component_variable_cons.find('.') + 1:]

            # iteratively checking a flux and its associated concentration variable in a component
            c = importedModel.getComponent(name_of_component_cons)

            i = 0
            while c.getVariable(i) != None:
                v_flux = c.getVariable(i)
                # if flux variable exists then find its associated concentration variable
                if v_flux.getName() == name_of_variable_flux:
                    flag_flux = True
                    break
                # increment i to iterate next item in the while loop
                i += 1

            # find a concentration variable of the associated flux variable in the same component
            if flag_flux == True:
                c = importedModel.getComponent(name_of_component_cons)
                i = 0
                while c.getVariable(i) != None:
                    v_cons = c.getVariable(i)
                    if v_cons.getName() == name_of_variable_cons and v_cons.getInitialValue() != "":
                        # add units of concentration and flux variables
                        addUnitsModel(v_cons.getUnits(), importedModel, m)
                        addUnitsModel(v_flux.getUnits(), importedModel, m)

                        # concentration variable
                        if compartment.getVariable(v_cons.getName()) == None:
                            v_cons_compartment = Variable()
                            createComponent(v_cons_compartment, v_cons.getName(), v_cons.getUnits(), "public",
                                            v_cons.getInitialValue(), compartment, v_cons)

                        # flux variable
                        if compartment.getVariable(v_flux.getName()) == None:
                            v_flux_compartment = Variable()
                            createComponent(v_flux_compartment, v_flux.getName(), v_flux.getUnits(), "public",
                                            v_flux.getInitialValue(), compartment, v_flux)

                        # assign plus or minus sign in the ODE based equations
                        sign = odeSignNotation(compartment, source_fma, sink_fma)

                        # exclude ODE based equations for channels and diffusive fluxes
                        if source_fma2 != "channel" and source_fma2 != "diffusiveflux":
                            compartment.appendMath(mathEq(v_cons.getName(), v_flux.getName(), sign))

                        flag_concentration = True
                        break
                    # increment i to iterate next item in the while loop
                    i += 1

            # if flux and concentration variables are in the same component
            # then exit from the for loop to iterate next item from the model recipe
            if flag_concentration == True:
                break

    # ODE equations for channels and diffusive fluxes
    # Include all variables that are in the channels and diffusive fluxes equations
    if source_fma2 == "channel" or source_fma2 == "diffusiveflux":
        c = importedModel.getComponent(name_of_component_flux)
        getChannelsEquation(c.getMath().splitlines(), name_of_variable_flux, compartment,
                            importedModel, m, epithelial)


# environment component
environment = Component()
environment.setName("environment")
v_e = Variable()
createComponent(v_e, "time", "second", "public", None, environment, None)
m.addComponent(environment)

# epithelial component
epithelial = Component()
epithelial.setName("epithelial")

# lumen component
lumen = Component()
lumen.setName("lumen")

# cytosol component
cytosol = Component()
cytosol.setName("cytosol")

# interstitial fluid component
interstitialfluid = Component()
interstitialfluid.setName("interstitialfluid")

# encapsulation of epithelial component
# create lumen components inside epithelial component
for item in model_recipe:
    if item["source_fma"] == lumen_fma:
        addImportedComponent(item["model_entity"], item["source_fma"], item["solute_chebi"], lumen, item["source_fma2"],
                             item["source_fma"], item["sink_fma"], epithelial)
    if item["sink_fma"] == lumen_fma:
        addImportedComponent(item["model_entity"], item["sink_fma"], item["solute_chebi"], lumen, item["source_fma2"],
                             item["source_fma"], item["sink_fma"], epithelial)
    if item["source_fma2"] != "" and item["source_fma2"] == lumen_fma:
        addImportedComponent(item["model_entity2"], item["source_fma2"], item["solute_chebi2"], lumen,
                             item["source_fma2"], item["source_fma2"], item["sink_fma2"], epithelial)
    if item["source_fma2"] != "" and item["sink_fma2"] == lumen_fma:
        addImportedComponent(item["model_entity2"], item["sink_fma2"], item["solute_chebi2"], lumen,
                             item["source_fma2"], item["source_fma2"], item["sink_fma2"], epithelial)
    if item["source_fma3"] != "" and item["source_fma3"] == lumen_fma:
        addImportedComponent(item["model_entity3"], item["source_fma3"], item["solute_chebi3"], lumen,
                             item["source_fma2"], item["source_fma3"], item["sink_fma3"], epithelial)
    if item["source_fma3"] != "" and item["sink_fma3"] == lumen_fma:
        addImportedComponent(item["model_entity3"], item["sink_fma3"], item["solute_chebi3"], lumen,
                             item["source_fma2"], item["source_fma3"], item["sink_fma3"], epithelial)

# create cytosol components inside epithelial component
for item in model_recipe:
    if item["source_fma"] == cytosol_fma:
        addImportedComponent(item["model_entity"], item["source_fma"], item["solute_chebi"], cytosol,
                             item["source_fma2"], item["source_fma"], item["sink_fma"], epithelial)
    if item["sink_fma"] == cytosol_fma:
        addImportedComponent(item["model_entity"], item["sink_fma"], item["solute_chebi"], cytosol, item["source_fma2"],
                             item["source_fma"], item["sink_fma"], epithelial)
    if item["source_fma2"] != "" and item['source_fma2'] == cytosol_fma:
        addImportedComponent(item["model_entity2"], item["source_fma2"], item["solute_chebi2"], cytosol,
                             item["source_fma2"], item["source_fma2"], item["sink_fma2"], epithelial)
    if item["source_fma2"] != "" and item['sink_fma2'] == cytosol_fma:
        addImportedComponent(item["model_entity2"], item["sink_fma2"], item["solute_chebi2"], cytosol,
                             item["source_fma2"], item["source_fma2"], item["sink_fma2"], epithelial)
    if item["source_fma3"] != "" and item["source_fma3"] == cytosol_fma:
        addImportedComponent(item["model_entity3"], item["source_fma3"], item["solute_chebi3"], cytosol,
                             item["source_fma2"], item["source_fma3"], item["sink_fma3"], epithelial)
    if item["source_fma3"] != "" and item["sink_fma3"] == cytosol_fma:
        addImportedComponent(item["model_entity3"], item["sink_fma3"], item["solute_chebi3"], cytosol,
                             item["source_fma2"], item["source_fma3"], item["sink_fma3"], epithelial)

# create interstitial fluid components inside epithelial component
for item in model_recipe:
    if item["source_fma"] == interstitialfluid_fma:
        addImportedComponent(item["model_entity"], item["source_fma"], item["solute_chebi"], interstitialfluid,
                             item["source_fma2"], item["source_fma"], item["sink_fma"], epithelial)
    if item["sink_fma"] == interstitialfluid_fma:
        addImportedComponent(item["model_entity"], item["sink_fma"], item["solute_chebi"], interstitialfluid,
                             item["source_fma2"], item["source_fma"], item["sink_fma"], epithelial)
    if item["source_fma2"] != "" and item["source_fma2"] == interstitialfluid_fma:
        addImportedComponent(item["model_entity2"], item["source_fma2"], item["solute_chebi2"], interstitialfluid,
                             item["source_fma2"], item["source_fma2"], item["sink_fma2"], epithelial)
    if item["source_fma2"] != "" and item["sink_fma2"] == interstitialfluid_fma:
        addImportedComponent(item["model_entity2"], item["sink_fma2"], item["solute_chebi2"], interstitialfluid,
                             item["source_fma2"], item["source_fma2"], item["sink_fma2"], epithelial)
    if item["source_fma3"] != "" and item["source_fma3"] == interstitialfluid_fma:
        addImportedComponent(item["model_entity3"], item["source_fma3"], item["solute_chebi3"], interstitialfluid,
                             item["source_fma2"], item["source_fma3"], item["sink_fma3"], epithelial)
    if item["source_fma3"] != "" and item["sink_fma3"] == interstitialfluid_fma:
        addImportedComponent(item["model_entity3"], item["sink_fma3"], item["solute_chebi3"], interstitialfluid,
                             item["source_fma2"], item["source_fma3"], item["sink_fma3"], epithelial)

# include time variable to lumen, cytosol, interstitial fluid and epithelial component
v_lumen = Variable()
createComponent(v_lumen, "time", "second", "public", None, lumen, None)

v_cytosol = Variable()
createComponent(v_cytosol, "time", "second", "public", None, cytosol, None)

v_interstitial = Variable()
createComponent(v_interstitial, "time", "second", "public", None, interstitialfluid, None)

# add lumen component to epithelial component
epithelial.addComponent(lumen)

# add cytosol component to epithelial component
epithelial.addComponent(cytosol)

# add interstitial component to epithelial component
epithelial.addComponent(interstitialfluid)

m.addComponent(epithelial)

# remove concentration of solutes variable from the epithelial component which exist
# in the lumen/cytosol/interstitial fluid component with initial value.
# Initially, make a list of epithelial component's variables
i = 0
epithelial_var_list = []
while epithelial.getVariable(i) != None:
    v = epithelial.getVariable(i)
    epithelial_var_list.append(v.getName())
    i += 1

# Iterate over lumen, cytosol and interstitial fluid component
# remove C_c_Na from here ['C_c_Na', 'RT', 'psi_c', 'P_mc_Na', 'F', 'psi_m']
eIndex = 0
while epithelial.getComponent(eIndex) != None:
    compName = epithelial.getComponent(eIndex)
    vIndex = 0
    while compName.getVariable(vIndex) != None:
        varName = compName.getVariable(vIndex)
        if varName.getName() in epithelial_var_list and varName.getInitialValue() != "":
            epithelial.removeVariable(varName.getName())
        vIndex += 1
    eIndex += 1

# remove multiple instances of MathML in lumen, cytosol and interstitial fluid component
i = 0
while epithelial.getComponent(i) != None:
    c = epithelial.getComponent(i)
    str_math = c.getMath().splitlines()
    str_math_2 = ""
    print("compartments:", str_math)
    for j in range(len(str_math)):
        if "<math xmlns=\"http://www.w3.org/1998/Math/MathML\">" in str_math[j] or "</math>" in str_math[j]:
            if j != 0 and j != len(str_math) - 1:
                continue
        str_math_2 += str_math[j]
    c.setMath(str_math_2)
    i += 1

# remove multiple instances of MathML in epithelial component
i = 0
while m.getComponent(i) != None:
    c = m.getComponent(i)
    if c.getName() == "epithelial":
        str_math = c.getMath().splitlines()
        str_math_2 = ""
        print("epithelial:", str_math)
        for j in range(len(str_math)):
            if "<math xmlns=\"http://www.w3.org/1998/Math/MathML\">" in str_math[j] or "</math>" in str_math[j]:
                if j != 0 and j != len(str_math) - 1:
                    continue
            str_math_2 += str_math[j]
        c.setMath(str_math_2)
        break
    i += 1

# mapping connection between epithelial and environment component
i = 0
while epithelial.getVariable(i) != None:
    v1 = epithelial.getVariable(i)
    v1_name = v1.getName()
    j = 0
    while environment.getVariable(j) != None:
        v2 = environment.getVariable(j)
        v2_name = v2.getName()

        if v1_name == v2_name:
            variable = Variable()
            variable.addEquivalence(v1, v2)
        # increment j to iterate next item in the while loop
        j += 1
    # increment i to iterate next item in the while loop
    i += 1

# mapping connection between epithelial and lumen component
i = 0
while epithelial.getVariable(i) != None:
    v1 = epithelial.getVariable(i)
    v1_name = v1.getName()
    j = 0
    while lumen.getVariable(j) != None:
        v2 = lumen.getVariable(j)
        v2_name = v2.getName()

        if v1_name == v2_name:
            variable = Variable()
            variable.addEquivalence(v1, v2)
        # increment j to iterate next item in the while loop
        j += 1
    # increment i to iterate next item in the while loop
    i += 1

# mapping connection between epithelial and cytosol component
i = 0
while epithelial.getVariable(i) != None:
    v1 = epithelial.getVariable(i)
    v1_name = v1.getName()
    j = 0
    while cytosol.getVariable(j) != None:
        v2 = cytosol.getVariable(j)
        v2_name = v2.getName()

        if v1_name == v2_name:
            variable = Variable()
            variable.addEquivalence(v1, v2)
        # increment j to iterate next item in the while loop
        j += 1
    # increment i to iterate next item in the while loop
    i += 1

# mapping connection between epithelial and interstitial fluid component
i = 0
while epithelial.getVariable(i) != None:
    v1 = epithelial.getVariable(i)
    v1_name = v1.getName()
    j = 0
    while interstitialfluid.getVariable(j) != None:
        v2 = interstitialfluid.getVariable(j)
        v2_name = v2.getName()

        if v1_name == v2_name:
            variable = Variable()
            variable.addEquivalence(v1, v2)
        # increment j to iterate next item in the while loop
        j += 1
    # increment i to iterate next item in the while loop
    i += 1

# serialize and print a model
printer = Printer()
model = printer.printModel(m)

print("\nModel:", model)

# write the model in a file
f = open("model.xml", "w")
f.write(model)
