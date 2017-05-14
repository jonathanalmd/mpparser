import re
import errorhandler

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
        return "\nProblem Name:\n\t" + str(self.name) + \
        "\nProblem Domain: \n\t" + str(self.domain_name) + \
        "\nObjects: \n\t" + str(self.objects) + \
        "\nInit: \n\t" + str(self.init) + \
        "\nGoal: \n\t" + str(self.goal) + "\n"

    def __repr__(self):
        return "\nProblem Name:\n\t" + str(self.name) + \
        "\nProblem Domain: \n\t" + str(self.domain_name) + \
        "\nObjects: \n\t" + str(self.objects) + \
        "\nInit: \n\t" + str(self.init) + \
        "\nGoal: \n\t" + str(self.goal) + "\n"




class PDDLProblemParse:
    def __init__(self):
        self.problem_name = ""
        self.problem_domain = ""
        self.problem_objects = {}
        self.problem_init_pred = []
        self.problem_goal_pred = []

        self.lista_obj_type = []
        self.problem_used_obj = []

        self.lista_ids = []
        self.lista_ids_sep = []

        self.lista_problem_pred = []

    def setProblemName(self, name):
        self.problem_name = name

    def setProblemDomain(self, domain):
        self.problem_domain = domain

    def setProblemObjects(self):
        self.lista_obj_type.reverse()
        # print(self.lista_ids_sep)
        check_obj_repetition = []
        for obj_type, ids in zip(self.lista_obj_type, self.lista_ids_sep):
            self.problem_objects[obj_type] = ids
            for oid in ids:
                check_obj_repetition.append(oid)

        if len(check_obj_repetition) != len(set(check_obj_repetition)):
            errorhandler.reportError("ot*") # repeated obj from diff types
        # cleann variables to use in :INIT formalization
        self.cleanProblemIds()
        self.cleanProblemListaIdsSep()

    def setProblemPredicates(self, runmode, operator):
        # print (self.lista_ids_sep)
        if runmode == "i":
            for init_pred in self.lista_ids_sep:
                if init_pred[0] == "!":
                    ipred = PDDLProblemPredicate(init_pred[1])
                    ipred.p_vars = init_pred[2:]
                    for obj in init_pred[2:]:
                        self.problem_used_obj.append(obj)
                    ipred.name = "!" + ipred.name 
                elif init_pred[0] == "=":
                    # print(init_pred)
                    ipred = PDDLProblemPredicate(init_pred[1])
                    ipred.p_vars = init_pred[2:len(init_pred)]
                    # ipred_p_vars = ipred.p_vars.append(init_pred[-1])
                    ipred.name = "=" + ipred.name 
                else:
                    ipred = PDDLProblemPredicate(init_pred[0])
                    ipred_vars = []
                    for var in init_pred[1:]:
                        var = re.sub('[!&]', '', var)
                        ipred_vars.append(var)
                        self.problem_used_obj.append(var)
                    # ipred.p_vars = init_pred[1:]
                    ipred.p_vars = ipred_vars
                self.problem_init_pred.append(ipred)
        elif runmode == "g": #goal
            if operator == "and":
                for goal_pred in self.lista_ids_sep:
                    if goal_pred[0] == "!":
                        gpred = PDDLProblemPredicate(goal_pred[1])
                        gpred.p_vars = goal_pred[2:]
                        for obj in goal_pred[2:]:
                            self.problem_used_obj.append(obj)
                        gpred.name = "&!" + gpred.name 
                    elif goal_pred[0] == "=":
                        # print("GOALPred",goal_pred)
                        gpred = PDDLProblemPredicate(goal_pred[1])
                        gpred.p_vars = goal_pred[2:len(goal_pred)]
                        # gpred.p_vars.append(goal_pred[-1])
                        # print (gpred.p_vars)
                        gpred.name = "&=" + gpred.name 
                    else:
                        gpred = PDDLProblemPredicate("&" + goal_pred[0])       
                        gpred.p_vars = goal_pred[1:]
                        for obj in goal_pred[1:]:
                            self.problem_used_obj.append(obj)

                    self.problem_goal_pred.append(gpred)
            else: #or
                for goal_pred in self.lista_ids_sep:
                    if goal_pred[0] == "!":
                        gpred = PDDLProblemPredicate(goal_pred[1])
                        gpred.p_vars = goal_pred[2:]
                        for obj in goal_pred[2:]:
                            self.problem_used_obj.append(obj)
                        gpred.name = "|!" + gpred.name 
                    elif goal_pred[0] == "=":
                        # print("GOALPred",goal_pred)
                        gpred = PDDLProblemPredicate(goal_pred[1])
                        gpred.p_vars = goal_pred[2:len(goal_pred)]
                        # gpred.p_vars.append(goal_pred[-1])
                        # print (gpred.p_vars)
                        gpred.name = "|=" + gpred.name 
                    else:
                        gpred = PDDLProblemPredicate("|" + goal_pred[0])       
                        gpred.p_vars = goal_pred[1:]
                        for obj in goal_pred[1:]:
                            self.problem_used_obj.append(obj)

                    self.problem_goal_pred.append(gpred)

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

    def getPDDLProblem(self):
        return PDDLProblemInfo(self.problem_name, self.problem_domain, self.problem_objects, self.problem_init_pred, self.problem_goal_pred)

    def getUnusedObjects(self):
        defined_objects = []
        used_objects = []
        defined_objects = list(self.problem_objects.values())
        defined_objects = set([item for sublist in defined_objects for item in sublist])

        used_objects = set(self.problem_used_obj)
        unused_objects = defined_objects - used_objects

        return unused_objects

    def __str__(self):
        return "\nProblem: " + self.problem_name + \
        "\n\tFrom Domain: " + str(self.problem_domain) + \
        "\n\tObjects: " + str(self.problem_objects) + \
        "\n\tInit: " + str(self.problem_init_pred) + \
        "\n\tGoal: " + str(self.problem_goal_pred)

    def __repr__(self):
        return "\nProblem: " + self.problem_name + \
        "\n\tFrom Domain: " + str(self.problem_domain) + \
        "\n\tObjects: " + str(self.problem_objects) + \
        "\n\tInit: " + str(self.problem_init_pred) + \
        "\n\tGoal: " + str(self.problem_goal_pred)



