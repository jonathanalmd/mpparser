# An implementation of Dartmouth BASIC (1964)
#

import sys
import plex
import multipparser
# import pddldomain

# If a filename has been specified, we try to run it.
# If a runtime error occurs, we bail out and enter
# interactive mode below
if len(sys.argv) == 2:
    data = open(sys.argv[1]).read()
    prog = multipparser.parse(data)
    if prog:
        print("Formalizacao %s sintaticamente correta!"%(sys.argv[1]))
    