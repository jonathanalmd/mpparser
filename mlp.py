import sys
import plex
import multipparser
import mlpplanner
import re
# import pddldomain

def parse(pinput):
    planning = multipparser.mlpParser()

    if len(pinput) > 1:
        run_parser = True
        in_type = pinput[0].split(".")
        if in_type[-1] not in ["pddl","PDDL"]:
            print("Invalid input for PDDL DOMAIN formalization")
            print("Correct use: python mlpparser.py input.{strips,adl} or python mlpparser.py domain.pddl problem.pddl")
            run_parser = False
        in_type = pinput[1].split(".")
        
        if in_type[-1] not in ["pddl","PDDL"]:
            print("Invalid input for PDDL PROBLEM formalization")
            print("Correct use: python mlpparser.py input.{strips,adl} or python mlpparser.py domain.pddl problem.pddl")
            run_parser = False
        
        if run_parser:
            pmode = "pddl"
            domain, problem = multipparser.parse(pmode,[pinput[0], pinput[1]])
            if domain:
                print("Formalizacao %s sintaticamente correta!"%(pinput[0]))
            if problem:
                print("Formalizacao %s sintaticamente correta!"%(pinput[1]))
            # print(domain)
            # print(problem)
            planning.setPDDL(domain, problem)
        else:
            sys.exit()

    else: # strips ou adl
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

    return planning

def runMlp():
    planning = multipparser.mlpParser()

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
            rmode = "pddl"
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
                    rmode = "strips"
                else: # adl
                    planning.setADL(strips_adl)
                    rmode = "adl"

    return planning,rmode


def main():
    if sys.argv[-1] == "-p": # parser mode
        input_parser = sys.argv[1:-1]
        print (input_parser)
        parsed_data = parse(input_parser)
        print(parsed_data)
        
    else: # planner mode
        parsed_data, rmode = runMlp()

        print(parsed_data)

        planner = mlpplanner.BFSPlanner(rmode)

        # run planner
        plan = planner.solve(parsed_data)
        if plan:
            print('Plan:')
            for act in plan:
                print(act)
        else:
            print('No plan was found')
        # print(planning.getPDDLDomainPredicates())

main()