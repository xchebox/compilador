import copy;
from variable_table import VarTable, Variable


class FunctionTable:
    def __init__(self):
        self.table = {'global':Function()}

    def exists(self, key):
        return self.table.has_key(key)

    def addFunction(self, id):
        self.table[id] = Function()

    def getFunctionTable(self):
        return self.table

    def getFunction(self,id):
        return self.table[id]


class Function():

    def __init__(self, return_type = None): #return type and params counter
        self.params = []
        self.return_type = 0
        self.var_table = VarTable()
        self.firstQuadruple = 0
        self.intMemoryRequired = 0
        self.doubleMemoryRequired = 0
        self.booleanMemoryRequired = 0

    def setFirstQuadruple(self, quadruple):
        self.firstQuadruple = quadruple

    def getFirstQuadruple(self):
        return self.firstQuadruple

    def addParam(self, paramName):
        self.params.append(paramName)

    def setReturnType(self, return_t):
        self.return_type = return_t

    def getVarTable(self):
        return self.var_table

    def getParams(self):
        return self.params

    def getReturnType(self):
        return self.return_type

    def hasVariable(self, key):
        return self.var_table.exists(key)

    def addVariable(self, id, var_type=None):
        self.var_table.addVariable(id, var_type)

    def getVariable(self, id):
        return self.var_table.getVariable(id)

    def getIntMemoryRequired(self):
        return self.intMemoryRequired

    def getDoubleMemoryRequired(self):
        return self.doubleMemoryRequired

    def getBooleanMemoryRequired(self):
        return self.booleanMemoryRequired

    def increaseIntMemoryRequired(self, amountToIncrement):
        self.intMemoryRequired += amountToIncrement

    def increaseBooleanMemoryRequired(self, amountToIncrement):
        self.booleanMemoryRequired += amountToIncrement

    def increaseDoubleMemoryRequired(self, amountToIncrement):
        self.doubleMemoryRequired += amountToIncrement
