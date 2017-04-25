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

        self.intLocalMemoryRequired = 0
        self.doubleLocalMemoryRequired = 0
        self.booleanLocalMemoryRequired = 0

        self.intConstMemoryRequired = 0
        self.doubleConstMemoryRequired = 0
        self.booleanConstMemoryRequired = 0

        self.intTempMemoryRequired = 0
        self.doubleTempMemoryRequired = 0
        self.booleanTempMemoryRequired = 0

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

    def getIntLocalMemoryRequired(self):
        return self.intLocalMemoryRequired

    def getDoubleLocalMemoryRequired(self):
        return self.doubleLocalMemoryRequired

    def getBooleanLocalMemoryRequired(self):
        return self.booleanLocalMemoryRequired

    def getIntConstMemoryRequired(self):
        return self.intConstMemoryRequired

    def getDoubleConstMemoryRequired(self):
        return self.doubleConstMemoryRequired

    def getBooleanConstMemoryRequired(self):
        return self.booleanConstMemoryRequired

    def getIntTempMemoryRequired(self):
        return self.intTempMemoryRequired

    def getDoubleTempMemoryRequired(self):
        return self.doubleTempMemoryRequired

    def getBooleanTempMemoryRequired(self):
        return self.booleanTempMemoryRequired

    def increaseIntLocalMemoryRequired(self, amountToIncrement):
        self.intLocalMemoryRequired += amountToIncrement

    def increaseBooleanLocalMemoryRequired(self, amountToIncrement):
        self.booleanLocalMemoryRequired += amountToIncrement

    def increaseDoubleLocalMemoryRequired(self, amountToIncrement):
        self.doubleLocalMemoryRequired += amountToIncrement

    def increaseIntConstMemoryRequired(self, amountToIncrement):
        self.intConstMemoryRequired += amountToIncrement

    def increaseBooleanConstMemoryRequired(self, amountToIncrement):
        self.booleanConstMemoryRequired += amountToIncrement

    def increaseDoubleConstMemoryRequired(self, amountToIncrement):
        self.doubleConstMemoryRequired += amountToIncrement

    def increaseIntTempMemoryRequired(self, amountToIncrement):
        self.intTempMemoryRequired += amountToIncrement

    def increaseBooleanTempMemoryRequired(self, amountToIncrement):
        self.booleanTempMemoryRequired += amountToIncrement

    def increaseDoubleTempMemoryRequired(self, amountToIncrement):
        self.doubleTempMemoryRequired += amountToIncrement
