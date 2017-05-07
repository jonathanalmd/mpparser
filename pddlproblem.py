
class PDDLProblemPredicate:
    def __init__(self, pred_name):
        self.name = pred_name
        self.p_vars = [] 
    
    def __str__(self):
        return "\n\t" + self.name + ":" + str(self.p_vars)

    def __repr__(self):
        return "\n\t" + self.name + ":" + str(self.p_vars)

class PDDLProblemInfo:
    def __init__(self, problem_name, domain_name, objects, init, goal):
        self.name = problem_name
        self.domain_name = domain_name
        self.objects = objects
        self.init = init
        self.goal = goal

    def getName(self):
        return self.name

    def getProblemDomain(self):
        return self.domain_name

    def getObjects(self):
        return self.objects

    def getInit(self):
        return self.init

    def getGoal(self):
        return self.goal

    def __str__(self):
        return "\nProblem Name:\n\t" + str(self.name) + "\nProblem Domain: \n\t" + str(self.domain_name) + "\nObjects: \n\t" + str(self.objects) + "\nInit: \n\t" + str(self.init) + "\nGoal: \n\t" + str(self.goal) +  "\n"

    def __repr__(self):
        return "\nProblem Name:\n\t" + str(self.name) + "\nProblem Domain: \n\t" + str(self.domain_name) + "\nObjects: \n\t" + str(self.objects) + "\nInit: \n\t" + str(self.init) + "\nGoal: \n\t" + str(self.goal) +  "\n"




class PDDLProblemParse:
    def __init__(self):
        self.problem_name = ""
        self.problem_domain = ""
        self.problem_objects = {}
        self.problem_init_pred = []
        self.problem_goal_pred = []

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

    def setProblemPredicates(self, runmode):
        # print (self.lista_ids_sep)
        # print ("\n\n")
        if runmode == "i":
            for init_pred in self.lista_ids_sep:
                if init_pred[0] == "!":
                    ipred = PDDLProblemPredicate(init_pred[1])
                    ipred.p_vars = init_pred[2:]
                    ipred.name = "!" + ipred.name 
                elif init_pred[0] == "=":
                    # print(init_pred)
                    ipred = PDDLProblemPredicate(init_pred[1])
                    ipred.p_vars = init_pred[2:len(init_pred)-1]
                    ipred_p_vars = ipred.p_vars.append(init_pred[-1])
                    ipred.name = "=" + ipred.name 
                else:
                    ipred = PDDLProblemPredicate(init_pred[0])       
                    ipred.p_vars = init_pred[1:]

                self.problem_init_pred.append(ipred)
        else:
            for goal_pred in self.lista_ids_sep:
                if goal_pred[0] == "!":
                    gpred = PDDLProblemPredicate(goal_pred[1])
                    gpred.p_vars = goal_pred[2:]
                    gpred.name = "!" + gpred.name 
                elif goal_pred[0] == "=":
                    # print(init_pred)
                    gpred = PDDLProblemPredicate(goal_pred[1])
                    gpred.p_vars = goal_pred[2:len(goal_pred)-1]
                    gpred.p_vars = gpred.p_vars.append(goal_pred[-1])
                    gpred.name = "=" + gpred.name 
                else:
                    gpred = PDDLProblemPredicate(goal_pred[0])       
                    gpred.p_vars = goal_pred[1:]

                self.problem_goal_pred.append(gpred)
        # print (self.problem_init_pred)
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
        print ("Init Predicates:\n\t",self.problem_init_pred)
        print ("Goal Predicates:\n\t",self.problem_goal_pred)

    def getPDDLProblem(self):
        return PDDLProblemInfo(self.problem_name, self.problem_domain, self.problem_objects, self.problem_init_pred, self.problem_goal_pred)



