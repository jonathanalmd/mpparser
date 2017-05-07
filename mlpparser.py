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
        self.pddlDomain = None #class PDDLDomain()
        self.pddlProblem = None #class PDDLProblem()
        self.adl = None # class ADLInfo()
        self.strips = None #class StripsInfo()

    def __str__(self):
        return "\nPDDL:\nPDDL Domain:" + str(self.pddlDomain) + "\nPDDL Problem:" + str(self.pddlProblem) + "\n\nSTRIPS:" + str(self.strips) + "\n\nADL:" + str(self.adl) + "\n"

    def __repr__(self):
        return "\nPDDL\nPDDL Domain:" + str(self.pddlDomain) + "\nPDDL Problem:" + str(self.pddlProblem) + "\n\nSTRIPS:" + str(self.strips) + "\n\nADL:" + str(self.adl) + "\n"

    def setPDDL(self, domain, problem):
        self.pddlDomain = domain
        self.pddlProblem = problem

    def setSTRIPS(self, strips):
        self.strips = strips

    def setADL(self, adl):
        self.adl = adl


    def getPDDL(self):
        return self.pddlDomain, self.pddlProblem 


    def getPDDLDomain(self):
        # PDDLDomain() class (pddldomain.py)
        return self.pddlDomain

    def getPDDLDomainName(self):
        # string
        return self.pddlDomain.getName()

    def getPDDLDomainPredicates(self): 
        # list of PDDLPredicate Class (pddldomain.py)
        # [pred_name {'type':[var1,var2], 'type2':[var1,var2]}, pred_name2 {'type3':[var1,var2]}]
        return self.pddlDomain.getPredicates()

    def getPDDLDomainTypes(self):
        # list of strings
        # [type1, type2, type3]
        return self.pddlDomain.getTypes()

    def getPDDLDomainConstants(self):
        # dictionary
        # {'type' : [constant1, constant2], 'type2' : [constant3]}
        return self.pddlDomain.getConstants()

    def getPDDLDomainFunctions(self):
        # list of PDDLFunction class (pddldomain.py)
        # ['' '' {'':['']}]
        # [string string {string:list of strings}]
        # [function_name function type {'type':[var1,var2]}]
        return self.pddlDomain.getFunctions()

    def getPDDLDomainActions(self):
        # list of PDDLActions class (pddldomain.py)
        # ['' {'':['']} {'':['']} {'':['']}]
        # [string {string:list of strings} {string: list of strings} {string: list of strings}]
        # [action_name {'type':[var1,var2]} {'pred_name':[var1,var2]} {'pred_name':[var1,var2]}]
        return self.pddlDomain.getActions()


    def getPDDLProblem(self):
        # PDDLProblem() class (pddlproblem.py)
        return self.pddlProblem

    def getPDDLProblemName(self):
        # string
        return self.pddlProblem.getName()

    def getPDDLProblemDomain(self):
        # string
        return self.pddlProblem.getProblemDomain()

    def getPDDLProblemObjects(self):
        # dictionary
        # {'type':[var1,var2], 'type2':[var1]}
        return self.pddlProblem.getObjects()

    def getPDDLProblemInit(self):
        # list of PDDLProblemPredicate class (pddlproblem.py)
        # string list of strings
        # pred_name ['var1','var2']
        return self.pddlProblem.getInit()

    def getPDDLProblemGoal(self):
        # list of PDDLProblemPredicate class (pddlproblem.py)
        # string list of strings
        # pred_name ['var1','var2']
        return self.pddlProblem.getGoal()


    def getSTRIPS(self):
        # StripsInfo() class (strips.py)
        return self.strips

    def getSTRIPSInitialState(self):
        # list of strings and lists of strings
        # predicate name1,list of vars from predicate name1, predicate name2, list of vars from predicate name2 ...
        # ['pred_name1',['var1', 'var2'],'pred_name2',['var1']]
        return self.strips.getInitialState()

    def getSTRIPSGoalState(self):
        # list of strings and lists of strings
        # predicate name1,list of vars from predicate name1, predicate name2, list of vars from predicate name2 ...
        # ['pred_name1',['var1', 'var2'],'pred_name2',['var1']]
        return self.strips.getGoalState()

    def getSTRIPSActions(self):
        # list of StripsAction() class (strips.py)
        # [string, list of strings, list of strings and lists of strings, list of strings and lists of strings]
        # [action_name, ['param1','param2'], ['predicate_precondition1',['var1','var2']], ['predicate_effect1',['var1']]]
        return self.strips.getActions()



    def getADL(self):
        # ADLInfo() class (adl.py)
        return self.adl

    def getADLInitialState(self):
        # list of strings and lists of strings
        # predicate name1,list of vars from predicate name1, predicate name2, list of vars from predicate name2 ...
        # ['pred_name1',['var1', 'var2'],'pred_name2',['var1']]
        return self.adl.getInitialState()

    def getADLGoalState(self):
        # list of strings and lists of strings
        # predicate name1,list of vars from predicate name1, predicate name2, list of vars from predicate name2 ...
        # ['pred_name1',['var1', 'var2'],'pred_name2',['var1']]
        return self.adl.getGoalState()

    def getADLActions(self):
        # list of ADLAction() class (adl.py)
        # string {string:list of strings} [predicate name1,list of vars from predicate name1, predicate name2, list of vars from predicate name2]
        # action_name {type : [var1,var2,va3], type2 : [var1,var2]} ['pred_name1',['var1', 'var2'],'pred_name2',['var1']] ['pred_name_effect1',['var1', 'var2'],'pred_name_effect2',['var1']]
        return self.adl.getActions()




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

# print(planning.getPDDLDomainPredicates())

            