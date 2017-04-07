class VarTable:
    def __init__(self):
        self.table = {}

    def exists(self, key):
        return self.table.has_key(key)

    def addVariable(self, id , var_type = None):
        self.table[id] = Variable(0, var_type)

    def getVariable(self, id):
        return self.table[id]

class Variable():

    def __init__(self, var_memory, var_type):
        self.memory = var_memory; #virtual memory/counter
        self.type = var_type; #variable type
        self.dimension = None #not an array

    def getType(self):
        return self.type

    def getMemory(self):
        return self.memory

    def setType(self, var_type):
        self.type = var_type;

    def addDimension(self, newDimension):
        d = self.dimension
        if not d is None:
            while not d.getNextDimension is None:
                d = d.getNextDimension #checks for last dimension
        d = Dimension(newDimension)


class Dimension():
    def __init__(self, newDimension):
        self.dimension = newDimension #dimension added upper limit
        self.nextDimension = None # no next dimension

    def getNextDimension(self):
        return self.nextDimension
