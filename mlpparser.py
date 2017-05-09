# An implementation of Dartmouth BASIC (1964)
#

import sys
import plex
import multipparser
import re
# import pddldomain

# If a filename has been specified, we try to run it.
# If a runtime error occurs, we bail out and enter
# interactive mode below

class Action:

    def __init__(self, name, parameters, positive_preconditions, negative_preconditions, add_effects, del_effects, cost = 0):
        self.name = name
        self.parameters = parameters
        self.positive_preconditions = positive_preconditions
        self.negative_preconditions = negative_preconditions
        self.add_effects = add_effects
        self.del_effects = del_effects
        self.cost = cost

    def __str__(self):
        return 'action: ' + self.name + \
        '\n  parameters: ' + str(self.parameters) + \
        '\n  positive_preconditions: ' + str(self.positive_preconditions) + \
        '\n  negative_preconditions: ' + str(self.negative_preconditions) + \
        '\n  add_effects: ' + str(self.add_effects) + \
        '\n  del_effects: ' + str(self.del_effects) + \
        '\n  cost: ' + str(self.cost) + '\n'

    def __eq__(self, other): 
        return self.__dict__ == other.__dict__


class Propositional_Planner:
    def __init__(self):
        self.actions = []
    #-----------------------------------------------
    # Solve
    #-----------------------------------------------
    def getDomainActions(self,planning_domain):
        act = planning_domain.getPDDLDomainActions()
        action = []
        for single_action in act:
            # print (single_action)
            action.append(":action")
            action.append(single_action.name)
            action.append(":parameters")
            action.append(list(single_action.parameters.values()))
            action.append(":precondition")
            action_pred = ['and']
            for precond in single_action.preconditions:
                if "!" in precond.name:
                    aux = []
                    aux.append('not')
                    precond.name = re.sub('[&!]', '', precond.name)
                    aux.append([precond.name])
                    action_pred.append(aux)
                else:
                    precond.name = re.sub('[&!]', '', precond.name)
                    action_pred.append([precond.name])

                if precond.p_vars[0][0] != '(':
                    action.append(precond.p_vars)
            action.append(action_pred)
            action_pred = ['and']
            action.append(":effects")
            for effect in single_action.effects:
                if "!" in effect.name:
                    aux = []
                    aux.append('not')
                    effect.name = re.sub('[&!]', '', effect.name)
                    aux.append([effect.name])
                    action_pred.append(aux)
                else:
                    effect.name = re.sub('[&!]', '', effect.name)
                    action_pred.append([effect.name])

                if effect.p_vars[0][0] != '(':
                    action.append(effect.p_vars)
            action.append(action_pred)
        # print (action)
        return action

    def getDomainActionsFormated(self,planning_domain):
        act = planning_domain.getPDDLDomainActions()
        actions = []
        for single_action in act:
            # print (single_action)
            # action.append(":action")
            aname = single_action.name
            # action.append(":parameters")
            # action.append(list(single_action.parameters.values()))
            parameters = list(single_action.parameters.values())
            # action.append(":precondition")
            negative_preconditions = []
            positive_preconditions = []
            for precond in single_action.preconditions:
                if "!" in precond.name:
                    negative_preconditions.append([re.sub('[&!]', '', precond.name)])
                else:
                    positive_preconditions.append([re.sub('[&!]', '', precond.name)])

            # action.append(":effects")
            add_effects = []
            del_effects = []
            for effect in single_action.effects:
                if "!" in effect.name:
                    del_effects.append([re.sub('[&!]', '', effect.name)])
                else:
                    add_effects.append([re.sub('[&!]', '', effect.name)])


            actions.append(Action(aname, parameters, positive_preconditions, negative_preconditions, add_effects, del_effects))
        # print (action)
        return actions

    def getProblemInit(self,planning_problem):
        init = planning_problem.getPDDLProblemInit()
        # print (init)
        state = []

        init_preds = []
        state.append(":init")
        for pred_name in init:
            if "!" in pred_name.name:
                aux = []
                aux.append('not')
                pred_name.name = re.sub('[&!]', '', pred_name.name)
                aux.append([pred_name.name])
                init_preds.append(aux)
            else:
                pred_name.name = re.sub('[&!]', '', pred_name.name)
                init_preds.append([pred_name.name])

            if pred_name.p_vars != []:
                init_preds.append(effect.p_vars)

        state.append(init_preds)


        # print (state)
        return state

    def getProblemInitFormated(self,planning_problem):
        init = planning_problem.getPDDLProblemInit()
        # print (init)
        state = []

        init_preds = []
        # state.append(":init")
        for pred_name in init:
            # if "!" in pred_name.name:
            #     aux = []
            #     aux.append('not')
            #     pred_name.name = re.sub('[&!]', '', pred_name.name)
            #     aux.append([pred_name.name])
            #     init_preds.append(aux)
            # else:
            #     pred_name.name = re.sub('[&!]', '', pred_name.name)
            #     init_preds.append([pred_name.name])

            # if pred_name.p_vars != []:
            #     init_preds.append(effect.p_vars)
            init_preds.append([pred_name.name])
        state = init_preds


        # print (state)
        return state

    def getProblemGoal(self,planning_problem):
        goal = planning_problem.getPDDLProblemGoal()
        state = []

        init_preds = []
        init_preds.append('and')
        state.append(":goal")
        for pred_name in goal:
            if "!" in pred_name.name:
                aux = []
                aux.append('not')
                name = re.sub('[&!]', '', pred_name.name)
                aux.append([name])
                init_preds.append(aux)
            else:
                name = re.sub('[&!]', '', pred_name.name)
                init_preds.append([name])

            if pred_name.p_vars != []:
                init_preds.append(effect.p_vars)

        state.append(init_preds)

        # print (state)
        return state


    def getProblemGoalPos(self,planning_problem):
        goal = planning_problem.getPDDLProblemGoal()
        state = []

        init_preds = []
        for pred_name in goal:
            # if "!" in pred_name.name:
            #     aux = []
            #     aux.append('not')
            #     pred_name.name = re.sub('[&!]', '', pred_name.name)
            #     aux.append([pred_name.name])
            #     init_preds.append(aux)
            # else:
            # print(pred_name)
            if "!" not in pred_name.name:
                name = re.sub('[&!]', '', pred_name.name)
                state.append([name])

            if pred_name.p_vars != []:
                init_preds.append(pred_name.p_vars)

        # state.append(init_preds)

        # print (state)
        return state

    def getProblemGoalNeg(self,planning_problem):
        goal = planning_problem.getPDDLProblemGoal()
        state = []

        init_preds = []
        for pred_name in goal:
            # if "!" in pred_name.name:
            #     aux = []
            #     aux.append('not')
            #     pred_name.name = re.sub('[&!]', '', pred_name.name)
            #     aux.append([pred_name.name])
            #     init_preds.append(aux)
            # else:
            # print(pred_name)
            if "!" in pred_name.name:
                name = re.sub('[&!]', '', pred_name.name)
                state.append([name])

            if pred_name.p_vars != []:
                init_preds.append(pred_name.p_vars)

        # state.append(init_preds)

        # print (state)
        return state

    def solve(self, planning):
        # Parsed data
        actions = self.getDomainActionsFormated(planning)
        state = self.getProblemInitFormated(planning)
        # goal = self.getProblemGoal(planning)
        goal_pos = self.getProblemGoalPos(planning)
        goal_not = self.getProblemGoalNeg(planning)

        for act in actions:
            print(act)
        # print(state)
        # print(goal_pos)
        # print(goal_not)
        
        # state = parser.state
        # goal_pos = parser.positive_goals
        # goal_not = parser.negative_goals

        # Do nothing
        if self.applicable(state, goal_pos, goal_not):
            return []
        # Search
        visited = [state]
        fringe = [state, None]
        while fringe:
            state = fringe.pop(0)
            plan = fringe.pop(0)
            for act in actions:
                if self.applicable(state, act.positive_preconditions, act.negative_preconditions):
                    new_state = self.apply(state, act.add_effects, act.del_effects)
                    if new_state not in visited:
                        if self.applicable(new_state, goal_pos, goal_not):
                            full_plan = [act]
                            while plan:
                                act, plan = plan
                                full_plan.insert(0, act)
                            return full_plan
                        visited.append(new_state)
                        fringe.append(new_state)
                        fringe.append((act, plan))
        return None

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


def parse(pmode, pinput):
    if len(pinput) > 2:
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


planner = Propositional_Planner()
plan = planner.solve(planning)

if plan:
    print('plan:')
    for act in plan:
        print(act)
else:
    print('No plan was found')
# print(planning.getPDDLDomainPredicates())

            