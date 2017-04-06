# ------------------------------------------------------------

# ------------------------------------------------------------
import ply.ply.lex as lex

# List of token names.   This is always required

reserved = {
    'program'           : 'PROGRAM',
    'main'              : 'MAIN',
    'end'               : 'END',
    'function'          : 'FUNCTION',
    'return'            : 'RETURN',
    'if'                : 'IF',
    'else'              : 'ELSE',
    'while'             : 'WHILE',
    'do'                : 'DO',
    'int'               : 'INT',
    'double'            : 'DOUBLE',
    'boolean'           : 'BOOLEAN',
    'penUp'             : 'PENUP',
    'penDown'           : 'PENDOWN',
    'penColor'          : 'PENCOLOR',
    'penSize'           : 'PENSIZE',
    'setX'              : 'SETX',
    'setY'              : 'SETY',
    'clear'             : 'CLEAR',
    'moveOnX'           : 'MOVEONX',
    'moveOnY'           : 'MOVEONY',
    'rotateToRight'     : 'ROTATETORIGHT',
    'rotateToLeft'      : 'ROTATETOLEFT',
    'rectangle'         : 'RECTANGLE',
    'triangle'          : 'TRIANGLE',
    'circle'            : 'CIRCLE',
}

tokens = [
    'PLUS',
    'MINUS',
    'MULT',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'LBRACKET',
    'RBRACKET',
    'EQUALS',
    'ASSIGN',
    'LESS',
    'GREATER',
    'SEMICOLON',
    'COMMA',
    'AND',
    'OR',
    'CONST_INT',
    'CONST_DOUBLE',
    'CONST_BOOLEAN',
    'COMMENT',
    'ID'
] + list(reserved.values())

# Regular expression rules for simple tokens
t_PLUS      = r'\+'
t_MINUS     = r'-'
t_MULT      = r'\*'
t_DIVIDE    = r'/'
t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_LBRACE    = r'\{'
t_RBRACE    = r'\}'
t_LBRACKET  = r'\['
t_RBRACKET  = r'\]'
t_EQUALS    = r'=='
t_ASSIGN    = r'='
t_LESS      = r'<'
t_GREATER   = r'>'
t_SEMICOLON = r';'
t_COMMA     = r','
t_AND       = r'&'
t_OR        = r'\|'


# A regular expression rule with some action code
def t_COMMENT(t):
    r'\#.*(\n | $)'
    return t

def t_CONST_DOUBLE(t):
    r'-?\d+\.\d+'
    t.value = float(t.value)
    return t

def t_CONST_INT(t):
    r'-?\d+'
    t.value = int(t.value)
    return t

def t_CONST_BOOLEAN(t):
    r'(True|False)'
    t.value = t.value == 'True'
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t\n'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

#x = input('write something\n')

#lexer.input(x)

# Test it out

#data = 'boolean int double string'
#data = '''1212True'''
#data += ''' 123.12 123 2532a23432432'yolo' '''
#data += '''+ - * / ( ) {} []  == = < > "  : ; & | .'''
#for r in reserved:
#    data += ' ' + r
#data += ''' \'#jkdadjksb[]
#qwewqe\''''

# Give the lexer some input
#lexer.input(data)

# Tokenize
#while True:
#    tok = lexer.token()
#    if not tok:
#        break      # No more input
#    print(tok)
