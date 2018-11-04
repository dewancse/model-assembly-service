import requests
from xml.dom import pulldom

workspaceURL = 'https://models.physiomeproject.org/workspace/267/rawfile/HEAD/'
weinstein = requests.get(workspaceURL + 'weinstein_1995.cellml')

# extract name of component from a cellml model entity
modelEntity = 'weinstein_1995.cellml#Concentrations.C_ext_Na'
componentVariable = modelEntity[modelEntity.find('#') + 1:len(modelEntity)]
componentName = componentVariable[:componentVariable.find('.')]

# weinstein_1996
doc = pulldom.parseString(weinstein.text)
for event, node in doc:
    if event == pulldom.START_ELEMENT and node.tagName == 'component':
        if node.getAttribute('name') == componentName:
            doc.expandNode(node)
            weinsteinComponent = node.toxml()
            print(weinsteinComponent)

mackenzie = requests.get(workspaceURL + 'mackenzie_1996.cellml')

# extract name of component from a cellml model entity
modelEntity = 'mackenzie_1996.cellml#NBC_current.J_Na'
componentVariable = modelEntity[modelEntity.find('#') + 1:len(modelEntity)]
componentName = componentVariable[:componentVariable.find('.')]

# mackenzie_1996
doc = pulldom.parseString(mackenzie.text)
for event, node in doc:
    if event == pulldom.START_ELEMENT and node.tagName == 'component':
        if node.getAttribute('name') == componentName:
            doc.expandNode(node)
            mackenzieComponent = node.toxml()
            print(mackenzieComponent)
