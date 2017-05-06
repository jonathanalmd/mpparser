

class PDDLProblem:
    def __init__(self):
        self.problem_name = ""
        self.problem_domain = ""
        self.problem_objects = {}

        self.lista_obj_type = []

        self.lista_ids = []
        self.lista_ids_sep = []

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

    def printProblemInfo(self):
        print ("Problem Name:\n\t",self.problem_name)
        print ("From Domain:\n\t",self.problem_domain)
        print ("Objects:\n\t",self.problem_objects)




