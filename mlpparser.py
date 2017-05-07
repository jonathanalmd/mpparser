# An implementation of Dartmouth BASIC (1964)
#

import sys
import plex
import multipparser
# import pddldomain

# If a filename has been specified, we try to run it.
# If a runtime error occurs, we bail out and enter
# interactive mode below


if len(sys.argv) > 2:
    run_parser = True
    in_type = sys.argv[1].split(".")
    if in_type[-1] not in ["pddl","PDDL"]:
        print("Invalid input for PDDL DOMAIN formalization")
        print("Correct use: python mlpparser.py input.{strips,adl} or python mlpparser.py domain.pddl problem.pddl")
        run_parser = False
    in_type = sys.argv[2].split(".")
    if in_type[-1] not in ["pddl","PDDL"]:
        print("Invalid input for PDDL PROBLEM formalization")
        print("Correct use: python mlpparser.py input.{strips,adl} or python mlpparser.py domain.pddl problem.pddl")
        run_parser = False
    if run_parser:
        pmode = "pddl"
        run = multipparser.parse(pmode,[sys.argv[1], sys.argv[2]])
        if run:
            print("Formalizacao %s sintaticamente correta!"%(sys.argv[1]))
    else:
        sys.exit()

elif len(sys.argv) == 2:
    in_type = sys.argv[1].split(".")
    pmode = in_type[-1]

    if pmode not in ["adl","strips","ADL","STRIPS"]:
        print(">Invalid input file:",sys.argv[1])
        print("Correct use: python mlpparser.py input.{strips,adl} or python mlpparser.py domain.pddl problem.pddl")
        sys.exit()
    else:
        prog = multipparser.parse(pmode, [sys.argv[1]])
        if prog:
            print("Formalizacao %s sintaticamente correta!"%(sys.argv[1]))


            