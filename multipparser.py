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

class PDDLAction:
    def __init__(self):
        self.name = ""
        self.parameters = {}
        self.preconditions = {}
        self.effects = {}
    
    def __str__(self):
        return self.name + "\n\t" + str(self.parameters) + "\n\t" + str(self.preconditions) + "\n\t" + str(self.effects) + "\n"

    def __repr__(self):
        return self.name + "\n\t" + str(self.parameters) + "\n\t" + str(self.preconditions) + "\n\t" + str(self.effects) + "\n"

class PDDLDomain:
    def __init__(self, domain_name="", lista_predicados=[], 
                lista_types=[], dict_constants={}, pddl_ids=[], 
                dealing_with_types=[], lista_pddl_ids=[]):
        self.domain_name = domain_name
        self.lista_predicados = lista_predicados
        self.domain_predicates = [] # lista de PDDLPredicate()
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

        self.lista_actions = []
        self.domain_actions = [] # lista de PDDLAction()

        self.lista_action_predicados = []

        self.curLogicalOperator = ""

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

        # print("\n>>>",self.lista_pddl_vars_sep)
        # print("\n>>",self.dealing_with_types_sep)

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

    def appendPredicado(self,predicado):
        self.lista_predicados.append(predicado)

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
        self.cleanTypes()

    def cleanTypes(self):
        self.lista_types = []

    def dealWithActionLogicPredicate(self):
        for indx_action_predicado in range (0,2):
            last_predicado = self.lista_action_predicados[indx_action_predicado][-1]
            last_predicado = last_predicado.split("*")
            self.lista_action_predicados[indx_action_predicado][-1] = last_predicado[-1]
            last_predicado = last_predicado[:-1]
            print(indx_action_predicado,"LAST_PREDICADO>>>",last_predicado)
            len_action_pred = len(self.lista_action_predicados[indx_action_predicado]) - 1
            for logic_operator in last_predicado:
                op = logic_operator[0]
                num = int(logic_operator[1:])
                print("pre",op,num)
                for i in range(0,num):
                    self.lista_action_predicados[indx_action_predicado][len_action_pred - i] = op + self.lista_action_predicados[indx_action_predicado][len_action_pred - i]
            print("pre_predicados:",self.lista_action_predicados[indx_action_predicado])

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

        action = PDDLAction()
        i = 0
        if all(isinstance(n, list) for n in self.lista_pddl_vars[0]):
            for utype in self.lista_types:
                action.parameters[utype] = self.lista_pddl_vars[0][i]
                i = i + 1
        else:
            for utype in self.lista_types:
                action.parameters[utype] = self.lista_pddl_vars[0]
                i = i + 1

        action.parameters = self.lista_pddl_vars[0]
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

    def cleanPDDLids(self):
        self.pddl_ids = []

    def appendVar(self,pddl_var):
        self.pddl_vars.append(pddl_var)

    def appendListaPDDLvars(self):
        self.lista_pddl_vars.append(self.pddl_vars)

    def cleanPDDLvars(self):
        self.pddl_vars = []


    def dealWithParameters(self):
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
        print("LOGIC>>",self.curLogicalOperator)
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

        print("Actions:")
        self.lista_actions.reverse()
        print("\t",self.lista_actions)
        # print(self.lista_pddl_vars_sep)
        # print(self.lista_pddl_vars)
        # print(self.lista_types)
        # print(self.pddl_vars)

        print(self.domain_actions)

# Get the token map
tokens = plex.tokens


# -------------- RULES ----------------
()
def p_programa_1(p):
    '''programa : LPAREN DEFINE domain_formalization RPAREN
    '''
    # {;}
()
def p_programa_2(p):
    '''programa : LPAREN DEFINE problem_formalization RPAREN'''
    # {;}
()
def p_programa_3(p):
    '''programa : strips_formalization'''
    # {;}
()
def p_programa_4(p):
    '''programa : adl_formalization'''
    # {;}
()
def p_programa_5(p):
    '''programa : LPAREN DOMAIN RPAREN'''

def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOI")

()
def p_adl_formalization_1(p):
    '''adl_formalization : adl_initial_state adl_goal_state adl_actions_def'''
    # {;}
def p_adl_formalization_bad(p):
    '''adl_initial_state : error adl_goal_state adl_actions_def'''
    print("MALFORMED STATEMENT AT LINE %s" % p[1])
    p[0] = None
    p.parser.error = 1

()
def p_adl_initial_state_1(p):
    '''adl_initial_state : INIT LPAREN adl_lista_predicados RPAREN'''
    # {;}
()
def p_initial_state_bad(p):
    '''adl_initial_state : INIT error adl_lista_predicados RPAREN'''
    print("MALFORMED STATEMENT AT LINE %s" % p[1])
    p[0] = None
    p.parser.error = 1

def p_adl_lista_predicados_1(p):
    '''adl_lista_predicados : adl_strips_predicado'''
    # {;}
()
def p_adl_lista_predicados_2(p):
    '''adl_lista_predicados : adl_strips_predicado AND adl_lista_predicados'''
    # {;}
()
def p_adl_goal_state_1(p):
    '''adl_goal_state : GOAL LPAREN adl_lista_predicados RPAREN'''
    # {;}
()
def p_adl_actions_def_1(p):
    '''adl_actions_def : adl_action'''
    # {;}
()
def p_adl_actions_def_2(p):
    '''adl_actions_def : adl_action adl_actions_def'''
    # {;}
()
def p_adl_action_1(p):
    '''adl_action : ACTION LPAREN ID LPAREN adl_lista_parametros RPAREN COMMA adl_precond adl_effect RPAREN'''
    # {;}
()
def p_adl_lista_parametros_1(p):
    '''adl_lista_parametros : adl_parametro'''
    # {;}
()
def p_adl_lista_parametros_2(p):
    '''adl_lista_parametros : adl_parametro COMMA adl_lista_parametros'''
    # {;}
()
def p_adl_parametro_1(p):
    '''adl_parametro : ID COLON lista_ids'''
    # {;}
()
def p_adl_precond_1(p):
    '''adl_precond : PRECOND COLON adl_lista_predicados'''
()
def p_adl_effect_1(p):
    '''adl_effect : EFFECT COLON adl_lista_predicados'''
()
def p_strips_formalization_1(p):
    '''strips_formalization : strips_initial_state strips_goal_state strips_actions_def'''
    # {;}
()
def p_strips_initial_state_1(p):
    '''strips_initial_state : INITS STATE COLON strips_lista_predicados'''
    # {;}
()
def p_strips_lista_predicados_1(p):
    '''strips_lista_predicados : adl_strips_predicado'''
    # {;}
()
def p_strips_lista_predicados_2(p):
    '''strips_lista_predicados : adl_strips_predicado COMMA strips_lista_predicados'''
    # {;}
()
def p_adl_strips_predicado_1(p):
    '''adl_strips_predicado : ID LPAREN adl_strips_lista_ids RPAREN'''
    # {;}
()
def p_adl_strips_predicado_2(p):
    '''adl_strips_predicado : AND ID LPAREN adl_strips_lista_ids RPAREN'''
    # {;}
()
def p_adl_strips_lista_ids_1(p):
    '''adl_strips_lista_ids : ID'''
    # {;}
()
def p_adl_strips_lista_ids_2(p):
    '''adl_strips_lista_ids : ID COMMA adl_strips_lista_ids'''
    # {;}
()
def p_strips_goal_state_1(p):
    '''strips_goal_state : GOAL STATE COLON strips_lista_predicados'''
    # {;}
()
def p_strips_actions_def_1(p):
    '''strips_actions_def : '''
()
def p_strips_actions_def_2(p):
    '''strips_actions_def : ACTIONS COLON strips_lista_actions'''
    # {;}
()
def p_strips_lista_actions_1(p):
    '''strips_lista_actions : strips_action'''
    # {;}
()
def p_strips_lista_actions_2(p):
    '''strips_lista_actions : strips_action strips_lista_actions'''
    # {;}
()
def p_strips_action_1(p):
    '''strips_action : adl_strips_predicado PRECONDITIONS COLON strips_lista_predicados EFFECT COLON strips_lista_predicados'''
    # {;}
()
def p_problem_formalization_1(p):
    '''problem_formalization : def_problem def_domain_p def_objects def_init def_goal'''
    # {;}
()
def p_def_problem_1(p):
    '''def_problem : LPAREN PROBLEM ID RPAREN'''
    # {;}
()
def p_def_domain_p_1(p):
    '''def_domain_p : LPAREN COLON DOMAIN ID RPAREN'''
    # {;}
()
def p_def_objects_1(p):
    '''def_objects : LPAREN COLON OBJECTS lista_objects RPAREN'''
    # {;}
()
def p_lista_objects_1(p):
    '''lista_objects : '''
()
def p_lista_objects_2(p):
    '''lista_objects : lista_ids MINUS ID lista_objects'''
    # {;}
()
def p_lista_objects_3(p):
    '''lista_objects : lista_ids'''
    # {;}
()
def p_def_init_1(p):
    '''def_init : LPAREN COLON INIT lista_predicados_p RPAREN'''
    # {;}
()
def p_def_goal_1(p):
    '''def_goal : '''
()
def p_def_goal_2(p):
    '''def_goal : LPAREN COLON GOAL LPAREN AND lista_predicados_p RPAREN RPAREN
                  '''
    # {;}
def p_def_goal_5(p):
    '''def_goal : LPAREN COLON GOAL LPAREN NOT lista_predicados_p RPAREN RPAREN'''
    # {;}
()
def p_def_goal_3(p):
    '''def_goal : LPAREN COLON GOAL COLON AGENT agent_def COLON CONDITION lista_predicados_p RPAREN'''
    # {;}
()
def p_def_goal_4(p):
    '''def_goal : LPAREN COLON GOAL RPAREN'''
    # {;}
()
def p_lista_predicados_p_1(p):
    '''lista_predicados_p : '''
()
def p_lista_predicados_p_2(p):
    '''lista_predicados_p : LPAREN lista_ids RPAREN lista_predicados_p'''
    # {;}
()
def p_lista_predicados_p_3(p):
    '''lista_predicados_p : LPAREN AND lista_predicados_p RPAREN lista_predicados_p'''
    # {;}
def p_lista_predicados_p_6(p):
    '''lista_predicados_p : LPAREN NOT lista_predicados_p RPAREN lista_predicados_p'''
    # {;}

()
def p_lista_predicados_p_4(p):
    '''lista_predicados_p : LPAREN COMP LPAREN lista_ids RPAREN NUM RPAREN lista_predicados_p'''
    # {;}
()
def p_lista_predicados_p_5(p):
    '''lista_predicados_p : LPAREN COMP LPAREN lista_ids RPAREN ID RPAREN lista_predicados_p'''
    # {;}
()
# def p_lista_predicados_p_6(p):
#     '''lista_predicados_p : LPAREN AT NUM ID RPAREN lista_predicados_p'''
#     # {;}
# ()
def p_domain_formalization_1(p):
    '''domain_formalization : def_domain def_requirements def_types def_constants def_predicates def_functions def_actions'''
    # {;}
()
def p_domain_formalization_2(p):
    '''domain_formalization : def_domain def_requirements def_types def_predicates def_actions'''
    # {;}
()
def p_domain_formalization_3(p):
    '''domain_formalization : def_domain def_requirements def_types def_predicates def_functions def_actions'''
    # {;}
()
def p_domain_formalization_4(p):
    '''domain_formalization : def_domain def_requirements def_types def_constants def_predicates def_actions'''
    # {;}
()
def p_domain_formalization_5(p):
    '''domain_formalization : def_domain def_requirements def_predicates def_actions'''
    # {;}
()
def p_def_domain_1(p):
    '''def_domain : LPAREN DOMAIN ID RPAREN'''
    # {;}
    objDomain.setDomainName(p[3])
()
def p_def_requirements_1(p):
    '''def_requirements : '''
()
def p_def_requirements_2(p):
    '''def_requirements : LPAREN COLON REQUIREMENTS lista_requirements RPAREN'''
    # {;}
()
def p_lista_requirements_1(p):
    '''lista_requirements : '''
()
def p_lista_requirements_2(p):
    '''lista_requirements : COLON ID lista_requirements'''
    # {;}
()
def p_def_types_1(p):
    '''def_types : '''
()
def p_def_types_2(p):
    '''def_types : LPAREN COLON TYPES lista_types RPAREN'''
    # {;}
()
# CHECK TALVEZ TIRE
def p_def_types_3(p):
    '''def_types : LPAREN COLON TYPES lista_types MINUS ID RPAREN'''
    # {;}
()
def p_lista_types_1(p):
    '''lista_types : '''
()
def p_lista_types_2(p):
    '''lista_types : ID lista_types'''
    # {;}
    objDomain.appendType(p[1])
()
def p_def_constants_1(p):
    '''def_constants : '''
()
def p_def_constants_2(p):
    '''def_constants : LPAREN COLON CONSTANTS lista_constants RPAREN'''
    # {;}
()
def p_lista_constants_1(p):
    '''lista_constants : '''

()
def p_lista_constants_2(p):
    '''lista_constants : lista_ids MINUS ID lista_constants'''
    # {;}
    if objDomain.pddl_ids:
        objDomain.appendListaPDDLids()
    objDomain.cleanPDDLids()
    objDomain.dealingWithType(p[3])
    objDomain.appendConstants()

def p_def_predicates_1(p):
    '''def_predicates : '''
()
def p_def_predicates_2(p):
    '''def_predicates : LPAREN COLON PREDICATES lista_predicates RPAREN'''
    # {;}
    # print(objDomain.lista_predicados) # predicates completo
    objDomain.setDomainPredicates()

()
def p_lista_predicates_1(p):
    '''lista_predicates : '''
    # print(objDomain.lista_predicados)

()
def p_lista_predicates_2(p):
    '''lista_predicates : LPAREN ID p_def RPAREN lista_predicates'''
    # {;}
    objDomain.appendPredicado(p[2])
    if objDomain.dealing_with_types:
        objDomain.dealingWithTypeSep()

    # print(objDomain.lista_predicados)
    # print(objDomain.dealing_with_types)
    # print(objDomain.lista_pddl_vars)

()
# def p_p_def_1(p):
#     '''p_def : lista_var MINUS ID'''
#     # {;}
#     if objDomain.pddl_vars:
#         objDomain.appendListaPDDLvars()
#     objDomain.cleanPDDLvars()
#     objDomain.dealingWithType(p[3])

()
def p_p_def_1(p):
    '''p_def : lista_var MINUS ID p_def'''
    # {;}
    # if objDomain.pddl_vars:
    objDomain.appendListaPDDLvars()

    objDomain.cleanPDDLvars()
    objDomain.dealingWithType(p[3])

    # print(p[3])

()
def p_p_def_2(p):
    '''p_def : lista_var'''
    # {;}
    objDomain.dealingWithTypeSep()
    objDomain.appendListaPDDLPredVars()
    objDomain.cleanListaPDDLvars()
()
def p_def_functions_1(p):
    '''def_functions : '''
()
def p_def_functions_2(p):
    '''def_functions : LPAREN COLON FUNCTIONS lista_functions RPAREN'''
()
def p_lista_functions_1(p):
    '''lista_functions : '''
()
def p_lista_functions_2(p):
    '''lista_functions : function lista_functions'''
    # {;}
()
def p_function_1(p):
    '''function : LPAREN ID VAR ID MINUS ID RPAREN'''
    # {;}
()
def p_function_2(p):
    '''function : LPAREN ID RPAREN'''
    # {;}
()
def p_def_actions_1(p):
    '''def_actions : '''
()
def p_def_actions_2(p):
    '''def_actions : LPAREN COLON ACTION ID a_def RPAREN def_actions'''
    # {;}
    objDomain.lista_actions.append(p[4])
    # objDomain.dealWithAction(p[4])
    objDomain.setDomainActions(p[4])
()
def p_def_actions_3(p):
    '''def_actions : LPAREN COLON ACTION ID COLON AGENT agent_def a_def RPAREN def_actions'''
    # {;}

()
def p_agent_def_1(p):
    '''agent_def : ID'''
    # {;}
()
def p_agent_def_2(p):
    '''agent_def : VAR ID'''
    # {;}
()
def p_agent_def_3(p):
    '''agent_def : VAR ID MINUS ID'''
    # {;}
()
def p_a_def_1(p):
    '''a_def : '''
()
def p_a_def_2(p):
    '''a_def : COLON PARAMETERS LPAREN lista_parameters RPAREN COLON PRECONDITION pddl_preconditions COLON EFFECT pddl_effects'''
    # {;}

()
def p_pddl_preconditions_1(p):
    '''pddl_preconditions : lista_preds_op'''
    objDomain.dealWithPreconditions()


def p_pddl_effects_1(p):
    '''pddl_effects : lista_preds_op '''
    objDomain.dealWithEffects()
()
def p_lista_parameters_1(p):
    '''lista_parameters : '''
    # print("<<<############",objDomain.lista_pddl_vars)
    objDomain.dealWithParameters()

    # objDomain.cleanListaPDDLvars()
()
def p_lista_parameters_2(p):
    '''lista_parameters : VAR ID MINUS ID lista_parameters'''
    # {;}
    # objDomain.lista_pddl_vars.append(p[2])
    # print(objDomain.pddl_vars)
    # print(objDomain.lista_pddl_vars)
    # objDomain.cleanListaPDDLvars()
    objDomain.appendType(p[4])
    # print("<<<############",objDomain.lista_pddl_vars)

    objDomain.appendVar(p[2])
    objDomain.dealWithParameters()





()
def p_lista_parameters_3(p):
    '''lista_parameters : lista_var MINUS ID lista_parameters'''
    # {;}
    # print(objDomain.pddl_vars)
    # print(objDomain.lista_pddl_vars)
    # objDomain.cleanListaPDDLvars()
    objDomain.appendType(p[3])
    # print("<<<############",objDomain.lista_pddl_vars)

()
def p_lista_preds_op_1(p):
    '''lista_preds_op : '''
()
def p_lista_preds_op_2(p):
    '''lista_preds_op : lista_predicados lista_preds_op'''
    # {;}
    # print("<<<<<<<<<FINAL_LOGIC>>>>",objDomain.curLogicalOperator)
()
def p_lista_preds_op_3(p):
    '''lista_preds_op : LPAREN AND lista_preds_op RPAREN lista_preds_op'''
    # {;}
    # objDomain.appendPredicado(p[2])
    # if objDomain.dealing_with_types:
    #     objDomain.dealingWithTypeSep()
    objDomain.curLogicalOperator = "AND"
    # objDomain.lista_predicados.append("AND")
    print("\t\tAND>>>>",objDomain.lista_predicados)
    objDomain.lista_predicados[0] = "&" + str(len(objDomain.lista_predicados)) + "*" + objDomain.lista_predicados[0]
def p_lista_preds_op_9(p):
    '''lista_preds_op : LPAREN NOT lista_preds_op RPAREN lista_preds_op'''
    # {;}
    objDomain.curLogicalOperator = "NOT"
    # objDomain.lista_predicados.append("AND")
    print("\t\tNOT>>>>",objDomain.lista_predicados)
    objDomain.lista_predicados[0] = "!" + str(len(objDomain.lista_predicados)) + "*" +objDomain.lista_predicados[0]
()
def p_lista_preds_op_4(p):
    '''lista_preds_op : LPAREN FORALL lista_preds_op RPAREN lista_preds_op'''
    # {;}
()
def p_lista_preds_op_5(p):
    '''lista_preds_op : LPAREN EXISTS lista_preds_op RPAREN lista_preds_op'''
    # {;}
()
def p_lista_preds_op_6(p):
    '''lista_preds_op : LPAREN IMPLY lista_preds_op RPAREN lista_preds_op'''
    # {;}
()
def p_lista_preds_op_7(p):
    '''lista_preds_op : LPAREN PREFERENCE '[' ID ']' RPAREN lista_preds_op'''
    # {;}
()
def p_lista_preds_op_8(p):
    '''lista_preds_op : LPAREN WHEN lista_preds_op RPAREN lista_preds_op'''
    # {;}
()
def p_lista_predicados_1(p):
    '''lista_predicados : LPAREN ID lista_var RPAREN lista_preds_op'''
    # {;}
    # print(p[2])
    # print(objDomain.lista_pddl_vars)
    # print(">>>",objDomain.pddl_vars)

    # if objDomain.pddl_vars:
    objDomain.appendListaPDDLvars()
    objDomain.cleanPDDLvars()


    objDomain.appendPredicado(p[2])
    # if objDomain.dealing_with_types:
    #     objDomain.dealingWithTypeSep()

()
def p_lista_predicados_2(p):
    '''lista_predicados : LPAREN lista_var MINUS ID RPAREN lista_preds_op'''
    # {;}
()
def p_lista_predicados_3(p):
    '''lista_predicados : LPAREN COMP lista_var RPAREN lista_preds_op'''
    # {;}
()
def p_lista_predicados_4(p):
    '''lista_predicados : LPAREN VAR ID COMP ID RPAREN lista_preds_op'''
    # {;}
()
def p_lista_predicados_5(p):
    '''lista_predicados : LPAREN DECREASE LPAREN ID RPAREN NUM RPAREN'''
    # {;}
()
def p_lista_var_1(p):
    '''lista_var : '''
    # print(">>kekekekekekeke>",objDomain.pddl_vars)
    # if objDomain.pddl_vars:
    objDomain.appendListaPDDLvars()
    objDomain.cleanPDDLvars()

()
def p_lista_var_2(p):
    '''lista_var : VAR ID lista_var'''
    # {;}
    # print(">",p[2])
    # print(">>>jajajajjajajajaj>>",objDomain.pddl_vars)
    objDomain.appendVar(p[2])
()
def p_lista_var_3(p):
    '''lista_var : ID lista_var'''
    # {;}
    objDomain.appendVar(p[0])
()
def p_lista_ids_1(p):
    '''lista_ids : '''
    # {;}
    if objDomain.pddl_ids:
        objDomain.appendListaPDDLids()
    objDomain.cleanPDDLids()


()
def p_lista_ids_2(p):
    '''lista_ids : ID lista_ids'''
    # {;}
    objDomain.appendPDDLid(p[1])

()
# -------------- RULES END ----------------
# 
# 
# 
# 
# void yyerror (const char *s) /* chamada por yyparse durante erro*/
# {
#     printf("%s line %d\n", s, yylineno);
# }
# 
# int main (int argc, char *argv[]) 
# {
# 	int result = 0;
# 
# 	yydebug = 0;
# 	yyin = fopen(argv[1], "r");
# 
# 	result = yyparse();
# 	if(result)
# 		printf("Programa com erro sintatico!\n");
# 	else
# 		printf("Formalizacao %s sintaticamente correta!\n",argv[1]);
# 	
# 	return result;
# }
# 
# 
# 

import lex
import yacc
pparser = yacc.yacc()
objDomain = PDDLDomain()

def parse(data):
    pparser.error = 0
    p = pparser.parse(data)
    if pparser.error:
        return False

    objDomain.printDomainInfo()

    return True

# data = open(sys.argv[1]).read()
# prog = parser.parse(data)
# if not prog:
#     raise SystemExit


#yacc.yacc(method='LALR',write_tables=False,debug=False)

# while True:
#     try:
#         s = input("IN > ")
#     except EOFError:
#         break
#     # s = "init(at(c1,sfo))goal(at(c1,sfo))action(load(c:cargo),precond:at(c,p)effect:at(c,a))"
#     parser.parse(s)


# with open('p1.adl', 'r') as myfile:
#     data=myfile.read()

# parser.parse(data)

