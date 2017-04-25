from operands import TYPES

class VarTable:
    def __init__(self):
        self.table = {}

    def exists(self, key):
        return self.table.has_key(key)

    def addVariable(self, id , var_type = None, varMemory = None):
        self.table[id] = Variable(varMemory, var_type)

    def setVarType(self, var, var_type = None):
        self.table[var].setType(var_type)



    def getVariable(self, id):
        return self.table[id]

class Dimension:
    def __init__(self, size):
        self.size = size
        self.m = 0

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
        self.dimension.append(Dimension(newDimension))

        #calculates m's and return the total size of array
    def getTotalMemoryDimension(self):
        if len (self.dimension) == 0:
            return 1
        if len (self.dimension) == 1:
            return self.dimension[0].size
        totalMemory = 1
        for d in self.dimension:
            totalMemory *= d.size
            #at this point we have the total memory
        for d in self.dimension:
            d.m = totalMemory/d.size#calculates all m's
        self.dimension[len(self.dimension) - 1].m = 0 #last dimension m's 0

        return  self.dimension[0].m * self.dimension[0].size #Total size

    def getDimension(self):
        return self.dimension
