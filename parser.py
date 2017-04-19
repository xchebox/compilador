# Yacc example

import ply.ply.yacc as yacc
from semantic_cube import TYPES, semantic_cube
from operators import operators
from functions_table import *
from stacks import *
#from memory import MemoryManager
from quadruple import QuadrupleManager


#generates new function table
functionTable = FunctionTable()

#QuadrupleManager
quadrupleManager = QuadrupleManager()

#MemoryManager
#memoryManager = MemoryManager()

#checs if on global scope
def onGlobalScope():
    return not fStack



def printSummary():
    for f in functionTable.getFunctionTable():
        print ("function: %s has %s parameters and return type is %s. It starts on %s quadruple" % (f, len(functionTable.getFunctionTable()[f].getParams()), TYPES.keys()[TYPES.values().index(functionTable.getFunctionTable()[f].getReturnType())], functionTable.getFunctionTable()[f].getFirstQuadruple()))
        print('\n')
        print('requires :\n')
        print('%s ints\n%s doubles\n%s booleans\n'%(functionTable.getFunctionTable()[f].getIntMemoryRequired(), functionTable.getFunctionTable()[f].getDoubleMemoryRequired(), functionTable.getFunctionTable()[f].getBooleanMemoryRequired()))
        print ("the variables are :")
        print('\n')
        for v in functionTable.getFunctionTable()[f].getVarTable().table:
            print( "var %s is %s and memory %s and size of %s" % (v, TYPES.keys()[TYPES.values().index(functionTable.getFunctionTable()[f].getVarTable().table[v].getType())], functionTable.getFunctionTable()[f].getVarTable().table[v].getMemory(), functionTable.getFunctionTable()[f].getVarTable().table[v].getTotalMemoryDimension()))
            print('\n')
        print('\n')

def writeSummary():
    summary = open("./out/summary.txt", "w")
    for f in functionTable.getFunctionTable():
        summary.write ("function: %s has %s parameters and return type is %s. It starts on %s quadruple" % (f, len(functionTable.getFunctionTable()[f].getParams()), TYPES.keys()[TYPES.values().index(functionTable.getFunctionTable()[f].getReturnType())], functionTable.getFunctionTable()[f].getFirstQuadruple()))
        summary.write('\n')
        summary.write('requires :\n')
        summary.write('%s ints\n%s doubles\n%s booleans\n'%(functionTable.getFunctionTable()[f].getIntMemoryRequired(), functionTable.getFunctionTable()[f].getDoubleMemoryRequired(), functionTable.getFunctionTable()[f].getBooleanMemoryRequired()))
        summary.write ("the variables are :")
        summary.write('\n')
        for v in functionTable.getFunctionTable()[f].getVarTable().table:
            summary.write( "var %s is %s and memory %s and size of %s" % (v, TYPES.keys()[TYPES.values().index(functionTable.getFunctionTable()[f].getVarTable().table[v].getType())], functionTable.getFunctionTable()[f].getVarTable().table[v].getMemory(), functionTable.getFunctionTable()[f].getVarTable().table[v].getTotalMemoryDimension()))
            summary.write('\n')
        summary.write('\n')

def writeQuadruples():
    quadruple = open("./out/quadruple.cp", "w")
    for q in quadrupleManager.quadrupleStack:
        quadruple.write ("%s %s %s %s\n" % (q.operator, q.firstOperand, q.secondOperand, q.result))

def printQuadruples():
    print "Quadruples"

    for q in quadrupleManager.quadrupleStack:
        print "%s-- %s %s %s %s" % (quadrupleManager.quadrupleStack.index(q), operators.keys()[operators.values().index(q.operator)], q.firstOperand, q.secondOperand, q.result)

    for q in quadrupleManager.quadrupleStack:
        print ' '




#checks if function exists
def functionExists(key):
    return functionTable.exists(key)

# checks if var exists on function
def varExistsOnFunction(var, function):
    return functionTable.getFunction(function).hasVariable(var)

#get last variable on stack declared from a function table
def getLastVariableDeclaredFromFunction(function):
    return functionTable.getFunction(function).getVariable(getLastVariable())

#get last variable declared on stack from last function declared on stack
def getLastVariableDeclaredFromLastFunction():
    return functionTable.getFunction(getLastFunction()).getVariable(getLastVariable())

#add variabe to var table on function
def addVariableToFunction(variable, function):
    functionTable.getFunction(function).addVariable(variable)

#add variabe to var table on function
def addVariableToLastFunction(variable):
    functionTable.getFunction(getLastFunction()).addVariable(variable)

#get a variable from a var table of a function
def getVariableFromFunction(variable, function):
    return functionTable.getFunction(function).getVariable(variable)

def generateGoToMain():
    quadrupleManager.addQuadruple(operators['goto'], ' ', ' ', JUMP_SPACE)#TODO decide what to do with goto operator code

#used to generates quadruple. A common function used by the different operators
def generateOperatorNextQuadruple(operator):
    global temporalCounter
    if isSameOrder(operator):#last operator in stack is a mult
        if not getPenultimateType() is None:
            resultType = semantic_cube[getLastType()][lookOperatorStack()][getPenultimateType()]
            if  resultType != -1 : #can do operator
                result = quadrupleManager.addQuadruple(lookOperatorStack(), getPenultimateOperand(), getLastOperand(), 't'+`temporalCounter`)
                temporalCounter += 1
                #remove last operator
                operatorsStack.pop()
                #remove operands used
                operandsStack.pop()
                operandsStack.pop()#TODO change to pop and not looknext
                #remove types used
                typesStack.pop()
                typesStack.pop()
                #add result to stack
                operandsStack.append(result)
                #add result type to stack
                typesStack.append(resultType)

                if not onGlobalScope():
                    if getLastType() == TYPES['int']:
                        functionTable.getFunction(getLastFunction()).increaseIntMemoryRequired(1)#result always increments one by one
                    elif getLastType() == TYPES['double']:
                        functionTable.getFunction(getLastFunction()).increaseDoubleMemoryRequired(1)#result always increments one by one
                    elif getLastType() == TYPES['boolean']:
                        functionTable.getFunction(getLastFunction()).increaseBooleanMemoryRequired(1)#result always increments one by one
                    return 1

                else: # on global scope
                    if getLastType() == TYPES['int']:
                        functionTable.getFunction('global').increaseIntMemoryRequired(1)#result always increments one by one
                    elif getLastType() == TYPES['double']:
                        functionTable.getFunction('global').increaseDoubleMemoryRequired(1)#result always increments one by one
                    elif getLastType() == TYPES['boolean']:
                        functionTable.getFunction('global').increaseBooleanMemoryRequired(1)#result always increments one by one
                    return 1
            else :
                return 0
    return -1

#generates an assignation quadruple. Var is the variable that is going to be assigned
def generateAsignationNextQuadruple(var, varType):
    resultType = semantic_cube[typesStack.pop()][operators['=']][varType]
    if  resultType != -1 : #can do operator
        quadrupleManager.addQuadruple(operators['='], operandsStack.pop(), ' ', var)
        return 1
    else :
        return 0

    return -1

#generates gotof quadruple
def generateGotoFQuadruple():
    quadrupleManager.addQuadruple(operators['gotoF'], operandsStack.pop(), ' ', JUMP_SPACE)#TODO decide what to do with goto operator code
    jumpStack.append(quadrupleManager.getCounter() - 1)#adds position to jumpStack

#generates goto quadruple
def generateGotoQuadruple():
    quadrupleManager.addQuadruple(operators['goto'], ' ', ' ', JUMP_SPACE)#TODO decide what to do with goto operator code
    quadrupleManager.fillQuadrupleJump(jumpStack.pop(), quadrupleManager.getCounter())
    jumpStack.append(quadrupleManager.getCounter() - 1)#adds position to jumpStack

#generates goto while quadruple
def generateWhileGotoQuadruple():
    jumptToFalse = jumpStack.pop()
    quadrupleManager.addQuadruple(operators['goto'], ' ', ' ', jumpStack.pop())#TODO decide what to do with goto operator code
    quadrupleManager.fillQuadrupleJump(jumptToFalse, quadrupleManager.getCounter())

#generates gotoT while quadruple
def generateDoWhileGotoTQuadruple():
    quadrupleManager.addQuadruple(operators['gotoT'], operandsStack.pop(), ' ', jumpStack.pop())#TODO decide what to do with goto operator code

#function to generate a new return quadruple
def generateReturnQuadruple():
    quadrupleManager.addQuadruple(operators['return'], ' ', ' ', ' ')

#function to generate ERA quadruple
def generateERAQuadruple(function):
    quadrupleManager.addQuadruple(operators['era'], function, ' ', ' ')

#function to generate ERA quadruple
def generateGoSubQuadruple(function):
    quadrupleManager.addQuadruple(operators['goSub'], function, ' ', functionTable.getFunction(function).getFirstQuadruple())

#function to generate ERA quadruple
def generateParamQuadruple(function, k):
    varName = functionTable.getFunction(function).getParams()[ k - 1] #get the var memory from the parameters stack
    var = getVariableFromFunction(varName, function)
    if typesStack.pop() != var.getType():
        return 0
    else:
        quadrupleManager.addQuadruple(operators['param'], operandsStack.pop(), ' ', varName)#TODO replace for memory
        return 1

# Get the token map from the lexer.  This is required.
from lexico import tokens

#program logic
def p_program(p):
    'program : PROGRAM program_started ID SEMICOLON  global_declaration function_declaration main END SEMICOLON'
    quadrupleManager.addQuadruple(operators['end'],' ',' ',' ')

#used to generate gotoMain quadruple
def p_program_started (p):
    'program_started :      '
    generateGoToMain()

#main logic
def p_main(p):
    'main : MAIN main_declared LBRACE statute RBRACE'
    fStack.pop()#main removed from function stack

#main declared. Used to know when the main has been declared
def p_main_declared(p):
    'main_declared :            '
    functionTable.addFunction('main')#function added to func table
    fStack.append('main');#main added from function stack
    quadrupleManager.fillQuadrupleJump(0, quadrupleManager.getCounter())

#global_declaration
def p_global_declaration(p):
    '''global_declaration :       declaration_statute  global_declaration
                                |  empty'''

#declaration
def p_declaration_statute(p):
    '''declaration_statute :      INT int_declaration int_assignation SEMICOLON
                                | DOUBLE double_declaration double_assignation SEMICOLON
                                | BOOLEAN boolean_declaration boolean_assignation SEMICOLON'''
    vStack.pop(); #when the rule ends the function has already been defined


#int declaration
def p_int_declaration(p):#TODO check if add memory counter to global and main
    'int_declaration :   variable_declared array'
    if onGlobalScope() :
        g = functionTable.getFunction('global')
        getLastVariableDeclaredFromFunction('global').setType(TYPES['int']) #type added
        size = getLastVariableDeclaredFromFunction('global').getTotalMemoryDimension()
        #getLastVariableDeclaredFromFunction('global').setMemory(memoryManager.requestIntMemory(size)) TODO delete this
        getLastVariableDeclaredFromFunction('global').setMemory(g.getIntMemoryRequired())
        g.increaseIntMemoryRequired(size)
    else :
        lastFunction = functionTable.getFunction(getLastFunction())
        getLastVariableDeclaredFromLastFunction().setType(TYPES['int']) #type added
        size = getLastVariableDeclaredFromLastFunction().getTotalMemoryDimension()
        #getLastVariableDeclaredFromLastFunction().setMemory(memoryManager.requestIntMemory(size)) TODO delete this
        getLastVariableDeclaredFromLastFunction().setMemory(lastFunction.getIntMemoryRequired())
        lastFunction.increaseIntMemoryRequired(size)


#double declaration
def p_double_declaration(p):
    'double_declaration :   variable_declared array'
    if onGlobalScope() :
        g = functionTable.getFunction('global')
        getLastVariableDeclaredFromFunction('global').setType(TYPES['double']) #type added
        size = getLastVariableDeclaredFromFunction('global').getTotalMemoryDimension()
        #getLastVariableDeclaredFromFunction('global').setMemory(memoryManager.requestDoubleMemory(size))
        getLastVariableDeclaredFromFunction('global').setMemory(g.getDoubleMemoryRequired())
        g.increaseDoubleMemoryRequired(size)
    else :
        lastFunction = functionTable.getFunction(getLastFunction())
        getLastVariableDeclaredFromLastFunction().setType(TYPES['double']) #type added
        size = getLastVariableDeclaredFromLastFunction().getTotalMemoryDimension()
        getLastVariableDeclaredFromLastFunction().setMemory(lastFunction.getDoubleMemoryRequired())
        lastFunction.increaseDoubleMemoryRequired(size)

#boolean declaration
def p_boolean_declaration(p):
    'boolean_declaration :   variable_declared array'
    if onGlobalScope() :
        g = functionTable.getFunction('global')
        getLastVariableDeclaredFromFunction('global').setType(TYPES['boolean']) #type added
        size = getLastVariableDeclaredFromFunction('global').getTotalMemoryDimension()
        #getLastVariableDeclaredFromFunction('global').setMemory(memoryManager.requestBooleanMemory(size))
        getLastVariableDeclaredFromFunction('global').setMemory(g.getBooleanMemoryRequired())
        g.increaseBooleanMemoryRequired(size)
    else :
        lastFunction = functionTable.getFunction(getLastFunction())
        getLastVariableDeclaredFromLastFunction().setType(TYPES['boolean']) #type added
        size = getLastVariableDeclaredFromLastFunction().getTotalMemoryDimension()
        #getLastVariableDeclaredFromLastFunction().setMemory(memoryManager.requestBooleanMemory(size))
        getLastVariableDeclaredFromLastFunction().setMemory(lastFunction.getBooleanMemoryRequired())
        lastFunction.increaseBooleanMemoryRequired(size)

#variable declared. Extra to know a variable has been declared
def p_variable_declared(p):
    'variable_declared : ID  '
    #global definition added to var_table
    if onGlobalScope(): #empty, -> main
        if varExistsOnFunction(p[1], 'global'):
            error('variable ' + p[1] +' already defined on global scope',p.lineno(1))
        else:
            addVariableToFunction(p[1], 'global')
    else : #function scope
        if varExistsOnFunction(p[1], getLastFunction()):# exists on function var table
            error('variable ' + p[1] +' already defined on function scope',p.lineno(1))
        else:
            addVariableToFunction(p[1], getLastFunction())
    vStack.append(p[1])# added to var stack

#main declaration
#def p_main_declaration(p):
#    'main_declaration : ID array '

#possible array declaration
def p_array(p):
    '''array :      LBRACKET CONST_INT RBRACKET dimension_added array
                    | empty'''


def p_dimension_added(p):
    'dimension_added : '
    if onGlobalScope():#global scope
        getLastVariableDeclaredFromFunction('global').addDimension(p[-2])#dimension added to variable
    else :
        getLastVariableDeclaredFromLastFunction().addDimension(p[-2])#dimension added to variable


#possible array use
def p_array_u(p):
    '''array_u :      LBRACKET array_used expression RBRACKET array_u
                    | empty'''

def p_array_used(p):
    'array_used :     '


#possible function use as expression
def p_function(p):
    '''function :         LPAREN function_called params RPAREN
                        | array_u'''
    if p[1] == '(':
        generateGoSubQuadruple(p[-1])
        functionCalled = functionTable.getFunction(p[-1]) #function called
        typesStack.append(functionCalled.getReturnType())
        operandsStack.append(operandsStack.pop()) #TODO change for memory
        #TODO release memory after return


    else :#if not a function name then you are going to use an var id
        if onGlobalScope() :
            if not varExistsOnFunction(p[-1], 'global'):
                error('var '+p[-1]+' not defined on line', p.lineno(-1))
            else:
                typesStack.append(getVariableFromFunction(p[-1], 'global').getType())
                #operandsStack.append(p[-1])
                operandsStack.append(getVariableFromFunction(p[-1], 'global').getMemory())
        else : #function scope
            if not varExistsOnFunction(p[-1], getLastFunction()):# var not declared on local
                if not varExistsOnFunction(p[-1], 'global'): #var not declared on global
                    error('var '+p[-1]+' not defined on line', p.lineno(-1))
                else : #var used from global scope
                    typesStack.append(getVariableFromFunction(p[-1], 'global').getType())
                    #operandsStack.append(p[-1])
                    operandsStack.append(getVariableFromFunction(p[-1], 'global').getMemory())
            else:#variable used on local scope
                typesStack.append(getVariableFromFunction(p[-1], getLastFunction()).getType())
                #operandsStack.append(p[-1])
                operandsStack.append(getVariableFromFunction(p[-1], getLastFunction()).getMemory())

def p_function_called(p):
    'function_called :  '
    # using a function
    if p[-1] == '(':#function call/reference
        #checks functions exists
        if not functionExists( p[-2] ):
            error('function ' + p[-2] + ' not declared on line', p.lineno(-1))
        else:
            generateERAQuadruple(p[-2])

#params to be used on function call
def p_params(p):
    '''params :       expression param_passed mult_params
                    | empty'''

#used to know when a paramete has been passed to the function call
def p_param_passed(p):
    'param_passed :     '
    k = 1 #TODO check this thing, it works!!!! yeah
    functionName = p[k*(-3) - 1]#TODO delicate. It counts the tokens
    while functionName is None :
        k += 1
        functionName = p[k*(-3)  - 1] #if dont get name then go three space backwards to get id
    paramsNo = len (functionTable.getFunction(functionName).getParams())
    if k  > paramsNo:
        error('function %s needs %s elements, %s given, on line '%(functionName, paramsNo, k),p.lineno(0))

    if generateParamQuadruple(functionName, k)  == 0: #Quadruple generated
        error('Type mismatch on line ', p.lineno(0))



#multiple params to be used on function call
def p_mult_params(p):
    '''mult_params :      COMMA params
                        | empty'''

#assignation of a int variable
def p_int_assignation(p):
    '''int_assignation :      ASSIGN expression
                            | empty'''
    if p[1] == '=':
        if onGlobalScope():
            if generateAsignationNextQuadruple(getVariableFromFunction(getLastVariable(), 'global').getMemory(), TYPES['int']) == 0:
                error("Type mismatch on line", p.lineno(1))
            #TODO change into memory using globla or local scope
        else :
            if generateAsignationNextQuadruple(getLastVariableDeclaredFromLastFunction().getMemory(), TYPES['int']) == 0:
                error("Type mismatch on line", p.lineno(1))

#assignation of a double variable
def p_double_assignation(p):
    '''double_assignation :   ASSIGN expression
                            | empty'''
    if p[1] == '=':
        if onGlobalScope():
            if generateAsignationNextQuadruple(getVariableFromFunction(getLastVariable(), 'global').getMemory(), TYPES['double']) == 0:
                error("Type mismatch on line", p.lineno(1))
            #TODO change into memory using globla or local scope
        else :
            if generateAsignationNextQuadruple(getLastVariableDeclaredFromLastFunction().getMemory(), TYPES['double']) == 0:
                error("Type mismatch on line", p.lineno(1))


#assignation of a boolean variable
def p_boolean_assignation(p):
    '''boolean_assignation :  ASSIGN expression
                            | empty'''
    if p[1] == '=':
        if onGlobalScope():
            generateAsignationNextQuadruple(getVariableFromFunction(getLastVariable(), 'global').getMemory(), TYPES['boolean'])
            #TODO change into memory using globla or local scope
        else :
            generateAsignationNextQuadruple(getLastVariableDeclaredFromLastFunction().getMemory(), TYPES['boolean'])

#unknown variable assignation
def p_assignation_statute(p):
    '''assignation_statute : ID array_u ASSIGN expression SEMICOLON'''
    if onGlobalScope():
        if not varExistsOnFunction(p[1], 'global'):
            error('variable '+p[1]+ ' not declared on line', p.lineno(1))
        else :
            # add info into from global scope
            var = getVariableFromFunction(p[1],'global')
            if generateAsignationNextQuadruple(var.getMemory(), var.getType()) == 0:
                error('Type mismatch on line', p.lineno(1))
    else :
        if not varExistsOnFunction(p[1], getLastFunction()):
            if not varExistsOnFunction(p[1], 'global'):
                error('variable '+p[1]+ ' not declared on line', p.lineno(1))
            else :
                # add info into from global scope
                var = getVariableFromFunction(p[1],'global')
                if generateAsignationNextQuadruple(var.getMemory(), var.getType()) == 0:
                    error('Type mismatch on line', p.lineno(1))
        else :
            # add into info from local scope
            var = getVariableFromFunction(p[1],getLastFunction())
            if generateAsignationNextQuadruple(var.getMemory(), var.getType()) == 0:
                error('Type mismatch on line ', p.lineno(1))




#expression
def p_expression(p):
    '''expression :     clean_expressions logical '''

#used to clear the stack. In theory before a new expression is called the older values are useless
def p_clean_expressions(p):
    'clean_expressions :        '
    del operandsStack[:]#TODO handle this. Is basic just for the return statement
    del typesStack[:]

#logic
def p_logical(p):
    '''logical :      relational logical_after_term logical_main '''

#used to check multiple logical
def p_logical_main(p):
    '''logical_main :     AND logical_used logical
                        | OR logical_used logical
                        | empty'''

#used to know the operator used
def p_logical_used(p):
    'logical_used :      '
    operatorsStack.append(operators[p[-1]])

#used to create quadruple. runs just after term is received
def p_logical_after_term(p):
    'logical_after_term :  '
    if generateOperatorNextQuadruple('&') == 0:
        error('type mismatch on line ',p.lineno(0))

#relational
def p_relational(p):
    '''relational :   sum relational_after_term relational_main'''

#used to check multiple relations
def p_relational_main(p):
    '''relational_main :      EQUALS relational_used relational
                            | LESS relational_used relational
                            | GREATER relational_used relational
                            | empty'''

#used to know the operator used
def p_relational_used(p):
    'relational_used :      '
    operatorsStack.append(operators[p[-1]])

#used to create quadruple. runs just after term is received
def p_relational_after_term(p):
    'relational_after_term :  '
    if generateOperatorNextQuadruple('==') == 0:
        error('type mismatch on line', p.lineno(0))


#sum
def p_sum(p):
    '''sum :      mult sum_after_term sum_main'''

#used to check multiple sums
def p_sum_main(p):
    '''sum_main :     PLUS sum_used sum
                    | MINUS sum_used sum
                    | empty'''

#used to know the operator used
def p_sum_used(p):
    'sum_used :      '
    operatorsStack.append(operators[p[-1]])

#used to create quadruple. runs just after term is received
def p_sum_after_term(p):
    'sum_after_term :  '
    if generateOperatorNextQuadruple('+') == 0:
        error('type mismatch on line', p.lineno(0))

#multiplication
def p_mult(p):
    '''mult :         term mult_after_term mult_main'''

#used to check multiple multiplications
def p_mult_main(p):
    '''mult_main :        MULT mult_used mult
                        | DIVIDE mult_used mult
                        | empty'''

#used to know the operator used
def p_mult_used(p):
    'mult_used :      '
    operatorsStack.append(operators[p[-1]])

#used to create quadruple. runs just after term is received
def p_mult_after_term(p):
    'mult_after_term :  '
    if generateOperatorNextQuadruple('*') == 0:
        error('type mismatch on line ', p.lineno(0))

#atomic element for expression
def p_term(p):
    '''term :         CONST_INT term_int_used
                    | CONST_DOUBLE term_double_used
                    | CONST_BOOLEAN term_boolean_used
                    | ID function
                    | LPAREN term_parenthesis_used logical RPAREN'''
    #remove false bottom
    if p[1] == '(': #TODO check if works properly.... it seems so
        operatorsStack.pop()


#rule to identify the used type
def p_term_int_used(p):
    'term_int_used :     '
    #global temporalCounter
    #operandsStack.append('t'+`temporalCounter`)
    #temporalCounter += 1#TODO remember to change temporal on constants. constants do not generate temmporal

    operandsStack.append(p[-1])
    #type added to stack
    typesStack.append(TYPES['int'])

#rule to identify the used type
def p_term_double_used(p):
    'term_double_used :     '
    #global temporalCounter
    #operandsStack.append('t'+`temporalCounter`)
    #temporalCounter += 1


    operandsStack.append(p[-1])

    #type added to stack
    typesStack.append(TYPES['double'])

#rule to identify the used type
def p_term_boolean_used(p):
    'term_boolean_used :     '
    #global temporalCounter
    #operandsStack.append('t'+`temporalCounter`)
    #temporalCounter += 1

    operandsStack.append(p[-1])
    #type added to stack
    typesStack.append(TYPES['boolean'])

#rule to identify a use of parenthesis
def p_term_parenthesis_used(p):
    'term_parenthesis_used :     '
    #add false bottom
    operatorsStack.append(FALSE_BOTTOM)


#function
def p_function_declaration(p):
    '''function_declaration :     function_header function_main function_declaration
                                | empty'''

#function declaration
def p_function_header(p):
    '''function_header :   FUNCTION  return_type_declared LPAREN params_declaration RPAREN'''

#called after return statement declared
def p_return_type_declared(p):
    '''return_type_declared :    DOUBLE ID  function_declared
                                | INT ID  function_declared
                                | BOOLEAN ID  function_declared'''

#function declared. Used to know when a function has been declared
def p_function_declared(p):
    '''function_declared :'''
    if functionExists(p[-1]):
        error("Function "+p[-1]+" already declared on line ",p.lineno(0))
    else :
        fStack.append(p[-1])#function name added to function stack
        functionTable.addFunction(p[-1])#function added to func table
        functionTable.getFunction(p[-1]).setReturnType(TYPES[p[-2]])#return value added

#function main
def p_function_main(p):
    '''function_main :   LBRACE  function_main_started statute return_statute RBRACE'''
    #function finished



def p_function_main_started(p):
    'function_main_started :        '
    functionTable.getFunction(getLastFunction()).setFirstQuadruple(quadrupleManager.getCounter())


#params declaration
def p_params_declaration(p):
    '''params_declaration :       param_declaration
                                | empty'''

#param section
def p_param_declaration(p):
    '''param_declaration :       INT ID param_declared mult_params_declaration
                                | DOUBLE ID param_declared mult_params_declaration
                                | BOOLEAN ID param_declared mult_params_declaration'''

#param declared. Used to know when a param has been declared
def p_param_declared(p):
    '''param_declared :'''
    lastFunction = functionTable.getFunction(getLastFunction())
    addVariableToLastFunction(p[-1])
    getVariableFromFunction(p[-1], getLastFunction()).setType(TYPES[p[-2]])#type added to var and argument
    size = getVariableFromFunction(p[-1], getLastFunction()).getTotalMemoryDimension()
    #getVariableFromFunction(p[-1], getLastFunction()).setMemory(memoryManager.requestMemoryOfType(size, TYPES[p[-2]]))
    functionTable.getFunction(getLastFunction()).addParam(p[-1]) #param counter added
    if TYPES[p[-2]] == TYPES['int']: # is an integer
        getVariableFromFunction(p[-1], getLastFunction()).setMemory(lastFunction.getIntMemoryRequired())
        lastFunction.increaseIntMemoryRequired(size)
    elif TYPES[p[-2]] == TYPES['double']: # is a double
        getVariableFromFunction(p[-1], getLastFunction()).setMemory(lastFunction.getDoubleMemoryRequired())
        lastFunction.increaseDoubleMemoryRequired(size)
    elif TYPES[p[-2]] == TYPES['boolean']: # is a boolean
        getVariableFromFunction(p[-1], getLastFunction()).setMemory(lastFunction.getBooleanMemoryRequired())
        lastFunction.increaseBooleanMemoryRequired(size)
    else :
        error('internal error')
        #an error occurred

#multiples params
def p_mult_params_declaration(p):
    '''mult_params_declaration :      COMMA param_declaration
                                    | empty'''


#different types
def p_type(p):##############################delete this
    '''type :     DOUBLE
                | INT
                | BOOLEAN'''


#statute
def p_statute(p):
    '''statute :      if_statute statute
                    | while_statute statute
                    | do_while_statute statute
                    | assignation_statute statute
                    | declaration_statute statute
                    | function_statute statute
                    | comment_statute statute
                    | graphic_statute statute
                    | empty'''

#if
def p_if_statute(p):
    '''if_statute :       IF LPAREN expression RPAREN then LBRACE statute RBRACE else'''
    #fills the last jumpStack
    quadrupleManager.fillQuadrupleJump(jumpStack.pop(), quadrupleManager.getCounter())

#then. Means the expression has been resolved/executed
def p_then(p):
    'then :          '
    if typesStack.pop() != TYPES['boolean']:
        error('Semantic error on if statute on line ', p.lineno(0))
    else:
        #actual boolean expression
        generateGotoFQuadruple()


#else
def p_else(p):
    '''else :     ELSE else_then LBRACE statute RBRACE
                | empty'''

#else used
def p_else_then(p):
    'else_then :        '
    generateGotoQuadruple()




#while
def p_while_statute(p):
    '''while_statute :      WHILE while_declared LPAREN expression RPAREN while_then LBRACE statute RBRACE '''
    #fills the last jumpStack
    generateWhileGotoQuadruple()

#when declared and started
def p_when_declared(p):
    'while_declared :           '
    jumpStack.append(quadrupleManager.getCounter())

#after boolean expression
def p_while_then(p):
    'while_then :            '
    if typesStack.pop() != TYPES['boolean']:
        error('Semantic error on while statute on line ',p.lineno(0))
    else :
        generateGotoFQuadruple()



#do while statute
def p_do_while(p):
    '''do_while_statute :   DO do_while_then LBRACE statute RBRACE WHILE LPAREN expression RPAREN'''
    if typesStack.pop() == TYPES['boolean']:
        generateDoWhileGotoTQuadruple()

#do while then
def p_do_while_then(p):
    'do_while_then :        '
    jumpStack.append(quadrupleManager.getCounter())

#return statement
def p_return_statute(p):
    '''return_statute :   RETURN expression SEMICOLON'''
    generateReturnQuadruple()
    #typesStack.pop() TODO dont remember why pop
    addVariableToLastFunction('return')#TODO change to memory
    getVariableFromFunction('return', getLastFunction()).setType(functionTable.getFunction(getLastFunction()).getReturnType())
    fStack.pop()# function defined so we remove it from the stack

#function statute
def p_function_statute(p):
    '''function_statute :   ID LPAREN function_called params RPAREN SEMICOLON'''
    generateGoSubQuadruple(p[1])
#TODO check or delete to join with function called from expression

#comment statute
def p_comment_statute(p):
    '''comment_statute :    COMMENT statute'''


#turtle graphics statutes
def p_graphic_statute(p):
    '''graphic_statute :    pen_up_statute
                            | pen_down_statute
                            | pen_size_statute
                            | pen_color_statute
                            | set_x_statute
                            | set_y_statute
                            | clear_statute
                            | move_on_x_statute
                            | move_on_y_statute
                            | rotate_to_right_statute
                            | rotate_to_left_statute
                            | rectangle_statute
                            | triangle_statute
                            | circle_statute'''

def p_pen_up_statute(p):
    '''pen_up_statute :    PENUP LPAREN RPAREN SEMICOLON'''

def p_pen_down_statute(p):
    '''pen_down_statute :  PENDOWN LPAREN RPAREN SEMICOLON  '''

def p_pen_size_statute(p):
    '''pen_size_statute :  PENSIZE LPAREN expression RPAREN SEMICOLON  '''

def p_pen_color_statute(p):
    '''pen_color_statute :  PENCOLOR LPAREN expression COMMA expression COMMA expression RPAREN SEMICOLON  '''

def p_set_x_statute(p):
    '''set_x_statute :    SETX LPAREN expression RPAREN SEMICOLON'''

def p_set_y_statute(p):
    '''set_y_statute :    SETY LPAREN expression RPAREN SEMICOLON'''

def p_clear_statute(p):
    '''clear_statute :    CLEAR LPAREN RPAREN SEMICOLON '''

def p_move_on_x_statute(p):
    '''move_on_x_statute : MOVEONX LPAREN expression RPAREN SEMICOLON  '''

def p_move_on_y_statute(p):
    '''move_on_y_statute : MOVEONY LPAREN expression RPAREN SEMICOLON '''

def p_rotate_to_right_statute(p):
    '''rotate_to_right_statute : ROTATETORIGHT LPAREN expression RPAREN SEMICOLON '''

def p_rotate_to_left_statute(p):
    '''rotate_to_left_statute : ROTATETOLEFT LPAREN expression RPAREN SEMICOLON '''

#rectangle(width, height)
def p_rectangle_statute(p):
    '''rectangle_statute : RECTANGLE LPAREN expression COMMA expression RPAREN SEMICOLON '''
#triangle(base, height)
def p_triangle_statute(p):
    '''triangle_statute : TRIANGLE LPAREN expression COMMA expression RPAREN SEMICOLON '''
#circle(diameter)
def p_circle_statute(p):
    '''circle_statute : CIRCLE LPAREN expression RPAREN SEMICOLON '''

#error flag
def error(message, line = None):
    if line :
        message += ' on line '+str(line);
    print message;
    raise SyntaxError;

#empty rule
def p_empty(p):
    'empty :'
    pass

# Error rule for syntax errors
def p_error(p):
    print("Syntax error")

# Build the parser
parser = yacc.yacc();
parser.defaulted_states = {};

#test

#file = open("parse_test_cycles.txt", "r")
#file = open("parser_test_function.txt", "r")
file = open("parser_test.txt", "r")
parser.parse( file.read() )

printSummary()
printQuadruples()

writeQuadruples()
