import numpy
from operators import operators
from operands import TYPES
semantic_cube = numpy.zeros((len(TYPES), len(operators), len(TYPES)))

#semantic rules
#0 PLUS
semantic_cube[TYPES['int'],operators['PLUS'],TYPES['int']]                  = TYPES['int']
semantic_cube[TYPES['int'],operators['PLUS'],TYPES['double']]               = TYPES['int']
semantic_cube[TYPES['int'],operators['PLUS'],TYPES['boolean']]              = -1
semantic_cube[TYPES['double'],operators['PLUS'],TYPES['int']]               = TYPES['int']
semantic_cube[TYPES['double'],operators['PLUS'],TYPES['double']]            = TYPES['double']
semantic_cube[TYPES['double'],operators['PLUS'],TYPES['boolean']]           = -1
semantic_cube[TYPES['boolean'],operators['PLUS'],TYPES['int']]              = -1
semantic_cube[TYPES['boolean'],operators['PLUS'],TYPES['double']]           = -1
semantic_cube[TYPES['boolean'],operators['PLUS'],TYPES['boolean']]          = -1
#1 MINUS
semantic_cube[TYPES['int'],operators['MINUS'],TYPES['int']]                 = TYPES['int']
semantic_cube[TYPES['int'],operators['MINUS'],TYPES['double']]              = TYPES['int']
semantic_cube[TYPES['int'],operators['MINUS'],TYPES['boolean']]             = -1
semantic_cube[TYPES['double'],operators['MINUS'],TYPES['int']]              = TYPES['int']
semantic_cube[TYPES['double'],operators['MINUS'],TYPES['double']]           = TYPES['double']
semantic_cube[TYPES['double'],operators['MINUS'],TYPES['boolean']]          = -1
semantic_cube[TYPES['boolean'],operators['MINUS'],TYPES['int']]             = -1
semantic_cube[TYPES['boolean'],operators['MINUS'],TYPES['double']]          = -1
semantic_cube[TYPES['boolean'],operators['MINUS'],TYPES['boolean']]         = -1
#2 MULT
semantic_cube[TYPES['int'],operators['MULT'],TYPES['int']]                  = TYPES['int']
semantic_cube[TYPES['int'],operators['MULT'],TYPES['double']]               = TYPES['double']
semantic_cube[TYPES['int'],operators['MULT'],TYPES['boolean']]              = -1
semantic_cube[TYPES['double'],operators['MULT'],TYPES['int']]               = TYPES['double']
semantic_cube[TYPES['double'],operators['MULT'],TYPES['double']]            = TYPES['double']
semantic_cube[TYPES['double'],operators['MULT'],TYPES['boolean']]           = -1
semantic_cube[TYPES['boolean'],operators['MULT'],TYPES['int']]              = -1
semantic_cube[TYPES['boolean'],operators['MULT'],TYPES['double']]           = -1
semantic_cube[TYPES['boolean'],operators['MULT'],TYPES['boolean']]          = -1
#3 DIVIDE
semantic_cube[TYPES['int'],operators['DIVIDE'],TYPES['int']]                = TYPES['double']
semantic_cube[TYPES['int'],operators['DIVIDE'],TYPES['double']]             = TYPES['int']
semantic_cube[TYPES['int'],operators['DIVIDE'],TYPES['boolean']]            = -1
semantic_cube[TYPES['double'],operators['DIVIDE'],TYPES['int']]             = TYPES['double']
semantic_cube[TYPES['double'],operators['DIVIDE'],TYPES['double']]          = TYPES['double']
semantic_cube[TYPES['double'],operators['DIVIDE'],TYPES['boolean']]         = -1
semantic_cube[TYPES['boolean'],operators['DIVIDE'],TYPES['int']]            = -1
semantic_cube[TYPES['boolean'],operators['DIVIDE'],TYPES['double']]         = -1
semantic_cube[TYPES['boolean'],operators['DIVIDE'],TYPES['boolean']]        = -1
#4 EQUALS
semantic_cube[TYPES['int'],operators['EQUALS'],TYPES['int']]                = TYPES['boolean']
semantic_cube[TYPES['int'],operators['EQUALS'],TYPES['double']]             = TYPES['boolean']
semantic_cube[TYPES['int'],operators['EQUALS'],TYPES['boolean']]            = TYPES['boolean']
semantic_cube[TYPES['double'],operators['EQUALS'],TYPES['int']]             = TYPES['boolean']
semantic_cube[TYPES['double'],operators['EQUALS'],TYPES['double']]          = TYPES['boolean']
semantic_cube[TYPES['double'],operators['EQUALS'],TYPES['boolean']]         = TYPES['boolean']
semantic_cube[TYPES['boolean'],operators['EQUALS'],TYPES['int']]            = TYPES['boolean']
semantic_cube[TYPES['boolean'],operators['EQUALS'],TYPES['double']]         = TYPES['boolean']
semantic_cube[TYPES['boolean'],operators['EQUALS'],TYPES['boolean']]        = TYPES['boolean']
#5 ASSIGN
semantic_cube[TYPES['int'],operators['ASSIGN'],TYPES['int']]                = TYPES['int']
semantic_cube[TYPES['int'],operators['ASSIGN'],TYPES['double']]             = TYPES['int']
semantic_cube[TYPES['int'],operators['ASSIGN'],TYPES['boolean']]            = -1
semantic_cube[TYPES['double'],operators['ASSIGN'],TYPES['int']]             = TYPES['int']
semantic_cube[TYPES['double'],operators['ASSIGN'],TYPES['double']]          = TYPES['double']
semantic_cube[TYPES['double'],operators['ASSIGN'],TYPES['boolean']]         = -1
semantic_cube[TYPES['boolean'],operators['ASSIGN'],TYPES['int']]            = -1
semantic_cube[TYPES['boolean'],operators['ASSIGN'],TYPES['double']]         = -1
semantic_cube[TYPES['boolean'],operators['ASSIGN'],TYPES['boolean']]        = TYPES['boolean']
#6 LESS
semantic_cube[TYPES['int'],operators['LESS'],TYPES['int']]                  = TYPES['boolean']
semantic_cube[TYPES['int'],operators['LESS'],TYPES['double']]               = TYPES['boolean']
semantic_cube[TYPES['int'],operators['LESS'],TYPES['boolean']]              = TYPES['boolean']
semantic_cube[TYPES['double'],operators['LESS'],TYPES['int']]               = TYPES['boolean']
semantic_cube[TYPES['double'],operators['LESS'],TYPES['double']]            = TYPES['boolean']
semantic_cube[TYPES['double'],operators['LESS'],TYPES['boolean']]           = TYPES['boolean']
semantic_cube[TYPES['boolean'],operators['LESS'],TYPES['int']]              = TYPES['boolean']
semantic_cube[TYPES['boolean'],operators['LESS'],TYPES['double']]           = TYPES['boolean']
semantic_cube[TYPES['boolean'],operators['LESS'],TYPES['boolean']]          = TYPES['boolean']
#7 GREATER
semantic_cube[TYPES['int'],operators['GREATER'],TYPES['int']]               = TYPES['boolean']
semantic_cube[TYPES['int'],operators['GREATER'],TYPES['double']]            = TYPES['boolean']
semantic_cube[TYPES['int'],operators['GREATER'],TYPES['boolean']]           = TYPES['boolean']
semantic_cube[TYPES['double'],operators['GREATER'],TYPES['int']]            = TYPES['boolean']
semantic_cube[TYPES['double'],operators['GREATER'],TYPES['double']]         = TYPES['boolean']
semantic_cube[TYPES['double'],operators['GREATER'],TYPES['boolean']]        = TYPES['boolean']
semantic_cube[TYPES['boolean'],operators['GREATER'],TYPES['int']]           = TYPES['boolean']
semantic_cube[TYPES['boolean'],operators['GREATER'],TYPES['double']]        = TYPES['boolean']
semantic_cube[TYPES['boolean'],operators['GREATER'],TYPES['boolean']]       = TYPES['boolean']
#8 AND
semantic_cube[TYPES['int'],operators['AND'],TYPES['int']]                   = TYPES['boolean']
semantic_cube[TYPES['int'],operators['AND'],TYPES['double']]                = TYPES['boolean']
semantic_cube[TYPES['int'],operators['AND'],TYPES['boolean']]               = TYPES['boolean']
semantic_cube[TYPES['double'],operators['AND'],TYPES['int']]                = TYPES['boolean']
semantic_cube[TYPES['double'],operators['AND'],TYPES['double']]             = TYPES['boolean']
semantic_cube[TYPES['double'],operators['AND'],TYPES['boolean']]            = TYPES['boolean']
semantic_cube[TYPES['boolean'],operators['AND'],TYPES['int']]               = TYPES['boolean']
semantic_cube[TYPES['boolean'],operators['AND'],TYPES['double']]            = TYPES['boolean']
semantic_cube[TYPES['boolean'],operators['AND'],TYPES['boolean']]           = TYPES['boolean']
#9 OR
semantic_cube[TYPES['int'],operators['OR'],TYPES['int']]                    = TYPES['boolean']
semantic_cube[TYPES['int'],operators['OR'],TYPES['double']]                 = TYPES['boolean']
semantic_cube[TYPES['int'],operators['OR'],TYPES['boolean']]                = TYPES['boolean']
semantic_cube[TYPES['double'],operators['OR'],TYPES['int']]                 = TYPES['boolean']
semantic_cube[TYPES['double'],operators['OR'],TYPES['double']]              = TYPES['boolean']
semantic_cube[TYPES['double'],operators['OR'],TYPES['boolean']]             = TYPES['boolean']
semantic_cube[TYPES['boolean'],operators['OR'],TYPES['int']]                = TYPES['boolean']
semantic_cube[TYPES['boolean'],operators['OR'],TYPES['double']]             = TYPES['boolean']
semantic_cube[TYPES['boolean'],operators['OR'],TYPES['boolean']]            = TYPES['boolean']
