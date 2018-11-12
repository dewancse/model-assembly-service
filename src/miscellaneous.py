import requests
from xml.dom import pulldom

modelEntityList = ['weinstein_1995.cellml#Concentrations.C_ext_Na', 'mackenzie_1996.cellml#NBC_current.J_Na']
componentList = []

for index in range(len(modelEntityList)):
    workspaceURL = 'https://models.physiomeproject.org/workspace/267/rawfile/HEAD/'
    modelName = modelEntityList[index][0:modelEntityList[index].find('#')]
    r = requests.get(workspaceURL + modelName)

    # extract name of component from a cellml model entity
    componentVariable = modelEntityList[index][modelEntityList[index].find('#') + 1:len(modelEntityList[index])]
    componentName = componentVariable[:componentVariable.find('.')]

    # traverse xml dom, find above component name, and pull that including its children
    doc = pulldom.parseString(r.text)
    for event, node in doc:
        if event == pulldom.START_ELEMENT and node.tagName == 'component':
            if node.getAttribute('name') == componentName:
                doc.expandNode(node)
                componentList.insert(index, node.toxml())

for component in componentList:
    print(component)

# find cellml model version 1.0 or 2.0
# import requests
# from xml.dom import pulldom
#
# workspaceURL = 'https://models.physiomeproject.org/workspace/267/rawfile/HEAD/'
# r = requests.get(workspaceURL + 'weinstein_1995.cellml')
#
# doc = pulldom.parseString(r.text)
# for event, node in doc:
#     if event == pulldom.START_ELEMENT and node.tagName == 'model':
#         # access directly by attribute name
#         print(node.getAttribute('xmlns:cmeta'))
#         # loop through to access all attributes
#         for index in range(node.attributes.length):
#             print('name:', node.attributes.item(index).name, ' value:', node.attributes.item(index).value)
