from operators import operators
from operands import TYPES
semantic_cube = []

for i in TYPES:
    types1 = []
    for j in operators:
        ope = []
        for k in TYPES:
            types2 = -1
            ope.append(types2)
        types1.append(ope)
    semantic_cube.append(types1)

#semantic rules
#0 +
semantic_cube[TYPES['int']][operators['+']][TYPES['int']]                  = TYPES['int']
semantic_cube[TYPES['int']][operators['+']][TYPES['double']]               = TYPES['int']
semantic_cube[TYPES['int']][operators['+']][TYPES['boolean']]              = -1
semantic_cube[TYPES['double']][operators['+']][TYPES['int']]               = TYPES['int']
semantic_cube[TYPES['double']][operators['+']][TYPES['double']]            = TYPES['double']
semantic_cube[TYPES['double']][operators['+']][TYPES['boolean']]           = -1
semantic_cube[TYPES['boolean']][operators['+']][TYPES['int']]              = -1
semantic_cube[TYPES['boolean']][operators['+']][TYPES['double']]           = -1
semantic_cube[TYPES['boolean']][operators['+']][TYPES['boolean']]          = -1
#1 -
semantic_cube[TYPES['int']][operators['-']][TYPES['int']]                 = TYPES['int']
semantic_cube[TYPES['int']][operators['-']][TYPES['double']]              = TYPES['int']
semantic_cube[TYPES['int']][operators['-']][TYPES['boolean']]             = -1
semantic_cube[TYPES['double']][operators['-']][TYPES['int']]              = TYPES['int']
semantic_cube[TYPES['double']][operators['-']][TYPES['double']]           = TYPES['double']
semantic_cube[TYPES['double']][operators['-']][TYPES['boolean']]          = -1
semantic_cube[TYPES['boolean']][operators['-']][TYPES['int']]             = -1
semantic_cube[TYPES['boolean']][operators['-']][TYPES['double']]          = -1
semantic_cube[TYPES['boolean']][operators['-']][TYPES['boolean']]         = -1
#2 *
semantic_cube[TYPES['int']][operators['*']][TYPES['int']]                  = TYPES['int']
semantic_cube[TYPES['int']][operators['*']][TYPES['double']]               = TYPES['double']
semantic_cube[TYPES['int']][operators['*']][TYPES['boolean']]              = -1
semantic_cube[TYPES['double']][operators['*']][TYPES['int']]               = TYPES['double']
semantic_cube[TYPES['double']][operators['*']][TYPES['double']]            = TYPES['double']
semantic_cube[TYPES['double']][operators['*']][TYPES['boolean']]           = -1
semantic_cube[TYPES['boolean']][operators['*']][TYPES['int']]              = -1
semantic_cube[TYPES['boolean']][operators['*']][TYPES['double']]           = -1
semantic_cube[TYPES['boolean']][operators['*']][TYPES['boolean']]          = -1
#3 /
semantic_cube[TYPES['int']][operators['/']][TYPES['int']]                = TYPES['int']
semantic_cube[TYPES['int']][operators['/']][TYPES['double']]             = TYPES['double']
semantic_cube[TYPES['int']][operators['/']][TYPES['boolean']]            = -1
semantic_cube[TYPES['double']][operators['/']][TYPES['int']]             = TYPES['double']
semantic_cube[TYPES['double']][operators['/']][TYPES['double']]          = TYPES['double']
semantic_cube[TYPES['double']][operators['/']][TYPES['boolean']]         = -1
semantic_cube[TYPES['boolean']][operators['/']][TYPES['int']]            = -1
semantic_cube[TYPES['boolean']][operators['/']][TYPES['double']]         = -1
semantic_cube[TYPES['boolean']][operators['/']][TYPES['boolean']]        = -1
#4 ==
semantic_cube[TYPES['int']][operators['==']][TYPES['int']]                = TYPES['boolean']
semantic_cube[TYPES['int']][operators['==']][TYPES['double']]             = TYPES['boolean']
semantic_cube[TYPES['int']][operators['==']][TYPES['boolean']]            = TYPES['boolean']
semantic_cube[TYPES['double']][operators['==']][TYPES['int']]             = TYPES['boolean']
semantic_cube[TYPES['double']][operators['==']][TYPES['double']]          = TYPES['boolean']
semantic_cube[TYPES['double']][operators['==']][TYPES['boolean']]         = TYPES['boolean']
semantic_cube[TYPES['boolean']][operators['==']][TYPES['int']]            = TYPES['boolean']
semantic_cube[TYPES['boolean']][operators['==']][TYPES['double']]         = TYPES['boolean']
semantic_cube[TYPES['boolean']][operators['==']][TYPES['boolean']]        = TYPES['boolean']
#5 =
semantic_cube[TYPES['int']][operators['=']][TYPES['int']]                = TYPES['int']
semantic_cube[TYPES['int']][operators['=']][TYPES['double']]             = TYPES['int']
semantic_cube[TYPES['int']][operators['=']][TYPES['boolean']]            = -1
semantic_cube[TYPES['double']][operators['=']][TYPES['int']]             = TYPES['int']
semantic_cube[TYPES['double']][operators['=']][TYPES['double']]          = TYPES['double']
semantic_cube[TYPES['double']][operators['=']][TYPES['boolean']]         = -1
semantic_cube[TYPES['boolean']][operators['=']][TYPES['int']]            = -1
semantic_cube[TYPES['boolean']][operators['=']][TYPES['double']]         = -1
semantic_cube[TYPES['boolean']][operators['=']][TYPES['boolean']]        = TYPES['boolean']
#6 <
semantic_cube[TYPES['int']][operators['<']][TYPES['int']]                  = TYPES['boolean']
semantic_cube[TYPES['int']][operators['<']][TYPES['double']]               = TYPES['boolean']
semantic_cube[TYPES['int']][operators['<']][TYPES['boolean']]              = TYPES['boolean']
semantic_cube[TYPES['double']][operators['<']][TYPES['int']]               = TYPES['boolean']
semantic_cube[TYPES['double']][operators['<']][TYPES['double']]            = TYPES['boolean']
semantic_cube[TYPES['double']][operators['<']][TYPES['boolean']]           = TYPES['boolean']
semantic_cube[TYPES['boolean']][operators['<']][TYPES['int']]              = TYPES['boolean']
semantic_cube[TYPES['boolean']][operators['<']][TYPES['double']]           = TYPES['boolean']
semantic_cube[TYPES['boolean']][operators['<']][TYPES['boolean']]          = TYPES['boolean']
#7 >
semantic_cube[TYPES['int']][operators['>']][TYPES['int']]               = TYPES['boolean']
semantic_cube[TYPES['int']][operators['>']][TYPES['double']]            = TYPES['boolean']
semantic_cube[TYPES['int']][operators['>']][TYPES['boolean']]           = TYPES['boolean']
semantic_cube[TYPES['double']][operators['>']][TYPES['int']]            = TYPES['boolean']
semantic_cube[TYPES['double']][operators['>']][TYPES['double']]         = TYPES['boolean']
semantic_cube[TYPES['double']][operators['>']][TYPES['boolean']]        = TYPES['boolean']
semantic_cube[TYPES['boolean']][operators['>']][TYPES['int']]           = TYPES['boolean']
semantic_cube[TYPES['boolean']][operators['>']][TYPES['double']]        = TYPES['boolean']
semantic_cube[TYPES['boolean']][operators['>']][TYPES['boolean']]       = TYPES['boolean']
#8 &
semantic_cube[TYPES['int']][operators['&']][TYPES['int']]                   = TYPES['boolean']
semantic_cube[TYPES['int']][operators['&']][TYPES['double']]                = TYPES['boolean']
semantic_cube[TYPES['int']][operators['&']][TYPES['boolean']]               = TYPES['boolean']
semantic_cube[TYPES['double']][operators['&']][TYPES['int']]                = TYPES['boolean']
semantic_cube[TYPES['double']][operators['&']][TYPES['double']]             = TYPES['boolean']
semantic_cube[TYPES['double']][operators['&']][TYPES['boolean']]            = TYPES['boolean']
semantic_cube[TYPES['boolean']][operators['&']][TYPES['int']]               = TYPES['boolean']
semantic_cube[TYPES['boolean']][operators['&']][TYPES['double']]            = TYPES['boolean']
semantic_cube[TYPES['boolean']][operators['&']][TYPES['boolean']]           = TYPES['boolean']
#9 |
semantic_cube[TYPES['int']][operators['|']][TYPES['int']]                    = TYPES['boolean']
semantic_cube[TYPES['int']][operators['|']][TYPES['double']]                 = TYPES['boolean']
semantic_cube[TYPES['int']][operators['|']][TYPES['boolean']]                = TYPES['boolean']
semantic_cube[TYPES['double']][operators['|']][TYPES['int']]                 = TYPES['boolean']
semantic_cube[TYPES['double']][operators['|']][TYPES['double']]              = TYPES['boolean']
semantic_cube[TYPES['double']][operators['|']][TYPES['boolean']]             = TYPES['boolean']
semantic_cube[TYPES['boolean']][operators['|']][TYPES['int']]                = TYPES['boolean']
semantic_cube[TYPES['boolean']][operators['|']][TYPES['double']]             = TYPES['boolean']
semantic_cube[TYPES['boolean']][operators['|']][TYPES['boolean']]            = TYPES['boolean']
