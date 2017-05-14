import mlpparser
import multipparser
import sys

class PDDL_Parser:
    def __init__(self):
        # actions
        self.parameters = []
        self.positive_preconditions = []
        self.negative_preconditions = []
        self.add_effects = []
        self.del_effects = []

        #problems
        self.problem_name = 'unknown'
        self.objects = []
        self.state = []
        self.positive_goals = []
        self.negative_goals = []



class Propositional_Planner:

    #-----------------------------------------------
    # Solve
    #-----------------------------------------------
    def getDomainActionsFormated(self,planning_domain):
        act = planning_domain.getPDDLDomainActions()
        for single_action in act:
            print (single_action)

    def solve(self, planning):
        # Parsed data
        actions = self.getDomainActionsFormated(planning)
        # state = parser.state
        # goal_pos = parser.positive_goals
        # goal_not = parser.negative_goals

        # # Do nothing
        # if self.applicable(state, goal_pos, goal_not):
        #     return []
        # # Search
        # visited = [state]
        # fringe = [state, None]
        # while fringe:
        #     state = fringe.pop(0)
        #     plan = fringe.pop(0)
        #     for act in actions:
        #         if self.applicable(state, act.positive_preconditions, act.negative_preconditions):
        #             new_state = self.apply(state, act.add_effects, act.del_effects)
        #             if new_state not in visited:
        #                 if self.applicable(new_state, goal_pos, goal_not):
        #                     full_plan = [act]
        #                     while plan:
        #                         act, plan = plan
        #                         full_plan.insert(0, act)
        #                     return full_plan
        #                 visited.append(new_state)
        #                 fringe.append(new_state)
        #                 fringe.append((act, plan))
        # return None

    #-----------------------------------------------
    # Applicable
    #-----------------------------------------------

    def applicable(self, state, positive, negative):
        for i in positive:
            if i not in state:
                return False
        for i in negative:
            if i in state:
                return False
        return True

    #-----------------------------------------------
    # Apply
    #-----------------------------------------------

    def apply(self, state, positive, negative):
        new_state = []
        for i in state:
            if i not in negative:
                new_state.append(i)
        for i in positive:
            if i not in new_state:
              new_state.append(i)
        return new_state




def runPlanner():

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
            print(domain)
            # print(problem)
            planning.setPDDL(domain, problem)
            
            planner = Propositional_Planner()
            plan = planner.solve(planning)

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


planning = mlpparser.mlpParser()
runPlanner()
# ==========================================
# Main
# ==========================================
# if __name__ == '__main__':
#     import sys
#     domain = sys.argv[1]
#     problem = sys.argv[2]
#     planner = Propositional_Planner()
#     plan = planner.solve(domain, problem)
#     if plan:
#         print('plan:')
#         for act in plan:
#             print(act)
#     else:
#         print('No plan was found')