import plex
import sys
import mlpplanner 

run_mode = ""
linestrips = 0

def reportError(value):
    if value == "(":
        print("Syntax error in line",plex.lexer.lineno-1)
        print("\tMissing or more {'(',')'} than expected")
        # if run_mode == "pddlproblem":
        #     print("\t\tOR")
        #     print("\tUsing more than one predicate inside 'NOT' operator: please apply 'NOT' operator on each predicate individually")
        if run_mode == "pddldomain":
            print("\t\tOR")
            print("\tUsing more than one 'NOT' operator: please apply 'NOT' one time for all negative predicates")
            print("\te.g.: (not(predicate1)) (not(predicate2)) -> (not (predicate1) (predicate2))")
            print("\t\tOR")
            print("\tPredicate after 'NOT' operator: please put all positive predicates first and then the negative predicates")
            print("\te.g.: (predicate1) (predicate2) (predicate3) (not(predicate4)(predicate5))")
            print("\t\tOR")
            print("\tPredicate declared outside 'AND' operator: please insert all predicates inside (and )")
            print("\te.g.: (and(predicate1) (predicate2) (predicate3) (not(predicate4)(predicate5)))")
            # sys.exit()

    else:
        if run_mode == "strips" and value.upper() == "PRECONDITIONS":
            print("Syntax error in Action formalization line %d"%(linestrips))
            print("\tProbably using more ',' than expected in Action EFFECTS formalization")
            # sys.exit()

        elif run_mode == "strips" and value.upper() == "EFFECT":
            print("Syntax error in Action Formalization line %d"%(plex.lexer.lineno-1))
            print("\tProbably using more ',' than expected in Action PRECONDITIONS formalization")
            # sys.exit()

        elif run_mode == "pddldomain":
            if value[0] == "@":
                print("Semantic error in '%s' (definition in/before line %d) in domain definition "%(value[1:],plex.lexer.lineno))
                print("\tUsing type definition without ':typing' requirement")
            elif value[0] == "?":
                print("Semantic error in '%s' (definition in/before line %d) in domain definition "%(value[1:],plex.lexer.lineno))
                print("\tType '%s' is not defined in ':types' definition section"%(value[1:]))
            elif value[0] == "#":
                print("Semantic error in '%s' (definition in/before line %d) in domain definition "%(value[1:],plex.lexer.lineno))
                print("\tPredicate '%s' is not defined in ':predicates' definition section"%(value[1:]))
            elif value[0] == "*":
                print("Semantic error in ':predicates' definition (right before line %d) in domain definition "%(plex.lexer.lineno))
                print("\tPredicate name(s) repetition")
            elif value[0] == ">":
                print("Semantic error in action definition in domain definition ")
                print("\tAction '%s' is duplicated"%(value[1:]))
            elif value[:2] == "t*":
                print("Semantic error in type '%s' definition (in/before line %d) in domain definition "%(value[2:],plex.lexer.lineno))
                print("\tType name(s) redefinition") 
            elif value[:2] == "c*":
                print("Semantic error in ':constants' definition (in/before line %d) in domain definition "%(plex.lexer.lineno))
                print("\tConstant name(s) repetition")
            elif value[:2] == "f*":
                print("Semantic error in ':functions' definition (in/before line %d) in domain definition "%(plex.lexer.lineno))
                print("\tFunction(s) redefinition")
            elif value[:3] == "vp*":
                print("Semantic error in var '%s' definition (in/before line %d) in domain definition "%(value[3:],plex.lexer.lineno))
                print("\tVar name(s) redefinition") 

            elif value.upper() == "CONSTANTS":
                print("Semantic error in '%s' line %d in domain definition "%(value,plex.lexer.lineno))
                print("\tAll constants must be typed")
                print("\t'You must define ':types' in order to use ':constants' definition")
            elif value == "const-typed":
                print("Syntax error in '%s' line %d in domain definition "%(value,plex.lexer.lineno))
                print("\tAll constants must be typed")
            elif value == "const-def":
                print("Syntax error in '%s' line %d in domain definition "%(value,plex.lexer.lineno))
                print("Wrong ':constants' formalization")
            elif value.upper() in ["STRIPS","ADL","TYPING","NEGATIVE-PRECONDITIONS","DISJUNCTIVE-PRECONDITIONS","EQUALITY","EXISTENTIAL-PRECONDITIONS","UNIVERSAL-PRECONDITIONS","QUANTIFIED-PRCONDITIONS","FLUENTS","CONDITIONAL-EFFECTS"]:
                print("Syntax error in '%s' line %d in domain definition "%(value,plex.lexer.lineno))
                print("\tInvalid requirement definition in ':requirements' section")
            else:
                print("Syntax error in '%s' line %d in domain definition "%(value,plex.lexer.lineno))
                print("\tP.S.: predicate after 'NOT' operator: please put all positive predicates first and then the negative predicates")
                print("\te.g.: (predicate1) (predicate2) (predicate3) (not(predicate4)(predicate5))")
                sys.exit()

        elif run_mode == "pddlproblem":
            if value[0] == "?":
                print("Semantic error in '%s' (definition in/before line %d) in problem definition "%(value[1:],plex.lexer.lineno))
                print("\tType '%s' is not defined in ':types' definition"%(value[1:]))
            elif value[0] == "!":
                print("Semantic error in '%s' (definition in/before line %d) in problem definition "%(value[1:],plex.lexer.lineno))
                print("\tNegative predicate '%s' definition without ':negative-preconditions' in domain ':requirements' definition"%(value[1:]))
            elif value[:2] == "o*":
                print("Semantic error in '%s' (definition in/before line %d) in problem definition"%(value[2:],plex.lexer.lineno))
                print("\tObject '%s' redefined'"%(value[1:]))
            elif value[:3] == "ot*":
                print("Semantic error in ':objects' definition (definition in/before line %d) in problem definition"%(plex.lexer.lineno))
                print("\tObjects from different types with the same name")

            elif value[0][0] == "]":
                print("Semantic error in problem domain definition in line %d in problem definition "%(plex.lexer.lineno))
                print("\tDomain name '%s' defined in problem file is not the same defined in domain file ('%s')"%(value[0][1:],value[1] ))
            else:
                print("Syntax error in '%s' line %d in problem definition "%(value,plex.lexer.lineno))
                print("\tP.S.: predicate after 'NOT' operator: please put all positive predicates first and then the negative predicates")
                print("\te.g.: (predicate1) (predicate2) (predicate3) (not(predicate4)(predicate5))")

        else:
            print("Syntax error in '%s' line %d"%(value,plex.lexer.lineno))
    sys.exit()
