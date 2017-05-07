import plex
import sys

run_mode = ""
linestrips = 0

def reportSyntaxError(value):
    if value == "(":
        print("Syntax error in line",plex.lexer.lineno)
        print("\tMissing or more {'(',')'} than expected")
        if run_mode == "pddlproblem":
            print("\t\tOR")
            print("\tUsing more than one predicate inside 'NOT' operator: please apply 'NOT' operator on each predicate individually")
    elif value != "(":
        if run_mode == "strips" and value.upper() == "PRECONDITIONS":
            print("Syntax error in Action formalization line %d"%(linestrips))
            print("\tProbably using more ',' than expected in Action EFFECTS formalization")
        else:
            if run_mode == "strips" and value.upper() == "EFFECT":
                print("Syntax error in Action Formalization line %d"%(plex.lexer.lineno-1))
                print("\tProbably using more ',' than expected in Action PRECONDITIONS formalization")
            else:
                print("Syntax error in %s line %d"%(value,plex.lexer.lineno))
    else:
        print("Syntax error at EOI")
    sys.exit()

