

class StripsAction:
    def __init__(self):
        self.name = ""
        self.param = []
        self.precond = []
        self.effect = []

    def __str__(self):
        return "\n\tAction Name: " + self.name + "\n\tParameters: " + str(self.param) + "\n\tPrecondition: " + str(self.precond) + "\n\tEffect: " + str(self.effect) + "\n"

    def __repr__(self):
        return "\n\tAction Name: " + self.name + "\n\tParameters: " + str(self.param) + "\n\tPrecondition: " + str(self.precond) + "\n\tEffect: " + str(self.effect) + "\n"

class StripsInfo:
    def __init__(self, initial_state, goal_state, actions):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.actions = actions

    def getInitialState(self):
        return self.initial_state

    def getGoalState(self):
        return self.goal_state

    def getActions(self):
        return self.actions

    def __str__(self):
        return "\nInitial State:\n\t" + str(self.initial_state) + "\nGoal State: \n\t" + str(self.goal_state) + "\nActions: \n\t" + str(self.actions) + "\n"

    def __repr__(self):
        return "\nInitial State:\n\t" + str(self.initial_state) + "\nGoal State: \n\t" + str(self.goal_state) + "\nActions: \n\t" + str(self.actions) + "\n"

class StripsFormParse:
    def __init__(self):
        self.lista_ids = []
        self.lista_ids_sep = []
        self.lista_pred_names = []

        self.strips_initial = []
        self.strips_goal = []
        self.strips_actions = []

        self.strips_action = StripsAction()

        self.c_section = 0

    def appendId(self, uid):
        self.lista_ids.append(uid)

    def appendListIds(self):
        self.lista_ids.reverse()
        self.lista_ids_sep.append(self.lista_ids)
        self.lista_ids = []

    def appendPredName(self, pname):
        self.lista_pred_names.append(pname)

    def cleanListIds(self):
        self.lista_ids_sep = []

    def dealWithPredicates(self):
        if self.c_section == 0: #initial
            for pred_name, pred_vars in zip(self.lista_pred_names, self.lista_ids_sep):
                self.strips_initial.append(pred_name)
                self.strips_initial.append(pred_vars)
            # print("INITIAL>>>",self.strips_initial)

        elif self.c_section == 1: #goal
            for pred_name, pred_vars in zip(self.lista_pred_names, self.lista_ids_sep):
                self.strips_goal.append(pred_name)
                self.strips_goal.append(pred_vars)
            # print("GOAL>>>",self.strips_goal)
            
        else: # actions
            if self.c_section % 2 == 0: # action name and preconds
                self.strips_action.name = self.lista_pred_names[0]
                self.strips_action.param = self.lista_ids_sep[0]
                list_aux = []

                for pred_name, pred_vars in zip(self.lista_pred_names[1:], self.lista_ids_sep[1:]):
                    list_aux.append(pred_name)
                    list_aux.append(pred_vars)

                self.strips_action.precond = list_aux

            else: # action effects
                for pred_name, pred_vars in zip(self.lista_pred_names, self.lista_ids_sep):
                    self.strips_action.effect.append(pred_name)
                    self.strips_action.effect.append(pred_vars)

                self.strips_actions.append(self.strips_action)
                # print(self.strips_action)
                self.strips_action = StripsAction()

        self.c_section += 1
        self.lista_pred_names = []
        self.cleanListIds()

    def printStripsInfo(self):
        print ("\n")
        print ("Initial State:\n\t",self.strips_initial)
        print ("Goal State:\n\t",self.strips_goal)
        print ("Actions:\n\t",self.strips_actions)
        print ("\n")

    def getStrips(self):
        return StripsInfo(self.strips_initial, self.strips_goal, self.strips_actions)




