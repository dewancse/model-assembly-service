from libcellml import Model, Printer, Component, ImportSource

# Instantiate a model
m = Model()

# model ID
modelId = "modelID"
m.setId(modelId)

# model name
modelName = "modelName"
m.setName(modelName)

print("Model: ", m, "\nModel Id: ", m.getId(), "\nModel Name: ", m.getName())

# add component
c = Component()
m.addComponent(c)

# pre-generated JSON model recipe
modelRecipe = [
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
];

print("\nModel recipe: ", modelRecipe)

# import component
workspaceURL = "https://models.physiomeproject.org/workspace/267/rawfile/HEAD/"


# instantiate source url and create an imported component
def instantiateComponent(sourceUrl, componentName):
    imp = ImportSource()
    imp.setUrl(sourceUrl)

    importedComponent = Component()
    importedComponent.setName(componentName)
    importedComponent.setSourceComponent(imp, componentName)

    m.addComponent(importedComponent)


# user-defined function for components instantiation
def processItem(item):
    cellmlModelName = item[0:item.find('#')]
    componentVariable = item[item.find('#') + 1:len(item)]
    componentName = componentVariable[:componentVariable.find('.')]
    sourceUrl = workspaceURL + cellmlModelName
    instantiateComponent(sourceUrl, componentName)


# iterate through model recipe to import components from source models
for item in modelRecipe:
    if item['model_entity'] != "":
        processItem(item['model_entity'])
    if item['model_entity2'] != "":
        processItem(item['model_entity2'])
    if item['model_entity3'] != "":
        processItem(item['model_entity3'])

# serialize and print a model
printer = Printer()
model = printer.printModel(m)

print("\nModel:", model)

# write in a file
f = open("model.xml", "w")
f.write(model)
