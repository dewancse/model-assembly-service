from libcellml import *

# pre-generated JSON model recipe
model_recipe = [
    {
        "med_fma": "http://purl.obolibrary.org/obo/FMA_84666",
        "med_pr": "http://purl.obolibrary.org/obo/PR_P55018",
        "med_pr_text": "solute carrier family 12 member 3 (rat)",
        "med_pr_text_syn": "TSC",
        "model_entity": "chang_fujita_b_1999.cellml#total_transepithelial_sodium_flux.J_mc_Na",
        "model_entity2": "chang_fujita_b_1999.cellml#solute_concentrations.J_mc_Cl",
        "model_entity3": "",
        "protein_name": "http://purl.obolibrary.org/obo/CL_0000066",
        "sink_fma": "http://purl.obolibrary.org/obo/FMA_66836",
        "sink_fma2": "http://purl.obolibrary.org/obo/FMA_66836",
        "sink_fma3": "",
        "solute_chebi": "http://purl.obolibrary.org/obo/CHEBI_29101",
        "solute_chebi2": "http://purl.obolibrary.org/obo/CHEBI_17996",
        "solute_chebi3": "",
        "solute_text": "Na+",
        "solute_text2": "Cl-",
        "solute_text3": "",
        "source_fma": "http://purl.obolibrary.org/obo/FMA_74550",
        "source_fma2": "http://purl.obolibrary.org/obo/FMA_74550",
        "source_fma3": "",
        "variable_text": "J_mc_Na",
        "variable_text2": "J_mc_Cl",
        "variable_text3": ""
    },
    {
        "med_fma": "http://purl.obolibrary.org/obo/FMA_84666",
        "med_pr": "http://purl.obolibrary.org/obo/PR_Q63633",
        "med_pr_text": "solute carrier family 12 member 5 (rat)",
        "med_pr_text_syn": "Q63633",
        "model_entity": "chang_fujita_b_1999.cellml#solute_concentrations.J_mc_Cl",
        "model_entity2": "chang_fujita_b_1999.cellml#total_transepithelial_potassium_flux.J_mc_K",
        "model_entity3": "",
        "protein_name": "http://purl.obolibrary.org/obo/CL_0000066",
        "sink_fma": "http://purl.obolibrary.org/obo/FMA_66836",
        "sink_fma2": "http://purl.obolibrary.org/obo/FMA_66836",
        "sink_fma3": "",
        "solute_chebi": "http://purl.obolibrary.org/obo/CHEBI_17996",
        "solute_chebi2": "http://purl.obolibrary.org/obo/CHEBI_29103",
        "solute_chebi3": "",
        "solute_text": "Cl-",
        "solute_text2": "K+",
        "solute_text3": "",
        "source_fma": "http://purl.obolibrary.org/obo/FMA_74550",
        "source_fma2": "http://purl.obolibrary.org/obo/FMA_74550",
        "source_fma3": "",
        "variable_text": "J_mc_Cl",
        "variable_text2": "J_mc_K",
        "variable_text3": ""
    },
    {
        "med_fma": "http://purl.obolibrary.org/obo/FMA_84666",
        "med_pr": "http://purl.obolibrary.org/obo/PR_P37089",
        "med_pr_text": "amiloride-sensitive sodium channel subunit alpha (rat)",
        "med_pr_text_syn": "RENAC",
        "model_entity": "chang_fujita_b_1999.cellml#mc_sodium_flux.G_mc_Na",
        "model_entity2": "",
        "model_entity3": "",
        "protein_name": "http://purl.obolibrary.org/obo/CL_0000066",
        "sink_fma": "http://purl.obolibrary.org/obo/FMA_66836",
        "sink_fma2": "channel",
        "sink_fma3": "channel",
        "solute_chebi": "http://purl.obolibrary.org/obo/CHEBI_29101",
        "solute_chebi2": "channel",
        "solute_chebi3": "channel",
        "solute_text": "Na+",
        "solute_text2": "channel",
        "solute_text3": "channel",
        "source_fma": "http://purl.obolibrary.org/obo/FMA_74550",
        "source_fma2": "channel",
        "source_fma3": "channel",
        "variable_text": "G_mc_Na",
        "variable_text2": "channel",
        "variable_text3": "channel"
    },
    {
        "med_fma": "http://purl.obolibrary.org/obo/FMA_84666",
        "med_pr": "http://purl.obolibrary.org/obo/PR_Q06393",
        "med_pr_text": "chloride channel protein ClC-Ka (rat)",
        "med_pr_text_syn": "CLCNK1",
        "model_entity": "chang_fujita_b_1999.cellml#mc_chloride_flux.G_mc_Cl",
        "model_entity2": "",
        "model_entity3": "",
        "protein_name": "http://purl.obolibrary.org/obo/CL_0000066",
        "sink_fma": "http://purl.obolibrary.org/obo/FMA_66836",
        "sink_fma2": "channel",
        "sink_fma3": "channel",
        "solute_chebi": "http://purl.obolibrary.org/obo/CHEBI_17996",
        "solute_chebi2": "channel",
        "solute_chebi3": "channel",
        "solute_text": "Cl-",
        "solute_text2": "channel",
        "solute_text3": "channel",
        "source_fma": "http://purl.obolibrary.org/obo/FMA_74550",
        "source_fma2": "channel",
        "source_fma3": "channel",
        "variable_text": "G_mc_Cl",
        "variable_text2": "channel",
        "variable_text3": "channel"
    },
    {
        "med_fma": "http://purl.obolibrary.org/obo/FMA_84666",
        "med_pr": "http://purl.obolibrary.org/obo/PR_P15387",
        "med_pr_text": "potassium voltage-gated channel subfamily B member 1 (rat)",
        "med_pr_text_syn": "P15387",
        "model_entity": "chang_fujita_b_1999.cellml#mc_potassium_flux.G_mc_K",
        "model_entity2": "",
        "model_entity3": "",
        "protein_name": "http://purl.obolibrary.org/obo/CL_0000066",
        "sink_fma": "http://purl.obolibrary.org/obo/FMA_66836",
        "sink_fma2": "channel",
        "sink_fma3": "channel",
        "solute_chebi": "http://purl.obolibrary.org/obo/CHEBI_29103",
        "solute_chebi2": "channel",
        "solute_chebi3": "channel",
        "solute_text": "K+",
        "solute_text2": "channel",
        "solute_text3": "channel",
        "source_fma": "http://purl.obolibrary.org/obo/FMA_74550",
        "source_fma2": "channel",
        "source_fma3": "channel",
        "variable_text": "G_mc_K",
        "variable_text2": "channel",
        "variable_text3": "channel"
    },
    {
        "med_fma": "http://purl.obolibrary.org/obo/FMA_84669",
        "med_pr": "http://purl.obolibrary.org/obo/PR_P06685",
        "med_pr_text": "sodium/potassium-transporting ATPase subunit alpha-1 (rat)",
        "med_pr_text_syn": "P06685",
        "model_entity": "chang_fujita_b_1999.cellml#solute_concentrations.J_sc_Na",
        "model_entity2": "chang_fujita_b_1999.cellml#sc_potassium_flux.J_sc_K",
        "model_entity3": "",
        "protein_name": "http://purl.obolibrary.org/obo/CL_0000066",
        "sink_fma": "http://purl.obolibrary.org/obo/FMA_9673",
        "sink_fma2": "http://purl.obolibrary.org/obo/FMA_66836",
        "sink_fma3": "",
        "solute_chebi": "http://purl.obolibrary.org/obo/CHEBI_29101",
        "solute_chebi2": "http://purl.obolibrary.org/obo/CHEBI_29103",
        "solute_chebi3": "",
        "solute_text": "Na+",
        "solute_text2": "K+",
        "solute_text3": "",
        "source_fma": "http://purl.obolibrary.org/obo/FMA_66836",
        "source_fma2": "http://purl.obolibrary.org/obo/FMA_9673",
        "source_fma3": "",
        "variable_text": "J_sc_Na",
        "variable_text2": "J_sc_K",
        "variable_text3": ""
    },
    {
        "med_fma": "http://purl.obolibrary.org/obo/FMA_84669",
        "med_pr": "http://purl.obolibrary.org/obo/PR_Q06393",
        "med_pr_text": "chloride channel protein ClC-Ka (rat)",
        "med_pr_text_syn": "CLCNK1",
        "model_entity": "chang_fujita_b_1999.cellml#sc_chloride_flux.G_sc_Cl",
        "model_entity2": "",
        "model_entity3": "",
        "protein_name": "http://purl.obolibrary.org/obo/CL_0000066",
        "sink_fma": "http://purl.obolibrary.org/obo/FMA_66836",
        "sink_fma2": "channel",
        "sink_fma3": "channel",
        "solute_chebi": "http://purl.obolibrary.org/obo/CHEBI_17996",
        "solute_chebi2": "channel",
        "solute_chebi3": "channel",
        "solute_text": "Cl-",
        "solute_text2": "channel",
        "solute_text3": "channel",
        "source_fma": "http://purl.obolibrary.org/obo/FMA_9673",
        "source_fma2": "channel",
        "source_fma3": "channel",
        "variable_text": "G_sc_Cl",
        "variable_text2": "channel",
        "variable_text3": "channel"
    },
    {
        "med_fma": "http://purl.obolibrary.org/obo/FMA_84669",
        "med_pr": "http://purl.obolibrary.org/obo/PR_P15387",
        "med_pr_text": "potassium voltage-gated channel subfamily B member 1 (rat)",
        "med_pr_text_syn": "P15387",
        "model_entity": "chang_fujita_b_1999.cellml#sc_potassium_flux.G_sc_K",
        "model_entity2": "",
        "model_entity3": "",
        "protein_name": "http://purl.obolibrary.org/obo/CL_0000066",
        "sink_fma": "http://purl.obolibrary.org/obo/FMA_66836",
        "sink_fma2": "channel",
        "sink_fma3": "channel",
        "solute_chebi": "http://purl.obolibrary.org/obo/CHEBI_29103",
        "solute_chebi2": "channel",
        "solute_chebi3": "channel",
        "solute_text": "K+",
        "solute_text2": "channel",
        "solute_text3": "channel",
        "source_fma": "http://purl.obolibrary.org/obo/FMA_9673",
        "source_fma2": "channel",
        "source_fma3": "channel",
        "variable_text": "G_sc_K",
        "variable_text2": "channel",
        "variable_text3": "channel"
    },
    {
        "med_fma": "http://purl.obolibrary.org/obo/FMA_67394",
        "med_pr": "http://purl.obolibrary.org/obo/PR_Q9Z0S6",
        "med_pr_text": "claudin-10 (mouse)",
        "med_pr_text_syn": "CLDN10A",
        "model_entity": "chang_fujita_b_1999.cellml#ms_sodium_flux.G_ms_Na",
        "model_entity2": "",
        "model_entity3": "",
        "protein_name": "http://purl.obolibrary.org/obo/CL_0000066",
        "sink_fma": "http://purl.obolibrary.org/obo/FMA_9673",
        "sink_fma2": "diffusiveflux",
        "sink_fma3": "diffusiveflux",
        "solute_chebi": "http://purl.obolibrary.org/obo/CHEBI_29101",
        "solute_chebi2": "diffusiveflux",
        "solute_chebi3": "diffusiveflux",
        "solute_text": "Na+",
        "solute_text2": "diffusiveflux",
        "solute_text3": "diffusiveflux",
        "source_fma": "http://purl.obolibrary.org/obo/FMA_74550",
        "source_fma2": "diffusiveflux",
        "source_fma3": "diffusiveflux",
        "variable_text": "G_ms_Na",
        "variable_text2": "diffusiveflux",
        "variable_text3": "diffusiveflux"
    },
    {
        "med_fma": "http://purl.obolibrary.org/obo/FMA_67394",
        "med_pr": "http://purl.obolibrary.org/obo/PR_O35054",
        "med_pr_text": "claudin-4 (mouse)",
        "med_pr_text_syn": "CPETR1",
        "model_entity": "chang_fujita_b_1999.cellml#ms_chloride_flux.G_ms_Cl",
        "model_entity2": "",
        "model_entity3": "",
        "protein_name": "http://purl.obolibrary.org/obo/CL_0000066",
        "sink_fma": "http://purl.obolibrary.org/obo/FMA_9673",
        "sink_fma2": "diffusiveflux",
        "sink_fma3": "diffusiveflux",
        "solute_chebi": "http://purl.obolibrary.org/obo/CHEBI_17996",
        "solute_chebi2": "diffusiveflux",
        "solute_chebi3": "diffusiveflux",
        "solute_text": "Cl-",
        "solute_text2": "diffusiveflux",
        "solute_text3": "diffusiveflux",
        "source_fma": "http://purl.obolibrary.org/obo/FMA_74550",
        "source_fma2": "diffusiveflux",
        "source_fma3": "diffusiveflux",
        "variable_text": "G_ms_Cl",
        "variable_text2": "diffusiveflux",
        "variable_text3": "diffusiveflux"
    },
    {
        "med_fma": "http://purl.obolibrary.org/obo/FMA_67394",
        "med_pr": "http://purl.obolibrary.org/obo/PR_F1LZ52",
        "med_pr_text": "kelch-like protein 3 (rat)",
        "med_pr_text_syn": "F1LZ52",
        "model_entity": "chang_fujita_b_1999.cellml#ms_potassium_flux.G_ms_K",
        "model_entity2": "",
        "model_entity3": "",
        "protein_name": "http://purl.obolibrary.org/obo/CL_0000066",
        "sink_fma": "http://purl.obolibrary.org/obo/FMA_9673",
        "sink_fma2": "diffusiveflux",
        "sink_fma3": "diffusiveflux",
        "solute_chebi": "http://purl.obolibrary.org/obo/CHEBI_29103",
        "solute_chebi2": "diffusiveflux",
        "solute_chebi3": "diffusiveflux",
        "solute_text": "K+",
        "solute_text2": "diffusiveflux",
        "solute_text3": "diffusiveflux",
        "source_fma": "http://purl.obolibrary.org/obo/FMA_74550",
        "source_fma2": "diffusiveflux",
        "source_fma3": "diffusiveflux",
        "variable_text": "G_ms_K",
        "variable_text2": "diffusiveflux",
        "variable_text3": "diffusiveflux"
    }
]

# PMR sparql endpoint
sparqlendpoint = "https://models.physiomeproject.org/pmr2_virtuoso_search"

# import component
workspaceURL = "https://models.physiomeproject.org/workspace/267/rawfile/HEAD/"

# reference URIs of anatomical locations
lumen_fma = "http://purl.obolibrary.org/obo/FMA_74550"
cytosol_fma = "http://purl.obolibrary.org/obo/FMA_66836"
interstitialfluid_fma = "http://purl.obolibrary.org/obo/FMA_9673"


# ODE based equation
def mathEq(vConcentration, vFlux, sign):
    return "<math xmlns=\"http://www.w3.org/1998/Math/MathML\">" \
           "<apply id=" + '"' + vConcentration + "_diff_eq" + '"' + ">" + \
           "<eq/>" \
           "<apply>" \
           "<diff/>" \
           "<bvar>" \
           "<ci>time</ci>" \
           "</bvar> " \
           "<ci>" + vConcentration + "</ci>" + \
           "</apply>" \
           "<apply>" \
           "<" + sign + "/>" + \
           "<ci>" + vFlux + "</ci>" + \
           "</apply>" \
           "</apply>" \
           "</math>"


# assign plus or minus sign in the ODE based equations
def odeSignNotation(compartment, source_fma, sink_fma):
    # lumen
    if compartment.getName() == "lumen":
        if source_fma == lumen_fma and sink_fma == cytosol_fma:
            sign = "minus"
        else:
            sign = "plus"

    # cytosol
    if compartment.getName() == "cytosol":
        if source_fma == cytosol_fma and sink_fma == lumen_fma:
            sign = "minus"
        elif source_fma == cytosol_fma and sink_fma == interstitialfluid_fma:
            sign = "minus"
        elif source_fma == lumen_fma and sink_fma == cytosol_fma:
            sign = "plus"
        elif source_fma == interstitialfluid_fma and sink_fma == cytosol_fma:
            sign = "plus"

    # interstitial fluid
    if compartment.getName() == "interstitialfluid":
        if source_fma == interstitialfluid_fma and sink_fma == cytosol_fma:
            sign = "minus"
        else:
            sign = "plus"

    # epithelial
    if compartment.getName() == "epithelial":
        if source_fma == lumen_fma and sink_fma == cytosol_fma:
            sign = "plus"
        elif source_fma == cytosol_fma and sink_fma == lumen_fma:
            sign = "minus"
        elif source_fma == cytosol_fma and sink_fma == interstitialfluid_fma:
            sign = "minus"
        elif source_fma == interstitialfluid_fma and sink_fma == cytosol_fma:
            sign = "plus"

    return sign


# user-defined function to instantiate a time component and its variable attributes
def createComponent(v, name, unit, interface, initialvalue, component, v2):
    v.setName(name)
    v.setUnits(unit)
    v.setInterfaceType(interface)

    if initialvalue != None:
        v.setInitialValue(initialvalue)

    if v2 == None:
        v.setId(component.getName() + "." + v.getName())
    else:
        v.setId(component.getName() + "." + v2.getName())

    component.addVariable(v)


# concentration sparql to get a result for a given FMA and CHEBI
def concentrationSparql(fma, chebi):
    return "PREFIX semsim: <http://www.bhi.washington.edu/SemSim#>" \
           "PREFIX ro: <http://www.obofoundry.org/ro/ro.owl#>" \
           "PREFIX dcterms: <http://purl.org/dc/terms/>" \
           "SELECT ?modelEntity " \
           "WHERE { " \
           "?modelEntity semsim:isComputationalComponentFor ?model_prop. " \
           "?model_prop semsim:hasPhysicalDefinition <http://identifiers.org/opb/OPB_00340>. " \
           "?model_prop semsim:physicalPropertyOf ?source_entity. " \
           "?source_entity ro:part_of ?source_part_of_entity. " \
           "?source_part_of_entity semsim:hasPhysicalDefinition <" + fma + ">. " + \
           "?source_entity semsim:hasPhysicalDefinition <" + chebi + ">. " + \
           "}"


# instantiate source url and create an imported component in the new model
def instantiateImportedComponent(sourceurl, component, m):
    imp = ImportSource()
    imp.setUrl(sourceurl)

    importedComponent = Component()
    importedComponent.setName(component)
    importedComponent.setSourceComponent(imp, component)

    m.addComponent(importedComponent)


# process model entities and source models' urls
def processModelEntity(modelentity, m):
    cellml_model_name = modelentity[0:modelentity.find('#')]
    component_variable = modelentity[modelentity.find('#') + 1:len(modelentity)]
    component = component_variable[:component_variable.find('.')]
    sourceurl = workspaceURL + cellml_model_name
    instantiateImportedComponent(sourceurl, component, m)
