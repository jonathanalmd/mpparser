import re

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

    def __repr__(self):
        return 'action: ' + self.name + \
        '\n  parameters: ' + str(self.parameters) + \
        '\n  positive_preconditions: ' + str(self.positive_preconditions) + \
        '\n  negative_preconditions: ' + str(self.negative_preconditions) + \
        '\n  add_effects: ' + str(self.add_effects) + \
        '\n  del_effects: ' + str(self.del_effects) + \
        '\n  cost: ' + str(self.cost) + '\n'

    def __eq__(self, other): 
        return self.__dict__ == other.__dict__


class BFSPlanner:
    def __init__(self, rmode):
        self.actions = []
        self.rmode = rmode 

    def getDomainActions(self,planning_domain):

        if self.rmode == "pddl":
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
        elif self.rmode == "adl":
            pass
        return action

    def getDomainActionsFormated(self,planning_domain):

        if self.rmode == "pddl":
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
        elif self.rmode == "adl":
            act = planning_domain.getADLActions()
            actions = []
            for single_action in act:
                # print (single_action)
                # action.append(":action")
                aname = single_action.name
                # action.append(":parameters")
                # action.append(list(single_action.parameters.values()))
                parameters = list(single_action.param.values())
                # action.append(":precondition")
                negative_preconditions = []
                positive_preconditions = []
                for i in range (0, len(single_action.precond),2):
                    if "!" in single_action.precond[i]:
                        negative_preconditions.append([re.sub('[&!]', '', single_action.precond[i])])
                    else:
                        positive_preconditions.append([re.sub('[&!]', '', single_action.precond[i])])

                # action.append(":effects")
                add_effects = []
                del_effects = []
                for i in range(0, len(single_action.effect), 2):
                    if "!" in single_action.effect[i]:
                        del_effects.append([re.sub('[&!]', '', single_action.effect[i])])
                    else:
                        add_effects.append([re.sub('[&!]', '', single_action.effect[i])])


                actions.append(Action(aname, parameters, positive_preconditions, negative_preconditions, add_effects, del_effects))
            # print (action)
        else: #strips
            act = planning_domain.getSTRIPSActions()
            actions = []
            for single_action in act:
                # print (single_action)
                # action.append(":action")
                aname = single_action.name
                # action.append(":parameters")
                # action.append(list(single_action.parameters.values()))
                parameters = single_action.param

                # action.append(":precondition")
                negative_preconditions = []
                positive_preconditions = []
                for i in range (0, len(single_action.precond),2):
                    if "!" in single_action.precond[i]:
                        negative_preconditions.append([re.sub('[&!]', '', single_action.precond[i])])
                    else:
                        positive_preconditions.append([re.sub('[&!]', '', single_action.precond[i])])

                # action.append(":effects")
                add_effects = []
                del_effects = []
                for i in range(0, len(single_action.effect), 2):
                    if "!" in single_action.effect[i]:
                        del_effects.append([re.sub('[&!]', '', single_action.effect[i])])
                    else:
                        add_effects.append([re.sub('[&!]', '', single_action.effect[i])])


                actions.append(Action(aname, parameters, positive_preconditions, negative_preconditions, add_effects, del_effects))
            # print (action)
        print(actions)
        return actions

    def getProblemInit(self,planning_problem):
        
        if self.rmode == "pddl":
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

        elif self.rmode == "adl":
            pass

        return state

    def getProblemInitFormated(self,planning_problem):
        if self.rmode == "pddl":
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

        elif self.rmode == "adl":
            init = planning_problem.getADLInitialState()
            # print ("INIT>",init)
            state = []

            init_preds = []
            # state.append(":init")
            for i in range(0,len(init)-1,2):
                init_preds.append([init[i]])

            state = init_preds
        else: #strips
        # print (state)
            init = planning_problem.getSTRIPSInitialState()
            # print ("INIT>",init)
            state = []

            init_preds = []
            # state.append(":init")
            for i in range(0,len(init)-1,2):
                init_preds.append([init[i]])

            state = init_preds
        return state

    def getProblemGoal(self,planning_problem):
        if self.rmode == "pddl":
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

        elif self.rmode == "adl":
            pass

        # print ("STATE>",state)
        return state


    def getProblemGoalPos(self,planning_problem):
        if self.rmode == "pddl":
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
            # if init_preds:
            #     state.append(init_preds)
        
        elif self.rmode == "adl":
            goal = planning_problem.getADLGoalState()
            state = []
            # print(goal)
            init_preds = []
            for i in range(0,len(goal)-1,2):
                # print(i)
                if "!" not in goal[i]:
                    name = re.sub('[&!]', '', goal[i])
                    state.append([name])
                if goal[i+1]:
                    init_preds.append(goal[i+1])
                # if "!" in pred_name.name:
                #     aux = []
                #     aux.append('not')
                #     pred_name.name = re.sub('[&!]', '', pred_name.name)
                #     aux.append([pred_name.name])
                #     init_preds.append(aux)
                # else:
                # print(pred_name)
                # if "!" not in pred_name.name:
                #     name = re.sub('[&!]', '', pred_name.name)
                #     state.append([name])

                # if pred_name.p_vars != []:
                #     init_preds.append(pred_name.p_vars)
    
        else:#strips
            goal = planning_problem.getSTRIPSGoalState()
            state = []
            # print(goal)
            init_preds = []
            for i in range(0,len(goal)-1,2):
                # print(i)
                if "!" not in goal[i]:
                    name = re.sub('[&!]', '', goal[i])
                    state.append([name])
                if goal[i+1]:
                    init_preds.append(goal[i+1])
                # if "!" in pred_name.name:
                #     aux = []
                #     aux.append('not')
                #     pred_name.name = re.sub('[&!]', '', pred_name.name)
                #     aux.append([pred_name.name])
                #     init_preds.append(aux)
                # else:
                # print(pred_name)
                # if "!" not in pred_name.name:
                #     name = re.sub('[&!]', '', pred_name.name)
                #     state.append([name])

                # if pred_name.p_vars != []:
                #     init_preds.append(pred_name.p_vars)
        if init_preds:
            state.append(init_preds)

        # print (state)
        return state

    def getProblemGoalNeg(self,planning_problem):
        if self.rmode == "pddl":
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
        elif self.rmode == "adl":
            goal = planning_problem.getADLGoalState()
            state = []
            # print(goal)
            init_preds = []
            for i in range(0,len(goal)-1,2):
                # print(i)
                if "!" in goal[i]:
                    name = re.sub('[&!]', '', goal[i])
                    state.append([name])
                if goal[i+1]:
                    init_preds.append(goal[i+1])
                # if "!" in pred_name.name:
                #     aux = []
                #     aux.append('not')
                #     pred_name.name = re.sub('[&!]', '', pred_name.name)
                #     aux.append([pred_name.name])
                #     init_preds.append(aux)
                # else:
                # print(pred_name)
                # if "!" not in pred_name.name:
                #     name = re.sub('[&!]', '', pred_name.name)
                #     state.append([name])

                # if pred_name.p_vars != []:
                #     init_preds.append(pred_name.p_vars)
        else: #strips
            goal = planning_problem.getSTRIPSGoalState()
            state = []
            # print(goal)
            init_preds = []
            for i in range(0,len(goal)-1,2):
                # print(i)
                if "!" in goal[i]:
                    name = re.sub('[&!]', '', goal[i])
                    state.append([name])
                if goal[i+1]:
                    init_preds.append(goal[i+1])

        if init_preds:
            state.append(init_preds)
                
        # print (state)
        return state

    def setParsedData(self,planning):

        actions = self.getDomainActionsFormated(planning)
        state = self.getProblemInitFormated(planning)
        # goal = self.getProblemGoal(planning)
        goal_pos = self.getProblemGoalPos(planning)
        goal_not = self.getProblemGoalNeg(planning)

        return actions, state, goal_pos, goal_not

    def solve(self, planning):
        print("RUN_MODE>",self.rmode)

        # Parsed data
        actions, state, goal_pos, goal_not = self.setParsedData(planning)

        # for act in actions:
        #     print(act)
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



