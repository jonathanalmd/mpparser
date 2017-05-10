import plex
import sys

run_mode = ""
linestrips = 0

def reportSyntaxError(value):
    if value == "(":
        print("Syntax error in line",plex.lexer.lineno-1)
        print("\tMissing or more {'(',')'} than expected")
        # if run_mode == "pddlproblem":
        #     print("\t\tOR")
        #     print("\tUsing more than one predicate inside 'NOT' operator: please apply 'NOT' operator on each predicate individually")
        if run_mode == "pddldomain":
            print("\t\tOR")
            print("\tUing more than one 'NOT' operator: please apply 'NOT' one time for all negative predicates")
            print("\te.g.: (not(predicate1)) (not(predicate2)) -> (not (predicate1) (predicate2))")
            print("\t\tOR")
            print("\tPredicate after 'NOT' operator: please put all positive predicates first and then the negative predicates")
            print("\te.g.: (predicate1) (predicate2) (predicate3) (not(predicate4)(predicate5))")
            print("\t\tOR")
            print("\tPredicate declared outside 'AND' operator: please insert all predicates inside (and )")
            print("\te.g.: (and(predicate1) (predicate2) (predicate3) (not(predicate4)(predicate5)))")
    else:
        if run_mode == "strips" and value.upper() == "PRECONDITIONS":
            print("Syntax error in Action formalization line %d"%(linestrips))
            print("\tProbably using more ',' than expected in Action EFFECTS formalization")
        elif run_mode == "strips" and value.upper() == "EFFECT":
            print("Syntax error in Action Formalization line %d"%(plex.lexer.lineno-1))
            print("\tProbably using more ',' than expected in Action PRECONDITIONS formalization")
        elif run_mode == "pddldomain":
            if value[0] == "@":
                print("Syntax error in '%s' (definition in/before line %d)"%(value[1:],plex.lexer.lineno))
                print("\tUsing type definition without ':typing' requirement")
            elif value[0] == "?":
                print("Syntax error in '%s' (definition in/before line %d)"%(value[1:],plex.lexer.lineno))
                print("\tType '%s' is not defined in ':types' definition"%(value[1:]))
            elif value.upper() == "CONSTANTS":
                print("Syntax error in '%s' line %d"%(value,plex.lexer.lineno))
                print("\tAll constants must be typed")
                print("\t'You must define ':types' in order to use ':constants' definition")
            elif value == "const-typed":
                print("Syntax error in '%s' line %d"%(value,plex.lexer.lineno))
                print("\tAll constants must be typed")
            elif value == "const-def":
                print("Syntax error in '%s' line %d"%(value,plex.lexer.lineno))
                print("Wrong ':constants' formalization")
            elif value.upper() in ["STRIPS","ADL","TYPING","NEGATIVE-PRECONDITIONS","DISJUNCTIVE-PRECONDITIONS","EQUALITY","EXISTENTIAL-PRECONDITIONS","UNIVERSAL-PRECONDITIONS","QUANTIFIED-PRCONDITIONS","FLUENTS","CONDITIONAL-EFFECTS"]:
                print("Syntax error in '%s' line %d"%(value,plex.lexer.lineno))
                print("\tInvalid requirement definition in ':requirements' section")
            else:
                print("Syntax error in '%s' line %d"%(value,plex.lexer.lineno))
                print("\tP.S.: predicate after 'NOT' operator: please put all positive predicates first and then the negative predicates")
                print("\te.g.: (predicate1) (predicate2) (predicate3) (not(predicate4)(predicate5))")
        else:
            print("Syntax error in '%s' line %d"%(value,plex.lexer.lineno))

    sys.exit()

