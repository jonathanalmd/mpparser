# %{
# #include <stdio.h> 
# #define YYDEBUG 1
# int yylex (void);
# void yyerror (const char *s);
# extern FILE *yyin;
# extern int yydebug;
# extern int yylineno;
# %}

import sys
import yacc 
import lex
import plex

class PDDLPredicate:
    def __init__(self, pred_name):
        self.name = pred_name
        self.p_vars = {} # {[?b,?b2]:"ball"}
    
    def __str__(self):
        return self.name + " " + str(self.p_vars)

    def __repr__(self):
        return self.name + " " + str(self.p_vars)

class PDDLFunction:
    def __init__(self):
        self.name = ""
        self.f_vars = {}
        self.f_type = ""
    
    def __str__(self):
        return "\tFunction-Name: " + self.name + "\n\tFunction-Type: " + str(self.f_type) + "\n\tFunction-Vars: " + str(self.f_vars) + "\n\n"

    def __repr__(self):
        return "\tFunction-Name: " + self.name + "\n\tFunction-Type: " + str(self.f_type) + "\n\tFunction-Vars: " + str(self.f_vars) + "\n\n"

class PDDLAction:
    def __init__(self):
        self.name = ""
        self.parameters = {}
        self.preconditions = {}
        self.effects = {}
    
    def __str__(self):
        return "\tAction-Name: " + self.name + "\n\tAction-Parameters: " + str(self.parameters) + "\n\tAction-Preconditions: " + str(self.preconditions) + "\n\tAction-Effects: " + str(self.effects) + "\n\n"

    def __repr__(self):
        return "\tAction-Name: " + self.name + "\n\tAction-Parameters: " + str(self.parameters) + "\n\tAction-Preconditions: " + str(self.preconditions) + "\n\tAction-Effects: " + str(self.effects) + "\n\n"

class PDDLDomain:
    def __init__(self, domain_name="", lista_predicados=[], 
                lista_types=[], dict_constants={}, pddl_ids=[], 
                dealing_with_types=[], lista_pddl_ids=[]):
        self.domain_name = domain_name
        self.lista_predicados = lista_predicados
        self.domain_predicates = [] # lista de PDDLPredicate()
        self.domain_functions = [] # lista de PDDLFunction()
        self.domain_types = []
        self.lista_types = lista_types
        self.dict_constants = dict_constants
        self.pddl_ids = pddl_ids
        self.lista_pddl_ids = lista_pddl_ids
        self.dealing_with_types = dealing_with_types

        self.dealing_with_types_sep = []

        self.pddl_vars = []
        self.lista_pddl_vars = [] #[[]]
        self.lista_pddl_vars_sep = [] #[[[]]]

        self.lista_pddl_func = []
        self.lista_pddl_func_types = []


        self.lista_actions = []
        self.domain_actions = [] # lista de PDDLAction()

        self.lista_action_predicados = []

        self.curLogicalOperator = ""

        self.curLineAction = 0

        self.curDealingWith = ""

    def setDomainName(self,domain_name):
        self.domain_name = domain_name

    def setDomainPredicates(self):
        # print(self.lista_predicados)
        # print(self.lista_pddl_vars_sep)
        # print(self.dealing_with_types_sep)
        
        i = 0
        while i < len(self.lista_pddl_vars_sep):
            self.lista_pddl_vars_sep[i] = [x for x in self.lista_pddl_vars_sep[i] if x != []]
            i = i + 1
        self.dealing_with_types_sep = [x for x in self.dealing_with_types_sep if x != []]
        
        if self.dealing_with_types_sep == []:
            for pddl_vars in self.lista_pddl_vars_sep:
                self.dealing_with_types_sep.append(["(NOTYPE)"])
        # print("\n>>>",self.lista_pddl_vars_sep)
        # print("\n>>",self.dealing_with_types_sep)
        
        if len(self.dealing_with_types_sep) != len(self.lista_pddl_vars_sep):
            print("ERRO: predicates must be all typed or all not typed")
            sys.exit()
        else:
            i = 0
            self.lista_predicados.reverse()
            for pred_name in self.lista_predicados:
                pddl_predicate = PDDLPredicate(pred_name)
                len_pred_types = len(self.dealing_with_types_sep[i])
                self.dealing_with_types_sep[i].reverse()
                j = 0
                # print("i",i)
                while j < len_pred_types:
                    # print("j",j)
                    # print(self.dealing_with_types_sep[i][j])
                    # print(self.lista_pddl_vars_sep[i][j])
                    pddl_predicate.p_vars[self.dealing_with_types_sep[i][j]] = self.lista_pddl_vars_sep[i][j]
                    j = j + 1
                i = i + 1

                self.domain_predicates.append(pddl_predicate)
            self.cleanListaPDDLvars()
            self.lista_predicados = []
            self.lista_pddl_vars_sep = []

    def setDomainActions(self, action_name):
        # print(self.lista_pddl_vars_sep)
        # print("ACTION1>>",self.lista_pddl_vars)
        # print("ACTION2>>",self.lista_types)
        # print(self.pddl_vars)
        # self.lista_actions.reverse()
        self.domain_actions[len(self.domain_actions)-len(self.lista_actions)].name = action_name

    def appendFunction(self, func):
        self.lista_pddl_func.append(func)
    def appendFuncType(self, ftype):
        self.lista_pddl_func_types.append(ftype)

    def appendPredicado(self,predicado):
        self.lista_predicados.append(predicado)
    
    def dealWithFunctionDef(self):
        # self.lista_pddl_vars_sep[i] = [x for x in self.lista_pddl_vars_sep[i] if x != []]
        self.lista_pddl_vars = [x for x in self.lista_pddl_vars if x != []]
        self.lista_pddl_func.reverse()
        self.lista_types.reverse()
        self.lista_pddl_func_types.reverse()
        i = 0
        for func in self.lista_pddl_func:
            if func[0] == "0":
                self.lista_pddl_func[i] = func[1:]
                self.lista_pddl_vars.insert(i, ["(NULL)"])
            i = i + 1
        # print("<func-names>:",self.lista_pddl_func)
        # print("<func-vars>:",self.lista_pddl_vars)
        # print("<func-var_types>:",self.lista_types)
        # print("<func-type>:",self.lista_pddl_func_types)

        for i in range(0,len(self.lista_pddl_func)):
            func = PDDLFunction()
            func.name = self.lista_pddl_func[i]
            func.f_vars[self.lista_types[i]] = self.lista_pddl_vars[i]
            func.f_type = self.lista_pddl_func_types[i] 
            self.domain_functions.append(func)

        self.lista_pddl_vars = []
        self.lista_types = []
    def cleanListaPDDLvars(self):
        self.lista_pddl_vars = []

    def appendListaPDDLPredVars(self):
        self.lista_pddl_vars_sep.append(self.lista_pddl_vars)

    def appendType(self,utype):
        self.lista_types.append(utype)
    
    def dealingWithType(self,utype):
        self.dealing_with_types.append(utype)

    def dealingWithTypeSep(self):
        self.dealing_with_types_sep.append(self.dealing_with_types)
        self.dealing_with_types = []

    def appendConstants(self):
        # print(self.lista_pddl_ids)
        # print(self.dealing_with_types)
        if self.lista_pddl_ids:
            len_pddl_ids = len(self.lista_pddl_ids)
            self.lista_pddl_ids.reverse()
            for curr_type, pddl_id in zip(self.dealing_with_types, self.lista_pddl_ids):
                self.dict_constants[curr_type] = pddl_id
            self.dealing_with_types = []
        else:
            print("Erro sintatico: decalracao de constante ausente (só colocou o tipo)")
        self.domain_types = self.lista_types
        
        self.cleanListaPDDLids()
        self.cleanTypes()

    def cleanTypes(self):
        self.lista_types = []

    def dealWithActionLogicPredicate(self):
        for indx_action_predicado in range (0,2):
            last_predicado = self.lista_action_predicados[indx_action_predicado][-1]
            last_predicado = last_predicado.split("*")
            self.lista_action_predicados[indx_action_predicado][-1] = last_predicado[-1]
            last_predicado = last_predicado[:-1]
            # print(indx_action_predicado,"LAST_PREDICADO>>>",last_predicado)
            len_action_pred = len(self.lista_action_predicados[indx_action_predicado]) - 1
            for logic_operator in last_predicado:
                op = logic_operator[0]
                num = int(logic_operator[1:])
                # print("pre",op,num)
                for i in range(0,num):
                    if op == "!" and self.lista_action_predicados[indx_action_predicado][len_action_pred - i][0] == "!":
                        print("WARNING: junte os predicados em uma unica operacao logica: ",self.lista_action_predicados[indx_action_predicado][len_action_pred - i][2:], "e", self.lista_action_predicados[indx_action_predicado][len_action_pred - i - 1][2:])
                        break
                    else:
                        self.lista_action_predicados[indx_action_predicado][len_action_pred - i] = op + self.lista_action_predicados[indx_action_predicado][len_action_pred - i]
            # print("pre_predicados:",self.lista_action_predicados[indx_action_predicado])

        # last_predicado = self.lista_action_predicados[1][-1]
        # last_predicado = last_predicado.split("*")
        # self.lista_action_predicados[1][-1] = last_predicado[-1]
        # last_predicado = last_predicado[:-1]
        # print("\n\n\n")
        # # print("2222LAST_PREDICADO>>>",last_predicado)
        # for logic_operator in last_predicado:
        #     op = logic_operator[0]
        #     num = int(logic_operator[1:])
        #     print("ef",op,num)
        # print("ef_predicados:",self.lista_action_predicados[1])
    def dealWithAction(self):
        # print("ACTION>>>>",self.lista_actions)
        # print(self.lista_pddl_vars_sep)
        # print("ACTION2>>",self.lista_types)
        self.lista_pddl_vars[0] = [x for x in self.lista_pddl_vars[0] if x != []]
        self.lista_pddl_vars[1] = [x for x in self.lista_pddl_vars[1] if x != []]
        self.lista_pddl_vars[2] = [x for x in self.lista_pddl_vars[2] if x != []]
        # print("ACTION1>>",self.lista_pddl_vars)
        # print("<TYPE>>>>>",self.lista_types)

        if self.lista_types == []:
            for pddl_vars in self.lista_pddl_vars[0]:
                self.lista_types.append("(NOTYPE)")

        if (len(self.lista_types) != len(self.lista_pddl_vars[0])) and all(isinstance(n, list) for n in self.lista_pddl_vars[0]):
            print("ERRO: action parameters variables in line %d must be all typed or all not typed"%(self.curLineAction))
            print("\tType(s)",self.lista_types)
            print("\tVar(s)",self.lista_pddl_vars[0])
            print("\tExpecting " + str(len(self.lista_pddl_vars[0])) + " type(s) and received only " + str(len(self.lista_types)) + " type(s)")
            
            sys.exit()
        else:
            action = PDDLAction()
            i = 0
            if all(isinstance(n, list) for n in self.lista_pddl_vars[0]):
                for utype in self.lista_types:
                    self.lista_pddl_vars[0][i].reverse()
                    action.parameters[utype] = self.lista_pddl_vars[0][i]
                    i = i + 1
            else:
                self.lista_pddl_vars[0].reverse()
                for utype in self.lista_types:
                    action.parameters[utype] = self.lista_pddl_vars[0]
                    i = i + 1
            # print(action.parameters)
            # action.parameters = self.lista_pddl_vars[0]
            self.lista_action_predicados[0].reverse()
            self.lista_action_predicados[1].reverse()
            self.dealWithActionLogicPredicate()
            i = 0
            for predicate in self.lista_action_predicados[0]:
                self.lista_pddl_vars[1][i].reverse()
                action.preconditions[predicate] = self.lista_pddl_vars[1][i]
                i = i + 1
            i = 0
            for predicate in self.lista_action_predicados[1]:
                self.lista_pddl_vars[2][i].reverse()
                action.effects[predicate] = self.lista_pddl_vars[2][i]
                i = i + 1
            self.domain_actions.append(action)
            # print("\n\n\n\n")
            # print(action)
            # print("<TYPES>",self.lista_types)
            # print(action)

            # print(self.lista_predicados)
            # print("PTOTAL>>>>>>>>>>>",self.lista_action_predicados)



            self.lista_action_predicados = []

            self.cleanPDDLvars()
            self.cleanListaPDDLvars()
            self.cleanTypes()

    def appendPDDLid(self,pddl_id):
        self.pddl_ids.append(pddl_id)

    def appendListaPDDLids(self):
        self.lista_pddl_ids.append(self.pddl_ids)

    def cleanListaPDDLids(self):
        self.lista_pddl_ids = []

    def cleanPDDLids(self):
        self.pddl_ids = []

    def appendVar(self,pddl_var):
        self.pddl_vars.append(pddl_var)

    def appendListaPDDLvars(self):
        self.lista_pddl_vars.append(self.pddl_vars)

    def cleanPDDLvars(self):
        self.pddl_vars = []


    def dealWithParameters(self):
        # print (self.pddl_vars)
        if self.pddl_vars:
            self.lista_pddl_vars = [x for x in self.lista_pddl_vars if x != []]

            lista = []
            lista = self.lista_pddl_vars
            lista.append(self.pddl_vars)
            # print(lista)
            # lista = self.lista_pddl_vars.append(self.pddl_vars)
            # print(">>>>>>.",lista)
            if len(lista) == 1:
                self.lista_pddl_vars = []
                self.lista_pddl_vars.append(lista[0])
                # print(">>BBBB>>>:",self.lista_pddl_vars)

            else:
                self.lista_pddl_vars = []
                self.lista_pddl_vars.append(lista)
                # print(">>AAAAA>>>:",self.lista_pddl_vars)
            self.cleanPDDLvars()

    def dealWithActionPredicates(self):
        # print("PRED>>",self.lista_predicados)
        self.lista_action_predicados.append(self.lista_predicados)
        # print("TOTPRED<>",self.lista_action_predicados)
        self.lista_predicados = []

    def dealWithPreconditions(self):
        lista = []
        lista = self.lista_pddl_vars[1:] # tira a lista de parameters
        # lista.append(self.pddl_vars)
        # lista = self.lista_pddl_vars.append(self.pddl_vars)
        # print(">>>>>>:",lista)
        # print(self.lista_pddl_vars)
        # self.lista_pddl_vars = []
        # self.lista_pddl_vars.append(lista)
        # print(self.lista_pddl_vars)
        lista2 = []
        lista2.append(self.lista_pddl_vars[0])
        lista2.append(lista)
        self.lista_pddl_vars = lista2
        # print("LOGIC>>",self.curLogicalOperator)
        self.dealWithActionPredicates()

    def dealWithEffects(self):
        lista = []
        lista = self.lista_pddl_vars[2:] # tira a lista de parameters e lista precond
        # lista.append(self.pddl_vars)
        # lista = self.lista_pddl_vars.append(self.pddl_vars)
        # print(">>>>>>.",lista)
        # print("hihi:",self.lista_pddl_vars)
        lista2 = self.lista_pddl_vars[:2]
        lista2.append(lista)
        self.lista_pddl_vars = lista2
        # print("hihi:",self.lista_pddl_vars)
        self.lista_types.reverse()

        self.dealWithActionPredicates()
        self.dealWithAction()

    def getDomainName(self):
        return self.domain_name

    def getPredicados(self):
        return self.lista_predicados

    def getTypes(self):
        return self.lista_types

    def printDomainInfo(self):
        print("\n\n\n")
        print("Domain Name:")
        print("\t", self.domain_name)
        print("Predicates:")
        # for item in self.domain_predicates:
        #     print(item)
        print("\t", *self.domain_predicates, sep = "\n\t") 
        print("Types:")
        print("\t", self.domain_types)
        print("Constants:")
        print("\t", self.dict_constants)
        print("Functions:")
        print("\t",self.lista_pddl_func)
        print("\n",self.domain_functions)
        print("Actions:")
        self.lista_actions.reverse()
        print("\t",self.lista_actions)
        # print(self.lista_pddl_vars_sep)
        # print(self.lista_pddl_vars)
        # print(self.lista_types)
        # print(self.pddl_vars)

        print(self.domain_actions)


