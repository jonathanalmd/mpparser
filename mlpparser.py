# An implementation of Dartmouth BASIC (1964)
#

import sys
import plex
import multipparser
# import pddldomain

# If a filename has been specified, we try to run it.
# If a runtime error occurs, we bail out and enter
# interactive mode below

class mlpParser:
    def __init__(self):
        self.pddlDomain = None
        self.pddlProblem = None
        self.adl = None
        self.strips = None

    def setPDDL(self, domain, problem):
        self.pddlDomain = domain
        self.pddlProblem = problem

    def setSTRIPS(self, strips):
        self.strips = strips

    def setADL(self, adl):
        self.adl = adl

    def __str__(self):
        return "\nPDDL:\nPDDL Domain:" + str(self.pddlDomain) + "\nPDDL Problem:" + str(self.pddlProblem) + "\n\nSTRIPS:" + str(self.strips) + "\n\nADL:" + str(self.adl) + "\n"

    def __repr__(self):
        return "\nPDDL\nPDDL Domain:" + str(self.pddlDomain) + "\nPDDL Problem:" + str(self.pddlProblem) + "\n\nSTRIPS:" + str(self.strips) + "\n\nADL:" + str(self.adl) + "\n"

def runMlp():
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
            domain, problem = multipparser.parse(pmode,[sys.argv[1], sys.argv[2]])
            if domain:
                print("Formalizacao %s sintaticamente correta!"%(sys.argv[1]))
            if problem:
                print("Formalizacao %s sintaticamente correta!"%(sys.argv[2]))
            # print(domain)
            # print(problem)
            planning.setPDDL(domain, problem)

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
            strips_adl = multipparser.parse(pmode, [sys.argv[1]])
            if strips_adl:
                # print(strips_adl)
                print("Formalizacao %s sintaticamente correta!"%(sys.argv[1]))
                in_type = sys.argv[1].split(".")
                if in_type[-1] in ["strips","STRIPS"]:
                    planning.setSTRIPS(strips_adl)
                else: # adl
                    planning.setADL(strips_adl)

planning = mlpParser()
runMlp()
print(planning)


            