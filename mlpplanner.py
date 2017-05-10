import re
import astar
from itertools import product,zip_longest
import operator as ops

NUM_OPS = {
    '>' : ops.gt,
    '<' : ops.lt,
    '=' : ops.eq,
    '>=': ops.ge,
    '<=': ops.le
}
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
        self.types = []
        self.arg_names = []
        if len(parameters) > 0:
            for param in parameters:
                if param[0] != "(NOTYPE)":
                    self.types.append(param[0])
                    self.arg_names.append(param[1:])
                else:
                    self.arg_names.append(param[1:])
        # if len(parameters) > 0:
        #     *self.types, self.arg_names = zip_longest(*parameters)
            
        # else:
        self.types = tuple(self.types)
        self.arg_names = tuple(self.arg_names)
        print(">>>>>",self.types)
        print(">>>>>",self.arg_names)
        self.preconditions = preconditions
        self.effects = effects
        self.unique = unique
        self.no_permute = no_permute

    def ground(self, *args):
        return _GroundedAction(self, *args)

    def __str__(self):
        arglist = ', '.join(['%s - %s' % pair for pair in zip(self.arg_names, self.types)])
        return '%s(%s)' % (self.name, arglist)

class _GroundedAction(object):
    """
    An action schema that has been grounded with objects
    """
    def __init__(self, action, *args):
        self.name = action.name
        ground = _grounder(action.arg_names, args)

        # Ground Action Signature
        print(action.arg_names)
        self.sig = ground((self.name,) + action.arg_names)
        print("GROUND",self.sig)

        # Ground Preconditions
        self.preconditions = list()
        self.num_preconditions = list()
        for pre in action.preconditions:
            if pre[0] in NUM_OPS:
                operands = [0, 0]
                for i in range(2):
                    if type(pre[i + 1]) == int:
                        operands[i] = pre[i + 1]
                    else:
                        operands[i] = ground(pre[i + 1])
                np = _num_pred(NUM_OPS[pre[0]], *operands)
                self.num_preconditions.append(np)
            else:
                self.preconditions.append(ground(pre))

        print("AAAA")
        # Ground Effects
        self.add_effects = list()
        self.del_effects = list()
        self.num_effects = list()
        for effect in action.effects:
            if effect[0] == -1:
                self.del_effects.append(ground(effect[1]))
            elif effect[0] == '+=':
                function = ground(effect[1])
                value = effect[2]
                self.num_effects.append((function, value))
            elif effect[0] == '-=':
                function = ground(effect[1])
                value = -effect[2]
                self.num_effects.append((function, value))
            else:
                self.add_effects.append(ground(effect))

    def __str__(self):
        arglist = ', '.join(map(str, self.sig[1:]))
        return '%s(%s)' % (self.sig[0], arglist)

class State(object):

    def __init__(self, predicates, functions, cost=0, predecessor=None):
        """Represents a state for A* search"""
        self.predicates = frozenset(predicates)
        self.functions = tuple(functions.items())
        self.f_dict = functions
        self.predecessor = predecessor
        self.cost = cost

    def is_true(self, predicates, num_predicates):
        return (all(p in self.predicates for p in predicates) and
                all(np(self) for np in num_predicates))

    def apply(self, action, monotone=False):
        """
        Apply the action to this state to produce a new state.
        If monotone, ignore the delete list (for A* heuristic)
        """
        new_preds = set(self.predicates)
        new_preds |= set(action.add_effects)
        if not monotone:
            new_preds -= set(action.del_effects)
        new_functions = dict()
        new_functions.update(self.functions)
        for function, value in action.num_effects:
            new_functions[function] += value
        return State(new_preds, new_functions, self.cost + 1, (self, action))

    def plan(self):
        """
        Follow backpointers to successor states
        to produce a plan.
        """
        plan = list()
        n = self
        while n.predecessor is not None:
            plan.append(n.predecessor[1])
            n = n.predecessor[0]
        plan.reverse()
        return plan

    # Implement __hash__ and __eq__ so we can easily
    # check if we've encountered this state before

    def __hash__(self):
        return hash((self.predicates, self.functions))

    def __eq__(self, other):
        return ((self.predicates, self.functions) ==
                (other.predicates, other.functions))

    def __str__(self):
        return ('Predicates:\n%s' % '\n'.join(map(str, self.predicates))
                +'\nFunctions:\n%s' % '\n'.join(map(str, self.functions)))
    def __lt__(self, other):
        return hash(self) < hash(other)

class DomainStar:

    def __init__(self, actions):
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


class ProblemStar:

    def __init__(self, domain, objects, init=(), goal=()):
        """
        Represents a PDDL Problem Specification
        @arg domain : Domain object specifying domain
        @arg objects : dictionary of object tuples keyed by type
        @arg init : tuple of initial state predicates
        @arg goal : tuple of goal state predicates
        """
        # Ground actions from domain
        self.grounded_actions = domain.ground(objects)

        # Parse Initial State
        print(init)
        predicates = list()
        functions = dict()
        for predicate in init:
            print (predicate)
            if predicate[0] == '=':
                functions[predicate[1]] = predicate[2]
            else:
                predicates.append(predicate)
        self.initial_state = State(predicates, functions)

        # Parse Goal State
        self.goals = list()
        self.num_goals = list()
        for g in goal:
            if g[0] in NUM_OPS:
                ng = _num_pred(NUM_OPS[g[0]], *g[1:])
                self.num_goals.append(ng)
            else:
                self.goals.append(g)

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

        # print(actions,state,goal_pos,goal_not, sep="\n\n")
        return actions, state, goal_pos, goal_not

    def setDomainAStar(self,planning):
        actions = planning.getPDDLDomainActions()
        domain = []

        for action in actions:
            # print (action)
            #get parameters
            param_tuples = []
            for key, value in action.parameters.items():
                param_tuple = [key]
                for var in value:
                    param_tuple.append(var)
                param_tuples.append(tuple(param_tuple))

            param_tuples = tuple(param_tuples)
            print("PARAM>::",param_tuples)

            #get preconditions
            precond_tuples = []
            for precond in action.preconditions:
                precond_tuple = []
                precond.name = re.sub('[&]', '', precond.name)
                if "!" in precond.name:
                    name = re.sub('[!]', '', precond.name)
                    precond_tuple.append(-1)
                    # precond_tuple.append(name)
                    aux_tuple = []
                    aux_tuple.append(name)
                    for var in precond.p_vars:
                        # deal with '='
                        if var != "(NOVARS!)":
                            aux_tuple.append(var)
                    precond_tuple.append(tuple(aux_tuple))
                else:
                    precond_tuple.append(precond.name)
                    for var in precond.p_vars:
                        # deal with '='
                        if var != "(NOVARS!)":
                            precond_tuple.append(var)
                precond_tuples.append(tuple(precond_tuple))

            precond_tuples = tuple(precond_tuples)
            # print("PRE>::",precond_tuples)

            #get effects
            effect_tuples = []
            for effect in action.effects:
                effect_tuple = []
                effect.name = re.sub('[&]', '', effect.name)
                if "!" in effect.name:
                    name = re.sub('[!]', '', effect.name)
                    effect_tuple.append(-1)
                    # effect_tuple.append(name)
                    aux_tuple = []
                    aux_tuple.append(name)
                    for var in effect.p_vars:
                        # deal with '='
                        if var != "(NOVARS!)":
                            aux_tuple.append(var)
                    effect_tuple.append(tuple(aux_tuple))
                else:
                    effect_tuple.append(precond.name)
                    for var in effect.p_vars:
                        # deal with '='
                        if var != "(NOVARS!)":
                            effect_tuple.append(var)
                effect_tuples.append(tuple(effect_tuple))

            effect_tuples = tuple(effect_tuples)
            print("EFFECT>:",effect_tuples)

            action_star = ActionStar(action.name,param_tuples,precond_tuples,effect_tuples)
            domain.append(action_star)

        domain_obj = DomainStar(domain)
        return domain_obj
    
    def setProblemAStar(self,planning):
        init_p = planning.getPDDLProblemInit()
        goal_p = planning.getPDDLProblemGoal()

        print(init_p,goal_p, sep = "\n\n")

        init_tuples = []
        for ipred in init_p:
            init_tuple = []
            if "=" in ipred.name:
                init_tuple.append("=")
                ipred.name = re.sub('[=]', '', ipred.name)
                tuple_params = [ipred.name]
                for var in ipred.p_vars[:-1]:
                    tuple_params.append(var)
                init_tuple.append(tuple(tuple_params))
                init_tuple.append(ipred.p_vars[-1])
            else:
                if "!" in ipred.name:
                    name = re.sub('[!]', '', ipred.name)
                    init_tuple.append(-1)
                    # init_tuple.append(name)
                    aux_tuple = []
                    aux_tuple.append(name)
                    for var in ipred.p_vars:
                        # deal with '='
                        if var != "(NOVARS!)":
                            aux_tuple.append(var)
                    init_tuple.append(tuple(aux_tuple))
                else:
                    init_tuple.append(ipred.name)
                    for var in ipred.p_vars:
                        # deal with '='
                        if var != "(NOVARS!)":
                            init_tuple.append(var)
            init_tuples.append(tuple(init_tuple))

        init_tuples = tuple(init_tuples)
        # print (init_tuples)

        goal_tuples = []
        for gpred in goal_p:
            goal_tuple = []
            if "=" in gpred.name:
                goal_tuple.append("=")
                gpred.name = re.sub('[=]', '', gpred.name)
                tuple_params = [gpred.name]
                for var in gpred.p_vars[:-1]:
                    tuple_params.append(var)
                goal_tuple.append(tuple(tuple_params))
                goal_tuple.append(gpred.p_vars[-1])
            else:    
                if "!" in gpred.name:
                    name = re.sub('[!]', '', gpred.name)
                    goal_tuple.append(-1)
                    # goal_tuple.append(name)
                    aux_tuple = []
                    aux_tuple.append(name)
                    for var in gpred.p_vars:
                        # deal with '='
                        if var != "(NOVARS!)":
                            aux_tuple.append(var)
                    goal_tuple.append(tuple(aux_tuple))
                else:
                    goal_tuple.append(gpred.name)
                    for var in gpred.p_vars:
                        # deal with '='
                        if var != "(NOVARS!)":
                            goal_tuple.append(var)
            goal_tuples.append(tuple(goal_tuple))

        goal_tuples = tuple(goal_tuples)
        print (goal_tuples)

        # + objects!!

        return init_tuples, goal_tuples

    def aStarPlanner(self, planning):
        # actions, state, goal_pos, goal_not = self.setParsedData(planning)

        domain = self.setDomainAStar(planning)
        init, goal = self.setProblemAStar(planning)
        objects = planning.getPDDLProblemObjects()
        for key, value in objects.items():
            objects[key] = tuple(value)
        print(objects)
        problem = ProblemStar(domain,objects,init,goal)

        plan = astar.planner(problem)

        return plan            


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

def _grounder(arg_names, args):
    """
    Returns a function for grounding predicates and function symbols
    """
    namemap = dict()
    for arg_name, arg in zip(arg_names, args):
        namemap[arg_name] = arg

    def _ground_by_names(predicate):
        print(predicate[0:1])
        return predicate[0:1] + tuple(namemap.get(arg, arg) for arg in predicate[1:])

    return _ground_by_names

def neg(effect):
    """
    Makes the given effect a negative (delete) effect, like 'not' in PDDL.
    """
    return (-1, effect)


