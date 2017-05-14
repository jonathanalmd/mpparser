import sys
import lex

# Reserved words
reserved = [
    'DEFINE', 'DOMAIN', 'REQUIREMENTS', 'TYPES', 'CONSTANTS',
    'PREDICATES', 'FUNCTIONS', 'ACTION', 'PARAMETERS', 'PRECONDITION', 
    'EFFECT', 'FORALL', 'EXISTS', 'INCREASE', 'DECREASE', 'ASSIGN', 
    'IMPLY', 'PREFERENCE', 'WHEN', 'AGENT', 'PROBLEM', 'OBJECTS', 'INIT', 
    'GOAL', 'CONDITION', 'INITIAL', 'STATE','ACTIONS', 'PRECONDITIONS',
    'PRECOND', 'AND', 'NOT', 'OR'
]
tokens = reserved + [
    'ID', 'NUM', 'MINUS',
    
    'LOR', 'LAND', 'LNOT', 
    'LT', 'LE', 'GT', 'GE', 'EQ', 'NE',

    # Conditional operator (?) -> pddl var
    'VAR',

    # Delimeters ( ) [ ] { } , . ; :
    'LPAREN', 'RPAREN',
    'LBRACKET', 'RBRACKET',
    'COMMA', 'COLON',

    # pddl comp -> '=' 
    'COMP'
]

# Completely ignored characters
t_ignore = ' \t\x0c\r'

# Newlines
def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

# Operators
# t_EQUALS = r'='
t_COMP = r'='
t_LNOT = r'!'

t_LT = r'<'
t_GT = r'>'
t_LE = r'<='
t_GE = r'>='
t_NE = r'!='

# ? (pddl var)
t_VAR = r'\?'

# Delimeters
t_MINUS = r'\-'
t_COLON = r':'
t_COMMA = r','

t_LPAREN = r'\('
t_RPAREN = r'\)'

t_LBRACKET = r'\['
t_RBRACKET = r'\]'

# Identifiers and reserved words
# reserved_map = {}
# for r in reserved:
#     reserved_map[r.lower()] = r
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

def t_comment(t):
    r'\s*;.*'
    t.lexer.lineno += t.value.count('\n')

def t_error(t):
    print("Illegal character %s" % repr(t.value[0]))
    lexer_error = 1
    t.lexer.skip(1)


lexer = lex.lex()
if __name__ == "__main__":
    lex.runmain(lexer)


