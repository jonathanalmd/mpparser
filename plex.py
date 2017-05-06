# ----------------------------------------------------------------------
# clex.py
#
# A lexer for ANSI C.
# ----------------------------------------------------------------------

import sys
# sys.path.insert(0, "../..")

import lex

# Reserved words

reserved = [
    'DEFINE', 'DOMAIN', 'REQUIREMENTS', 'TYPES', 'CONSTANTS',
    'PREDICATES', 'FUNCTIONS', 'ACTION', 'PARAMETERS', 'PRECONDITION', 'EFFECT',
    'FORALL', 'EXISTS', 'INCREASE', 'DECREASE', 'ASSIGN', 'IMPLY', 'PREFERENCE', 'WHEN',
    'AGENT', 'PROBLEM', 'OBJECTS', 'INIT', 'GOAL', 'CONDITION', 'INITIAL', 'STATE', 'ACTIONS', 'PRECONDITIONS',
    'PRECOND','INITS', 'AND', 'NOT', 'OPERATOR'
]

tokens = reserved + [
    # Literals (identifier, integer constant, float constant, string constant,
    # char const)
    'ID', 'TYPEID', 'ICONST', 'FCONST', 'SCONST', 'CCONST', 'NUM',

    # Operators (+,-,*,/,%,|,&,~,^,<<,>>, ||, &&, !, <, <=, >, >=, ==, !=)
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MOD',
    'OR', 'XOR', 'LSHIFT', 'RSHIFT',
    'LOR', 'LAND', 'LNOT', 
    'LT', 'LE', 'GT', 'GE', 'EQ', 'NE',

    # Assignment (=, *=, /=, %=, +=, -=, <<=, >>=, &=, ^=, |=)
    'EQUALS', 'TIMESEQUAL', 'DIVEQUAL', 'MODEQUAL', 'PLUSEQUAL', 'MINUSEQUAL',
    'LSHIFTEQUAL', 'RSHIFTEQUAL', 'ANDEQUAL', 'XOREQUAL', 'OREQUAL',

    # Increment/decrement (++,--)
    'PLUSPLUS', 'MINUSMINUS',

    # Conditional operator (?)
    'VAR',

    # Delimeters ( ) [ ] { } , . ; :
    'LPAREN', 'RPAREN',
    'LBRACKET', 'RBRACKET',
    'LBRACE', 'RBRACE',
    'COMMA', 'PERIOD', 'SEMI', 'COLON',

    # Ellipsis (...)
    'ELLIPSIS',

    'COMP', 'ARROW'
]

# Completely ignored characters
t_ignore = ' \t\x0c\r'
# Newlines


def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")



# Operators
t_PLUS = r'\+'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MOD = r'%'
t_OR = r'\|'
t_AND = r'&'
# t_NOT = r''
t_XOR = r'\^'
t_LSHIFT = r'<<'
t_RSHIFT = r'>>'
t_LOR = r'\|\|'
t_LAND = r'&&'
t_LNOT = r'!'
t_LT = r'<'
t_GT = r'>'
t_LE = r'<='
t_GE = r'>='
t_EQ = r'=='
t_NE = r'!='

# Assignment operators

# t_EQUALS = r'='
t_COMP = r'='
t_TIMESEQUAL = r'\*='
t_DIVEQUAL = r'/='
t_MODEQUAL = r'%='
t_PLUSEQUAL = r'\+='
t_MINUSEQUAL = r'-='
t_LSHIFTEQUAL = r'<<='
t_RSHIFTEQUAL = r'>>='
t_ANDEQUAL = r'&='
t_OREQUAL = r'\|='
t_XOREQUAL = r'\^='

# Increment/decrement
t_PLUSPLUS = r'\+\+'
t_MINUSMINUS = r'--'

# ->
t_ARROW = r'->'

# ?
t_VAR = r'\?'

# Delimeters
t_MINUS = r'\-'

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMMA = r','
t_PERIOD = r'\.'
t_SEMI = r';'
t_COLON = r':'
t_ELLIPSIS = r'\.\.\.'

# Identifiers and reserved words

reserved_map = {}
for r in reserved:
    reserved_map[r.lower()] = r

# print (reserved_map)


# t_ID = r'[A-Za-z_][\w_]*'
def t_ID(t):
    # r'[A-Za-z_][\w_]*'
    # t.type = reserved_map.get(t.value, "ID")
    # return t
    r'[a-zA-Z_][a-zA-Z0-9_-]*'

    if t.value.upper() in tokens:
        t.type = t.value.upper()
    # else:
    #     lista_predicados.append(t.value) #saving IDS
    return t

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)    
    return t


# def t_OPERATOR(t):
#     r'='
#     # if t.value == "=":
#     #     t.type = "COMP"
#     # elif t.value in ["=","not","NOT"]:
#     #     t.type = t.value.upper()
#     if t.value in ["=","not","NOT"]:
#         t.type = "OPERATOR"
        
#     return t

# Integer literal
t_ICONST = r'\d+([uU]|[lL]|[uU][lL]|[lL][uU])?'

# Floating literal
t_FCONST = r'((\d+)(\.\d+)(e(\+|-)?(\d+))? | (\d+)e(\+|-)?(\d+))([lL]|[fF])?'

# String literal
t_SCONST = r'\"([^\\\n]|(\\.))*?\"'

# Character constant 'c' or L'c'
t_CCONST = r'(L)?\'([^\\\n]|(\\.))*?\''

# Comments


def t_comment(t):
    r'\s*;.*'
    # r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

# Preprocessor directive (ignored)


def t_preprocessor(t):
    r'\#(.)*?\n'
    t.lexer.lineno += 1


def t_error(t):
    print("Illegal character %s" % repr(t.value[0]))
    lexer_error = 1
    t.lexer.skip(1)

lexer = lex.lex()
lexer_error = 0
lista_predicados = []
lista_types = []


if __name__ == "__main__":
    lex.runmain(lexer)
