class VarTable:
    def __init__(self):
        self.table = {}

    def exists(self, key):
        return self.table.has_key(key)

    def addVariable(self, id , var_type = None):
        self.table[id] = Variable(0, var_type)

    def getVariable(self, id):
        return self.table[id]

class Variable:

    def __init__(self, var_memory, var_type):
        self.memory = var_memory; #virtual memory/counter
        self.type = var_type; #variable type
        self.dimension = [] #not an array

    def getType(self):
        return self.type

    def getMemory(self):
        return self.memory

    def setType(self, var_type):
        self.type = var_type;

    def addDimension(self, newDimension):
        self.dimension.append(newDimension)
