from operands import TYPES

class VarTable:
    def __init__(self):
        self.table = {}
        self.iCounter = 0 #counter for integers
        self.dCounter = 0 #counter for doubles
        self.bCounter = 0 #counter for booleans

    def exists(self, key):
        return self.table.has_key(key)

    def addVariable(self, id , var_type = None, varMemory = None):
        self.table[id] = Variable(varMemory, var_type)

    def setVarType(self, var, var_type = None):
        varMemory = 0
        if var_type == TYPES['int']:
            varMemory = self.iCounter
            self.iCounter += 1
        if var_type == TYPES['double']:
            varMemory = self.dCounter
            self.dCounter += 1
        if var_type == TYPES['boolean']:
            varMemory = self.bCounter
            self.bCounter += 1
        self.table[var].setType(var_type)
        self.table[var].setMemory(varMemory)



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

    def setMemory(self, var_memory):
        self.memory = var_memory

    def setType(self, var_type):
        self.type = var_type;

    def addDimension(self, newDimension):
        self.dimension.append(newDimension)

    def getDimension(self):
        return self.dimension
