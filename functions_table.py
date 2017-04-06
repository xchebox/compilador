import copy;

last_type = 0;

TYPES = { #different types
    "int" : 0,
    "double" : 1,
    "string" : 2,
    "boolean" : 3,
}

COUNTERS = { #different types counters
    "int" : 0,
    "double" : 0,
    "string" : 0
}


class Variable():

    def __init__(self, var_memory, var_type):
        self.memory = var_memory;
        self.type = var_type;

    def getType(self):
        return self.type

    def getMemory(self):
        return self.memory

    def setType(self, var_type):
        self.type = var_type;

class Function():

    def __init__(self, return_type = None, num_params = 0): #return type and params counter
        self.num_params = num_params;
        self.return_type = return_type;
        self.var_table = {};

    def addParam(self):
        self.num_params += 1;

    def setReturnType(self, return_t):
        self.return_type = return_t;

    def setVarTable(self, table):
        self.var_table = copy.deepcopy(table);

    def getVarTable(self):
        return self.var_table;

    def getNumParams(self):
        return self.num_params;

    def getReturnType(self):
        return self.return_type;





GLOBAL = {};

FUNCTIONS = {};

FUNCS_STACK = [];

LOCALS = {};
