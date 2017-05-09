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

class ActionStar:
    """
    An action schema
    """
    def __init__(self, name, parameters=(), preconditions=(), effects=(),
                 unique=False, no_permute=False):
        """
        A PDDL-like action schema
        @arg name : action name for display purposes
        @arg parameters : tuple of ('type', 'param_name') tuples indicating
                          action parameters
        @arg precondtions : tuple of preconditions for the action
        @arg effects : tuple of effects of the action
        @arg unique : if True, only ground with unique arguments (no duplicates)
        @arg no_permute : if True, do not ground an action twice with the same
                          set of (permuted) arguments
        """
        self.name = name
        if len(parameters) > 0:
            self.types, self.arg_names = zip(*parameters)
        else:
            self.types = tuple()
            self.arg_names = tuple()
        self.preconditions = preconditions
        self.effects = effects
        self.unique = unique
        self.no_permute = no_permute

class DomainStar:

    def __init__(self, actions=()):
        """
        Represents a PDDL-like Problem Domain
        @arg actions : list of Action objects
        """
        self.actions = tuple(actions)

    def ground(self, objects):
        """
        Ground all action schemas given a dictionary
        of objects keyed by type
        """
        grounded_actions = list()
        for action in self.actions:
            param_lists = [objects[t] for t in action.types]
            param_combos = set()
            for params in product(*param_lists):
                param_set = frozenset(params)
                if action.unique and len(param_set) != len(params):
                    continue
                if action.no_permute and param_set in param_combos:
                    continue
                param_combos.add(param_set)
                grounded_actions.append(action.ground(*params))
        return grounded_actions

class MLPlanner:
    def __init__(self, rmode):
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

        # print (state)
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

        print(actions,state,goal_pos,goal_not, sep="\n\n")
        return actions, state, goal_pos, goal_not

    def aStarPlanner(self, planning):
        actions, state, goal_pos, goal_not = self.setParsedData(planning)

        actions = planning.getPDDLDomainActions()

        for action in actions:
            print (action)
            #get parameters
            param_tuples = []
            for key, value in action.parameters.items():
                param_tuple = [key]
                for var in value:
                    param_tuple.append(var)
                param_tuples.append(tuple(param_tuple))

            param_tuples = tuple(param_tuples)
            print(param_tuples)

            #get preconditions
            precond_tuples = []
            for precond in action.preconditions:
                precond_tuple = []
                if "!" in precond.name:
                    name = re.sub('[&!]', '', precond.name)
                    precond_tuple.append(name)
                for var in precond.p_vars:
                    # deal with '='
                    precond_tuple.append(var)
                precond_tuples.append(tuple(precond_tuple))

            precond_tuples = tuple(precond_tuples)
            print(precond_tuples)

            # action_star = ActionStar(action.name)
            domain = []
            domain.append(action)


        
    def bfsPlanner(self, planning):
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



