from operators import operators

fStack = []
vStack = []
dCounter = 0

operandsStack = [] #operands stack for quadruples
operatorsStack = []#operators stack for quadruples
typesStack = [] #types stack for quadruples

dimensionStack = [] #dimension stack

jumpStack = [] #jump stack

#temporal counter. only for testing purposes
temporalCounter = 1

FALSE_BOTTOM = '?'
JUMP_SPACE = '_'

def lookDimensionStack():
    if len(dimensionStack) == 0:
        return None
    if dimensionStack[ len(dimensionStack) - 1] == FALSE_BOTTOM:
        return None
    return dimensionStack[ len(dimensionStack) - 1]

#function to lookup the last element on operator stack
def lookOperatorStack():
    if len(operatorsStack) == 0:
        return None
    if operatorsStack[ len(operatorsStack) - 1] == FALSE_BOTTOM:
        return None
    return operatorsStack[ len(operatorsStack) - 1]

#checks if the last operator on stack is the given operator
def isLastOperator(operator):
    if lookOperatorStack() is None:
        return False
    return lookOperatorStack() == operators[operator]

#checks if the last operator on stack is in the same order
def isSameOrder(operator):
    if lookOperatorStack() is None:
        return False
    if operator == '+' or operator == '-':
        return isLastOperator('+') or isLastOperator('-')
    if operator == '*' or operator == '/':
        return isLastOperator('*') or isLastOperator('/')
    if operator == '==' or operator == '>' or operator == '<':
        return isLastOperator('==') or isLastOperator('>') or isLastOperator('<')
    if operator == '&' or operator == '|':
        return isLastOperator('&') or isLastOperator('|')
    return None #error. Bad operator given

def getLastOperand():
    if len(operandsStack) < 1:
        return None
    return operandsStack[ len(operandsStack) - 1]

def getPenultimateOperand():
    if len(operandsStack) < 2:
        return None
    return operandsStack[ len(operandsStack) - 2]

def getLastType():
    if len(typesStack) < 1:
        return None
    return typesStack[ len(typesStack) - 1]

def getPenultimateType():
    if len(typesStack) < 2:
        return None
    return typesStack[ len(typesStack) - 2]

def getLastVariable():
    return vStack[len(vStack) - 1]

def getLastFunction():
    return fStack[len(fStack) - 1]
