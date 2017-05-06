


class ADLForm:
    def __init__(self):
        self.lista_predicados = []
        self.lista_ids = []
        self.lista_ids_sep = []

        self.dealingwith = 0

    def appendPredicado(self, upred):
        self.lista_predicados.append(upred)

    def appendId(self, uid):
        self.lista_ids.append(uid)

    def appendListIds(self):
        self.lista_ids.reverse()
        self.lista_ids_sep.append(self.lista_ids)
        self.lista_ids = []

    def cleanListIds(self):
        self.lista_ids_sep = []

    def cleanListPreds(self):
        self.lista_predicados = []

    def setPredicates(self):
        if self.dealingwith == 0: # init
            print ("<DEALING_INIT>")
            print ("\t<PRED>",self.lista_predicados)
            print ("\t>>>>>>",self.lista_ids_sep)
        elif self.dealingwith == 1: # goal
            print ("<DEALING_GOAL>")
            print ("\t<PRED>",self.lista_predicados)
            print ("\t>>>>>>",self.lista_ids_sep)
        else: # action(s)
            print ("<DEALING_ACTION>")
            print ("\t<PRED>",self.lista_predicados)
            print ("\t>>>>>>",self.lista_ids_sep)