import copy;
from variable_table import VarTable, Variable, Dimension

last_type = 0;


COUNTERS = { #different types counters
    "int" : 0,
    "double" : 0,
    "boolean" : 0,
}

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

    def __init__(self, return_type = None, num_params = 0): #return type and params counter
        self.num_params = num_params;
        self.return_type = return_type;
        self.var_table = VarTable();

    def addParam(self):
        self.num_params += 1;

    def setReturnType(self, return_t):
        self.return_type = return_t;

    def getVarTable(self):
        return self.var_table;

    def getNumParams(self):
        return self.num_params;

    def getReturnType(self):
        return self.return_type;

    def hasVariable(self, key):
        return self.var_table.exists(key)

    def addVariable(self, id, var_type=None):
        self.var_table.addVariable(id, var_type)

    def getVariable(self, id):
        return self.var_table.getVariable(id)





GLOBAL = {};


FUNCS_STACK = [];

LOCALS = {};
