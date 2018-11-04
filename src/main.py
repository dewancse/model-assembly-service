import requests
from xml.dom import pulldom

modelEntityList = ['weinstein_1995.cellml#Concentrations.C_ext_Na', 'mackenzie_1996.cellml#NBC_current.J_Na']
componentList = []

for index in range(len(modelEntityList)):
    print(index, modelEntityList[index])

    workspaceURL = 'https://models.physiomeproject.org/workspace/267/rawfile/HEAD/'
    modelName = modelEntityList[index][0:modelEntityList[index].find('#')]
    print(modelName)
    r = requests.get(workspaceURL + modelName)

    # extract name of component from a cellml model entity
    componentVariable = modelEntityList[index][modelEntityList[index].find('#') + 1:len(modelEntityList[index])]
    componentName = componentVariable[:componentVariable.find('.')]

    # traverse xml doc
    doc = pulldom.parseString(r.text)
    for event, node in doc:
        if event == pulldom.START_ELEMENT and node.tagName == 'component':
            if node.getAttribute('name') == componentName:
                doc.expandNode(node)
                componentList.insert(index, node.toxml())

for component in componentList:
    print(component)
