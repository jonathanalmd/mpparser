
class ADLAction:
    def __init__(self, action_name, param, precond, effect):
        self.name = action_name
        self.param = param
        self.precond = precond
        self.effect = effect

    def __str__(self):
        return "\n\tAction Name: " + self.name + "\n\tParameters: " + str(self.param) + "\n\tPrecondition: " + str(self.precond) + "\n\tEffect: " + str(self.effect) + "\n"

    def __repr__(self):
        return "\n\tAction Name: " + self.name + "\n\tParameters: " + str(self.param) + "\n\tPrecondition: " + str(self.precond) + "\n\tEffect: " + str(self.effect) + "\n"

class ADLInfo:
    def __init__(self, initial_state, goal_state, actions):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.actions = actions

    def __str__(self):
        return "\nInitial State:\n\t" + str(self.initial_state) + "\nGoal State: \n\t" + str(self.goal_state) + "\nActions: \n\t" + str(self.actions) + "\n"

    def __repr__(self):
        return "\nInitial State:\n\t" + str(self.initial_state) + "\nGoal State: \n\t" + str(self.goal_state) + "\nActions: \n\t" + str(self.actions) + "\n"


class ADLFormParse:
    def __init__(self):
        self.lista_predicados = []
        self.lista_ids = []
        self.lista_ids_sep = []

        self.adl_init = []
        self.adl_goal = []
        self.adl_actions = []
        self.dealingwith = 0

        self.action_names = []

        self.action_params = []
        self.action_params_sep = []
        self.action_p_types = []
        self.action_p_types_sep = []

        self.action_precond = []
        self.action_effect = []

    def appendPredicado(self, upred):
        self.lista_predicados.append(upred)

    def appendId(self, uid):
        self.lista_ids.append(uid)

    def appendListIds(self):
        self.lista_ids.reverse()
        self.lista_ids_sep.append(self.lista_ids)
        self.lista_ids = []

    def appendActionName(self, aname):
        self.action_names.append(aname)
    
    def appendActionParam(self, aparam):
        self.action_params.append(aparam)
    
    def appendActionParamType(self, ptype):
        self.action_p_types.append(ptype)

    def appendListActionParam(self):
        self.action_params_sep.append(self.action_params)
        self.action_p_types_sep.append(self.action_p_types)
        self.cleanActionParam()
        self.cleanActionTypes()

    def cleanActionParam(self):
        self.action_params = []

    def cleanActionTypes(self):
        self.action_p_types = []

    def cleanListIds(self):
        self.lista_ids_sep = []

    def cleanListPreds(self):
        self.lista_predicados = []

    def setPredicates(self):
        if self.dealingwith == 0: # init
            # print ("<DEALING_INIT>")
            # print ("\t<PRED>",self.lista_predicados)
            # print ("\t>>>>>>",self.lista_ids_sep)

            for pred_name, pred_params in zip(self.lista_predicados, self.lista_ids_sep):
                self.adl_init.append(pred_name)
                self.adl_init.append(pred_params)
            # print (self.adl_init)

        elif self.dealingwith == 1: # goal
            # print ("<DEALING_GOAL>")
            # print ("\t<PRED>",self.lista_predicados)
            # print ("\t>>>>>>",self.lista_ids_sep)

            for pred_name, pred_params in zip(self.lista_predicados, self.lista_ids_sep):
                self.adl_goal.append(pred_name)
                self.adl_goal.append(pred_params)
            # print (self.adl_goal)

        else: # action(s)
            # print ("<DEALING_ACTION>")
            # print ("\t<PRED>",self.lista_predicados)
            # print ("\t>>>>>>",self.lista_ids_sep)

            if self.dealingwith % 2 == 0:
                # print("precond")
                precond = []
                for pred_name, pred_params in zip(self.lista_predicados, self.lista_ids_sep):
                    # aux_list = []
                    # aux_list.append(pred_name)
                    # aux_list.append(pred_params)
                    # aux_list = self.action_precond.append(aux_list)
                    # print(aux_list)

                    # precond[pred_name] = pred_params

                    precond.append(pred_name)
                    precond.append(pred_params)
                
                self.action_precond.append(precond)

            else:
                # print("effect")
                effect = []
                for pred_name, pred_params in zip(self.lista_predicados, self.lista_ids_sep):
                    # self.action_precond.append(pred_name)
                    # self.action_precond.append(pred_params)   
                    effect.append(pred_name)
                    effect.append(pred_params)
                
                self.action_effect.append(effect)

    def setADLActions(self):
        # print("<TYPES>:",self.action_p_types_sep)
        # print("<vars>:",self.action_params_sep)
        
        paction_list = []
        for param_types, param_vars in zip(self.action_p_types_sep, self.action_params_sep):
            paction = {}
            for utype, uvar in zip(param_types, param_vars):
                paction[uvar] = utype
            paction_list.append(paction)
        # print("\n<PARAMETERS:",paction_list)

        for action_name, param, precond, effect in zip(self.action_names, paction_list, self.action_precond, self.action_effect):
            uaction = ADLAction(action_name,param,precond,effect)
            self.adl_actions.append(uaction)

        # print (self.adl_actions)

    def printADLInfo(self):
        print ("\n")
        print ("Init Predicates:\n\t",self.adl_init)
        print ("\n")
        print ("Goal Predicates:\n\t",self.adl_goal)
        print ("\n")
        print ("Actions:\n\t",self.adl_actions)

    def getADL(self):
        return ADLInfo(self.adl_init, self.adl_goal, self.adl_actions)



