from libcellml import Model, Printer

m = Model()

# model ID
modelId = "modelID"
m.setId(modelId)

# model name
modelName = "modelName"
m.setName(modelName)

print("Model: ", m, "\nModel Id: ", m.getId(), "\nModel Name: ", m.getName())

# construct a model
printer = Printer()
model = printer.printModel(m)

print("\nModel:\n", model)

# save in a file
f = open("model.xml", "w")
f.write(model)
