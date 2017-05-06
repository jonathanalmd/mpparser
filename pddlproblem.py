
class PDDLInitPredicate:
    def __init__(self, pred_name):
        self.name = pred_name
        self.p_vars = [] 
    
    def __str__(self):
        return self.name + ":" + str(self.p_vars)

    def __repr__(self):
        return self.name + ":" + str(self.p_vars)


class PDDLProblem:
    def __init__(self):
        self.problem_name = ""
        self.problem_domain = ""
        self.problem_objects = {}
        self.problem_init_pred = []

        self.lista_obj_type = []

        self.lista_ids = []
        self.lista_ids_sep = []

        self.lista_problem_pred = []

    def setProblemName(self, name):
        self.problem_name = name

    def setProblemDomain(self, domain):
        self.problem_domain = domain

    def setProblemObjects(self):
        self.lista_obj_type.reverse()
        # print(self.lista_obj_type)
        # print(self.lista_ids_sep)

        for obj_type, ids in zip(self.lista_obj_type, self.lista_ids_sep):
            self.problem_objects[obj_type] = ids


        # cleann variables to use in :INIT formalization
        self.cleanProblemIds()
        self.cleanProblemListaIdsSep()

    def setProblemInitPredicates(self):
        print (self.lista_ids_sep)

        for init_pred in self.lista_ids_sep:
            ipred = PDDLInitPredicate(init_pred[0])
            if init_pred[1:]:
                ipred.p_vars = init_pred[1:]
            else:
                ipred.p_vars = ["(NULL)"]

            self.problem_init_pred.append(ipred)
        
        print (self.problem_init_pred)
        self.cleanProblemIds()
        self.cleanProblemListaIdsSep()

    def appendObjType(self, otype):
        self.lista_obj_type.append(otype)

    def appendId(self, uid):
        self.lista_ids.append(uid)

    def appendListIds(self):
        self.lista_ids.reverse()
        self.lista_ids_sep.append(self.lista_ids)

    def cleanProblemIds(self):
        self.lista_ids = []

    def cleanProblemListaIdsSep(self):
        self.lista_ids_sep = []

    def appendProblemPred(self, ppred):
        self.lista_problem_pred.append(ppred)

    def printProblemInfo(self):
        print ("Problem Name:\n\t",self.problem_name)
        print ("From Domain:\n\t",self.problem_domain)
        print ("Objects:\n\t",self.problem_objects)




