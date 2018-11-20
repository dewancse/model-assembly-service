import requests
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
for item in modelRecipe:
    if item['model_entity'] != "":
        processModelEntity(item['model_entity'], m)
    if item['model_entity2'] != "":
        processModelEntity(item['model_entity2'], m)
    if item['model_entity3'] != "":
        processModelEntity(item['model_entity3'], m)


def addImportedComponent(modelentity, fma, chebi, compartment):
    componentandvariable = modelentity[modelentity.find('#') + 1:len(modelentity)]
    nameofcomponent = componentandvariable[:componentandvariable.find('.')]
    nameofvariable = componentandvariable[componentandvariable.find('.') + 1:]
    compartment.addComponent(m.getComponent(nameofcomponent))

    # sparql
    query = concentrationSparql(fma, chebi)

    sparql = SPARQLWrapper(sparqlendpoint)
    sparql.setQuery(query)

    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    # load this cellml model
    modelname = modelentity[0:modelentity.find('#')]
    r = requests.get(workspaceURL + modelname)

    # parse the string representation of the model to access by libcellml
    p = Parser()
    importedModel = p.parseModel(r.text)

    for result in results["results"]["bindings"]:
        model_entity = result["modelEntity"]["value"]
        model_name = model_entity[0:model_entity.find('#')]

        flag = False
        flag_concentration = False
        if model_name == modelname:
            component_variable = model_entity[model_entity.find('#') + 1:len(model_entity)]
            name_of_component = component_variable[:component_variable.find('.')]
            name_of_variable = component_variable[component_variable.find('.') + 1:]

            # iteratively checking a flux and its associated concentration variable in a component
            c = importedModel.getComponent(name_of_component)

            i = 0
            while c.getVariable(i) != None:
                v_flux = c.getVariable(i)
                # if flux variable exists then find its associated concentration variable
                if v_flux.getName() == nameofvariable:
                    flag = True
                    break
                i += 1

            # find a concentration variable of the associated flux variable in the same component
            if flag == True:
                c = importedModel.getComponent(name_of_component)
                i = 1
                while c.getVariable(i) != None:
                    v_cons = c.getVariable(i)
                    if v_cons.getName() == name_of_variable:
                        # concentration variable
                        if compartment.getVariable(v_cons.getName()) == None:
                            v = Variable()
                            v.setName(v_cons.getName())
                            v.setUnits(v_cons.getUnits())
                            v.setInitialValue(v_cons.getInitialValue())
                            v.setInterfaceType(v_cons.getInterfaceType())
                            v.setId(compartment.getName() + "." + v_cons.getName())

                            compartment.addVariable(v)

                            print("name:", v_cons.getName(), "units:", v_cons.getUnits(), "initial_value:",
                                  v_cons.getInitialValue(),
                                  "interface:", v_cons.getInterfaceType(), "id:", v_cons.getId())

                        # flux variable
                        if compartment.getVariable(v_flux.getName()) == None:
                            v = Variable()
                            v.setName(v_flux.getName())
                            v.setUnits(v_flux.getUnits())
                            v.setInitialValue(v_flux.getInitialValue())
                            v.setInterfaceType(v_flux.getInterfaceType())
                            v.setId(compartment.getName() + "." + v_flux.getName())

                            compartment.addVariable(v)

                            print("name:", v_flux.getName(), "units:", v_flux.getUnits(), "initial_value:",
                                  v_flux.getInitialValue(),
                                  "interface:", v_flux.getInterfaceType(), "id:", v_flux.getId())

                        flag_concentration = True
                        break

                    i += 1

            if flag_concentration == True:
                break

    # print(result["modelEntity"]["value"])


# environment component
environment = Component()
environment.setName("environment")
v_e = Variable()
v_e.setName("time")
v_e.setUnits("second")
v_e.setInterfaceType("public")
v_e.setId(environment.getName() + "." + v_e.getName())
environment.addVariable(v_e)
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
for item in modelRecipe:
    if item["source_fma"] == lumen_fma:
        addImportedComponent(item["model_entity"], item["source_fma"], item["solute_chebi"], lumen)
        print(item["variable_text"])
    if item["sink_fma"] == lumen_fma:
        addImportedComponent(item["model_entity"], item["sink_fma"], item["solute_chebi"], lumen)
        print(item["variable_text"])
    if item["source_fma2"] != "" and item["source_fma2"] == lumen_fma:
        addImportedComponent(item["model_entity2"], item["source_fma2"], item["solute_chebi2"], lumen)
        print(item["variable_text2"])
    if item["source_fma2"] != "" and item["sink_fma2"] == lumen_fma:
        addImportedComponent(item["model_entity2"], item["sink_fma2"], item["solute_chebi2"], lumen)
        print(item["variable_text2"])
    if item["source_fma3"] != "" and item["source_fma3"] == lumen_fma:
        addImportedComponent(item["model_entity3"], item["source_fma3"], item["solute_chebi3"], lumen)
        print(item["variable_text3"])
    if item["source_fma3"] != "" and item["sink_fma3"] == lumen_fma:
        addImportedComponent(item["model_entity3"], item["sink_fma3"], item["solute_chebi3"], lumen)
        print(item["variable_text3"])

# create cytosol components inside epithelial component
for item in modelRecipe:
    if item["source_fma"] == cytosol_fma:
        addImportedComponent(item["model_entity"], item["source_fma"], item["solute_chebi"], cytosol)
        print(item["variable_text"])
    if item["sink_fma"] == cytosol_fma:
        addImportedComponent(item["model_entity"], item["sink_fma"], item["solute_chebi"], cytosol)
        print(item["variable_text"])
    if item["source_fma2"] != '' and item['source_fma2'] == cytosol_fma:
        addImportedComponent(item["model_entity2"], item["source_fma2"], item["solute_chebi2"], cytosol)
        print(item["variable_text2"])
    if item["source_fma2"] != '' and item['sink_fma2'] == cytosol_fma:
        addImportedComponent(item["model_entity2"], item["sink_fma2"], item["solute_chebi2"], cytosol)
        print(item["variable_text2"])
    if item["source_fma3"] != '' and item["source_fma3"] == cytosol_fma:
        addImportedComponent(item["model_entity3"], item["source_fma3"], item["solute_chebi3"], cytosol)
        print(item["variable_text3"])
    if item["source_fma3"] != '' and item["sink_fma3"] == cytosol_fma:
        addImportedComponent(item["model_entity3"], item["sink_fma3"], item["solute_chebi3"], cytosol)
        print(item["variable_text3"])

# create interstitial fluid components inside epithelial component
for item in modelRecipe:
    if item["source_fma"] == interstitialfluid_fma:
        addImportedComponent(item["model_entity"], item["source_fma"], item["solute_chebi"], interstitialfluid)
        print(item["variable_text"])
    if item["sink_fma"] == interstitialfluid_fma:
        addImportedComponent(item["model_entity"], item["sink_fma"], item["solute_chebi"], interstitialfluid)
        print(item["variable_text"])
    if item["source_fma2"] != "" and item["source_fma2"] == interstitialfluid_fma:
        addImportedComponent(item["model_entity2"], item["source_fma2"], item["solute_chebi2"], interstitialfluid)
        print(item["variable_text2"])
    if item["source_fma2"] != "" and item["sink_fma2"] == interstitialfluid_fma:
        addImportedComponent(item["model_entity2"], item["sink_fma2"], item["solute_chebi2"], interstitialfluid)
        print(item["variable_text2"])
    if item["source_fma3"] != "" and item["source_fma3"] == interstitialfluid_fma:
        addImportedComponent(item["model_entity3"], item["source_fma3"], item["solute_chebi3"], interstitialfluid)
        print(item["variable_text3"])
    if item["source_fma3"] != "" and item["sink_fma3"] == interstitialfluid_fma:
        addImportedComponent(item["model_entity3"], item["sink_fma3"], item["solute_chebi3"], interstitialfluid)
        print(item["variable_text3"])

# include time variable to lumen, cytosol, interstitial fluid, and epithelial component
v_lumen = Variable()
v_lumen.setName("time")
v_lumen.setUnits("second")
v_lumen.setInterfaceType("public")
v_lumen.setId(lumen.getName() + "." + v_lumen.getName())
lumen.addVariable(v_lumen)

v_cytosol = Variable()
v_cytosol.setName("time")
v_cytosol.setUnits("second")
v_cytosol.setInterfaceType("public")
v_cytosol.setId(cytosol.getName() + "." + v_cytosol.getName())
cytosol.addVariable(v_cytosol)

v_interstitial = Variable()
v_interstitial.setName("time")
v_interstitial.setUnits("second")
v_interstitial.setInterfaceType("public")
v_interstitial.setId(interstitialfluid.getName() + "." + v_interstitial.getName())
interstitialfluid.addVariable(v_interstitial)

v_epithelial = Variable()
v_epithelial.setName("time")
v_epithelial.setUnits("second")
v_epithelial.setInterfaceType("public")
v_epithelial.setId(epithelial.getName() + "." + v_epithelial.getName())
epithelial.addVariable(v_epithelial)

# add components to model
# m.addComponent(lumen)
# m.addComponent(cytosol)
# m.addComponent(interstitialfluid)

# add lumen component to epithelial component
epithelial.addComponent(lumen)

# add cytosol component to epithelial component
epithelial.addComponent(cytosol)

# add interstitial component to epithelial component
epithelial.addComponent(interstitialfluid)

m.addComponent(epithelial)

# mapping connection between epithelial and environment component
i = 0
while epithelial.getVariable(i) != None:
    v11 = epithelial.getVariable(i)
    v11_name = v11.getName()
    j = 0
    while environment.getVariable(j) != None:
        v12 = environment.getVariable(j)
        v12_name = v12.getName()

        if v11_name == v12_name:
            variable = Variable()
            variable.addEquivalence(v11, v12)
        j += 1
    i += 1

# mapping connection between epithelial and lumen component
i = 0
while epithelial.getVariable(i) != None:
    v11 = epithelial.getVariable(i)
    v11_name = v11.getName()
    j = 0
    while lumen.getVariable(j) != None:
        v12 = lumen.getVariable(j)
        v12_name = v12.getName()

        if v11_name == v12_name:
            variable = Variable()
            variable.addEquivalence(v11, v12)
        j += 1
    i += 1

# mapping connection between epithelial and cytosol component
i = 0
while epithelial.getVariable(i) != None:
    v11 = epithelial.getVariable(i)
    v11_name = v11.getName()
    j = 0
    while cytosol.getVariable(j) != None:
        v12 = cytosol.getVariable(j)
        v12_name = v12.getName()

        if v11_name == v12_name:
            variable = Variable()
            variable.addEquivalence(v11, v12)
        j += 1
    i += 1

# mapping connection between epithelial and interstitial fluid component
i = 0
while epithelial.getVariable(i) != None:
    v11 = epithelial.getVariable(i)
    v11_name = v11.getName()
    j = 0
    while interstitialfluid.getVariable(j) != None:
        v12 = interstitialfluid.getVariable(j)
        v12_name = v12.getName()

        if v11_name == v12_name:
            variable = Variable()
            variable.addEquivalence(v11, v12)
        j += 1
    i += 1

# serialize and print a model
printer = Printer()
model = printer.printModel(m)

print("\nModel:", model)

# write in a file
f = open("model.xml", "w")
f.write(model)