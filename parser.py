# Yacc example

import ply.ply.yacc as yacc
from functions_table import *

# Get the token map from the lexer.  This is required.
from lexico import tokens

#program logic
def p_program(p):
    'program : PROGRAM ID SEMICOLON  global_declaration function_declaration main END SEMICOLON'

#main logic
def p_main(p):
    'main : MAIN main_declared LBRACE statute RBRACE'
    FUNCTIONS['main'].setVarTable(LOCALS);
    LOCALS.clear();
    FUNCS_STACK.pop();
#main declared. Used to know when the main has been declared
def p_main_declared(p):
    'main_declared :'
    FUNCTIONS['main'] = Function();
    FUNCS_STACK.append('main');

#global_declaration
def p_global_declaration(p):
    '''global_declaration :       declaration_statute  global_declaration
                                |  empty'''

#declaration
def p_declaration_statute(p):
    '''declaration_statute :      INT int_declaration SEMICOLON
                                | DOUBLE double_declaration SEMICOLON
                                | BOOLEAN boolean_declaration SEMICOLON'''


#int declaration
def p_int_declaration(p):
    'int_declaration :   ID array int_assignation'
    #global definition added to var_table
    if (GLOBAL.has_key(p[1])):
        error('variable ' + p[1] +' already defined on global scope',p.lineno(1));
    if not FUNCS_STACK:
        GLOBAL[p[1]] = Variable(0, TYPES["int"]);
    else:
        if (LOCALS.has_key(p[1])):
            error('variable ' + p[1] +' already defined on local scope',p.lineno(1));
        LOCALS[p[1]] = Variable(0, TYPES["int"]);


#double declaration
def p_double_declaration(p):
    'double_declaration :   ID array double_assignation'
    #global definition added to var_table
    if (GLOBAL.has_key(p[1])):
        error('variable ' + p[1] +' already defined on global scope',p.lineno(1));
    if not FUNCS_STACK:
        GLOBAL[p[1]] = Variable(0, TYPES["double"]);
    else:
        if (LOCALS.has_key(p[1])):
            error('variable ' + p[1] +' already defined on local scope',p.lineno(1));
        LOCALS[p[1]] = Variable(0, TYPES["double"]);

#boolean declaration
def p_boolean_declaration(p):
    'boolean_declaration :   ID array boolean_assignation'
    #global definition added to var_table
    if (GLOBAL.has_key(p[1])):
        error('variable ' + p[1] +' already defined on global scope',p.lineno(1));
    if not FUNCS_STACK:
        GLOBAL[p[1]] = Variable(0, TYPES["boolean"]);
    else:
        if (LOCALS.has_key(p[1])):
            error('variable ' + p[1] +' already defined on local scope',p.lineno(1));
        LOCALS[p[1]] = Variable(0, TYPES["boolean"]);


#main declaration
#def p_main_declaration(p):
#    'main_declaration : ID array '

#possible array declaration
def p_array(p):
    '''array :        LBRACKET CONST_INT RBRACKET array_mult
                    | empty'''

#possible array declaration multiple dimensions
def p_array_mult(p):
    '''array_mult :  array'''

#possible array use
def p_array_u(p):
    '''array_u :      LBRACKET expression RBRACKET array_mult_u
                    | empty'''

#possible array use multiple dimensions
def p_array_mult_u(p):
    '''array_mult_u :  array_u'''

#possible function use
def p_function(p):
    '''function :         LPAREN params RPAREN
                        | array_u'''
    # using a function
    if p[1] == '(':
        #checks functions exists
        if not FUNCTIONS.has_key( p[-1] ):
            error('function ' + p[-1] + ' not declared');
    #checks var exists
    else :
        if not GLOBAL.has_key( p[-1] ) and ( not FUNCS_STACK or not LOCALS.has_key( p[-1] ) ):
            error('var '+ p[-1] +' not defined');


#params to be used on function call
def p_params(p):
    '''params :       expression mult_params
                    | empty'''


#multiple params to be used on function call
def p_mult_params(p):
    '''mult_params :      COMMA params
                        | empty'''

#assignation of a int variable
def p_int_assignation(p):
    '''int_assignation :      ASSIGN expression
                            | empty'''

#assignation of a double variable
def p_double_assignation(p):
    '''double_assignation :   ASSIGN expression
                            | empty'''


#assignation of a boolean variable
def p_boolean_assignation(p):
    '''boolean_assignation :  ASSIGN expression
                            | empty'''

#unknown variable assignation
def p_assignation_statute(p):
    '''assignation_statute : ID array_u ASSIGN expression SEMICOLON'''
    #var verification
    if not GLOBAL.has_key( p[1] ) and ( not FUNCS_STACK or not LOCALS.has_key( p[1] ) ):
        error('var '+p[1]+' not defined');


#expression
def p_expression(p):
    '''expression :     logical'''

#logic
def p_logical(p):
    '''logical :      relational logical_main'''

#used to check multiple logical
def p_logical_main(p):
    '''logical_main :     AND logical
                        | OR logical
                        | empty'''

#relational
def p_relational(p):
    '''relational :   sum relational_main'''

#used to check multiple relations
def p_relational_main(p):
    '''relational_main :      EQUALS relational
                            | LESS relational
                            | GREATER relational
                            | empty'''


#sum
def p_sum(p):
    '''sum :      mult sum_main'''

#used to check multiple sums
def p_sum_main(p):
    '''sum_main :     PLUS sum
                    | MINUS sum
                    | empty'''

#multiplication
def p_mult(p):
    '''mult :         term mult_main'''

#used to check multiple multiplications
def p_mult_main(p):
    '''mult_main :        MULT mult
                        | DIVIDE mult
                        | empty'''

#atomic element for expression
def p_term(p):
    '''term :         CONST_INT
                    | CONST_DOUBLE
                    | CONST_BOOLEAN
                    | ID function
                    | LPAREN expression RPAREN'''

#function
def p_function_declaration(p):
    '''function_declaration :     function_header function_main
                                | empty'''

#function declaration
def p_function_header(p):
    '''function_header :   FUNCTION type ID function_declared LPAREN params_declaration RPAREN'''

#function declared. Used to know when a function has been declared
def p_function_declared(p):
    '''function_declared :'''
    print(last_type);
    if FUNCTIONS.has_key(p[-1]):
        error('function ' + p[-1] + ' already defined');
    FUNCTIONS[p[-1]] = Function(last_type);# function and return type added
    FUNCS_STACK.append(p[-1]);


#function main
def p_function_main(p):
    '''function_main :   LBRACE  statute return_statute RBRACE function_declaration'''

#params declaration
def p_params_declaration(p):
    '''params_declaration :       param_declaration
                                | empty'''

#param section
def p_param_declaration(p):
    '''param_declaration :       type ID param_declared mult_params_declaration'''

#param declared. Used to know when a param has been declared
def p_param_declared(p):
    '''param_declared :'''
    if (LOCALS.has_key(p[-1])):
        error('variable ' + p[-1] +' already defined on local scope',p.lineno(-1));
    LOCALS[p[-1]] = Variable([0], last_type);
    FUNCTIONS[FUNCS_STACK[-1]].addParam();

#multiples params
def p_mult_params_declaration(p):
    '''mult_params_declaration :      COMMA param_declaration
                                    | empty'''


#different types
def p_type(p):
    '''type :     DOUBLE
                | INT
                | BOOLEAN'''
    last_type = TYPES[p[1]];


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
    '''if_statute :       IF LPAREN expression RPAREN LBRACE statute RBRACE else'''

#else
def p_else(p):
    '''else :     ELSE LBRACE statute RBRACE
                | empty'''


#while
def p_while_statute(p):
    '''while_statute :      WHILE LPAREN expression RPAREN LBRACE statute RBRACE '''

#do while statute
def p_do_while(p):
    '''do_while_statute :   DO LBRACE statute RBRACE WHILE LPAREN expression RPAREN'''

#return statement
def p_return_statute(p):
    '''return_statute :   RETURN expression SEMICOLON'''
    FUNCTIONS[FUNCS_STACK [- 1]].setVarTable(LOCALS);#locals added to funct table
    LOCALS.clear();
    FUNCS_STACK.pop();

#function statute
def p_function_statute(p):
    '''function_statute :   ID LPAREN params RPAREN SEMICOLON'''

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

file = open("parser_test2.txt", "r")
parser.parse( file.read() )

#print(FUNCTIONS['b'].getReturnType());
