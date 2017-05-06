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
    pmode = "pddl"
    run = multipparser.parse(pmode,[sys.argv[1], sys.argv[2]])
    if run:
        print("Formalizacao %s sintaticamente correta!"%(sys.argv[1]))

elif len(sys.argv) == 2:
    pmode = "stripsadl"
    prog = multipparser.parse(pmode, [sys.argv[1]])
    if prog:
        print("Formalizacao %s sintaticamente correta!"%(sys.argv[1]))