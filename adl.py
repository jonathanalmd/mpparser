


class ADLForm:
    def __init__(self):
        self.lista_predicados = []
        self.lista_ids = []
        self.lista_ids_sep = []

        self.adl_init = []
        self.adl_goal = []

        self.dealingwith = 0

        self.action_names = []
        self.action_params = []
        self.action_p_types = []

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
            print ("<DEALING_ACTION>")
            print ("\t<PRED>",self.lista_predicados)
            print ("\t>>>>>>",self.lista_ids_sep)

            if self.dealingwith % 2 == 0:
                print("precond")
            else:
                print("effect")

    def setADLActions(self):
        print ("\t<name>",self.action_names)


