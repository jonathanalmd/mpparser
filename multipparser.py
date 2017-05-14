import sys
import yacc 
import lex
import plex
import pddldomain
import pddlproblem
import adl
import strips
import errorhandler


class mlpParser:
    def __init__(self):
        self.pddlDomain = None #class PDDLDomain()
        self.pddlProblem = None #class PDDLProblem()
        self.adl = None # class ADLInfo()
        self.strips = None #class StripsInfo()

    def __str__(self):
        return "\nPDDL:\nPDDL Domain:" + str(self.pddlDomain) + \
        "\nPDDL Problem:" + str(self.pddlProblem) + \
        "\n\nSTRIPS:" + str(self.strips) + \
        "\n\nADL:" + str(self.adl) + "\n"

    def __repr__(self):
        return "\nPDDL:\nPDDL Domain:" + str(self.pddlDomain) + \
        "\nPDDL Problem:" + str(self.pddlProblem) + \
        "\n\nSTRIPS:" + str(self.strips) + \
        "\n\nADL:" + str(self.adl) + "\n"
        
    def setPDDL(self, domain, problem):
        self.pddlDomain = domain
        self.pddlProblem = problem

    def setSTRIPS(self, strips):
        self.strips = strips

    def setADL(self, adl):
        self.adl = adl


    def getPDDL(self):
        return self.pddlDomain, self.pddlProblem 


    def getPDDLDomain(self):
        # PDDLDomain() class (pddldomain.py)
        return self.pddlDomain

    def getPDDLDomainName(self):
        # string
        return self.pddlDomain.getName()

    def getPDDLDomainPredicates(self): 
        # list of PDDLPredicate Class (pddldomain.py)
        # [pred_name {'type':[var1,var2], 'type2':[var1,var2]}, pred_name2 {'type3':[var1,var2]}]
        return self.pddlDomain.getPredicates()

    def getPDDLDomainTypes(self):
        # list of strings
        # [type1, type2, type3]
        return self.pddlDomain.getTypes()

    def getPDDLDomainConstants(self):
        # dictionary
        # {'type' : [constant1, constant2], 'type2' : [constant3]}
        return self.pddlDomain.getConstants()

    def getPDDLDomainFunctions(self):
        # list of PDDLFunction class (pddldomain.py)
        # ['' '' {'':['']}]
        # [string string {string:list of strings}]
        # [function_name function type {'type':[var1,var2]}]
        return self.pddlDomain.getFunctions()

    def getPDDLDomainActions(self):
        # list of PDDLActions class (pddldomain.py)
        return self.pddlDomain.getActions()


    def getPDDLProblem(self):
        # PDDLProblem() class (pddlproblem.py)
        return self.pddlProblem

    def getPDDLProblemName(self):
        # string
        return self.pddlProblem.getName()

    def getPDDLProblemDomain(self):
        # string
        return self.pddlProblem.getProblemDomain()

    def getPDDLProblemObjects(self):
        # dictionary
        # {'type':[var1,var2], 'type2':[var1]}
        return self.pddlProblem.getObjects()

    def getPDDLProblemInit(self):
        # list of PDDLProblemPredicate class (pddlproblem.py)
        # string list of strings
        # pred_name ['var1','var2']
        return self.pddlProblem.getInit()

    def getPDDLProblemGoal(self):
        # list of PDDLProblemPredicate class (pddlproblem.py)
        # string list of strings
        # pred_name ['var1','var2']
        return self.pddlProblem.getGoal()


    def getSTRIPS(self):
        # StripsInfo() class (strips.py)
        return self.strips

    def getSTRIPSInitialState(self):
        # list of strings and lists of strings
        # predicate name1,list of vars from predicate name1, predicate name2, list of vars from predicate name2 ...
        # ['pred_name1',['var1', 'var2'],'pred_name2',['var1']]
        return self.strips.getInitialState()

    def getSTRIPSGoalState(self):
        # list of strings and lists of strings
        # predicate name1,list of vars from predicate name1, predicate name2, list of vars from predicate name2 ...
        # ['pred_name1',['var1', 'var2'],'pred_name2',['var1']]
        return self.strips.getGoalState()

    def getSTRIPSActions(self):
        # list of StripsAction() class (strips.py)
        # [string, list of strings, list of strings and lists of strings, list of strings and lists of strings]
        # [action_name, ['param1','param2'], ['predicate_precondition1',['var1','var2']], ['predicate_effect1',['var1']]]
        return self.strips.getActions()



    def getADL(self):
        # ADLInfo() class (adl.py)
        return self.adl

    def getADLInitialState(self):
        # list of strings and lists of strings
        # predicate name1,list of vars from predicate name1, predicate name2, list of vars from predicate name2 ...
        # ['pred_name1',['var1', 'var2'],'pred_name2',['var1']]
        return self.adl.getInitialState()

    def getADLGoalState(self):
        # list of strings and lists of strings
        # predicate name1,list of vars from predicate name1, predicate name2, list of vars from predicate name2 ...
        # ['pred_name1',['var1', 'var2'],'pred_name2',['var1']]
        return self.adl.getGoalState()

    def getADLActions(self):
        # list of ADLAction() class (adl.py)
        # string {string:list of strings} [predicate name1,list of vars from predicate name1, predicate name2, list of vars from predicate name2]
        # action_name {type : [var1,var2,va3], type2 : [var1,var2]} ['pred_name1',['var1', 'var2'],'pred_name2',['var1']] ['pred_name_effect1',['var1', 'var2'],'pred_name_effect2',['var1']]
        return self.adl.getActions()







# Get the token map
tokens = plex.tokens


# ========================================== RULES ================================================ #

# ========================================= MAIN RULES ============================================ #

def p_programa_1(p):
    '''programa : LPAREN DEFINE domain_formalization RPAREN
    '''

def p_programa_2(p):
    '''programa : LPAREN DEFINE problem_formalization RPAREN'''

def p_programa_3(p):
    '''programa : strips_formalization'''

def p_programa_4(p):
    '''programa : adl_formalization'''


# ======================================= END MAIN RULES ======================================== #



# =============================================================================================== #
# ========================================== ADL ================================================ #
# =============================================================================================== #


def p_adl_formalization_1(p):
    '''adl_formalization : adl_initial_state adl_goal_state adl_actions_def'''

def p_adl_formalization_bad(p):
    '''adl_initial_state : error adl_goal_state adl_actions_def'''
    print("MALFORMED STATEMENT AT LINE %s" % p[1])
    p[0] = None
    p.parser.error = 1


def p_adl_initial_state_1(p):
    '''adl_initial_state : INIT LPAREN adl_lista_predicados RPAREN'''

def p_initial_state_bad(p):
    '''adl_initial_state : INIT error adl_lista_predicados RPAREN'''
    print("MALFORMED STATEMENT AT %s LINE %d" %(p[1],plex.lexer.lineno))
    p[0] = None
    p.parser.error = 1


def p_adl_lista_predicados_1(p):
    '''adl_lista_predicados : adl_predicado'''
    # print ("<PRED>",objADL.lista_predicados)
    # print (">>>>>>",objADL.lista_ids_sep)
    objADL.setPredicates()

    objADL.dealingwith+=1
    objADL.cleanListPreds()
    objADL.cleanListIds()

def p_adl_lista_predicados_2(p):
    '''adl_lista_predicados : adl_predicado AND adl_lista_predicados'''


def p_adl_goal_state_1(p):
    '''adl_goal_state : GOAL LPAREN adl_lista_predicados RPAREN'''


def p_adl_actions_def_1(p):
    '''adl_actions_def : adl_action'''

    objADL.setADLActions()

def p_adl_actions_def_2(p):
    '''adl_actions_def : adl_action adl_actions_def'''

def p_adl_action_1(p):
    '''adl_action : ACTION LPAREN ID LPAREN adl_params RPAREN COMMA adl_precond adl_effect RPAREN'''
    # print(objADL.action_params)
    # print(objADL.action_p_types)
    objADL.appendListActionParam()
    objADL.appendActionName(p[3])

def p_adl_action_2(p):
    '''adl_action : ACTION LPAREN ID LPAREN RPAREN COMMA adl_precond adl_effect RPAREN'''
    # print(objADL.action_params)
    # print(objADL.action_p_types)
    objADL.appendListActionParam()
    objADL.appendActionName(p[3])

def p_adl_params_1(p):
    '''adl_params : ID COLON adl_parametro COMMA adl_params'''

    objADL.appendActionParam(p[1])

def p_adl_params_2(p):
    '''adl_params : ID COLON adl_parametro'''

    objADL.appendActionParam(p[1])

def p_adl_parametro_1(p):
    '''adl_parametro : ID'''

    objADL.appendActionParamType(p[1])





def p_adl_precond_1(p):
    '''adl_precond : PRECOND COLON adl_lista_predicados'''

def p_adl_effect_1(p):
    '''adl_effect : EFFECT COLON adl_lista_predicados'''


def p_adl_predicado_1(p):
    '''adl_predicado : ID LPAREN adl_lista_ids RPAREN'''

    objADL.appendPredicado(p[1])
    objADL.appendListIds()
    # print (objADL.lista_ids_sep)

def p_adl_predicado_2(p):
    '''adl_predicado : AND ID LPAREN adl_lista_ids RPAREN'''

    objADL.appendPredicado(p[2])

def p_adl_predicado_3(p):
    ''' adl_predicado : ID LPAREN RPAREN'''

    objADL.appendPredicado(p[1])
    objADL.appendListIds()

def p_adl_predicado_4(p):
    ''' adl_predicado : AND ID LPAREN RPAREN'''

    objADL.appendPredicado("!"+p[2])
    objADL.appendListIds()

def p_adl_predicado_5(p):
    '''adl_predicado : LNOT ID LPAREN adl_lista_ids RPAREN'''

    objADL.appendPredicado("!"+p[2])
    objADL.appendListIds()
    # print (objADL.lista_ids_sep)

def p_adl_predicado_6(p):
    '''adl_predicado : AND LNOT ID LPAREN adl_lista_ids RPAREN'''

    objADL.appendPredicado("!"+p[3])

def p_adl_predicado_7(p):
    ''' adl_predicado : LNOT ID LPAREN RPAREN'''

    objADL.appendPredicado("!"+p[2])
    objADL.appendListIds()

def p_adl_predicado_8(p):
    ''' adl_predicado : AND LNOT ID LPAREN RPAREN'''

    objADL.appendPredicado("!"+p[3])
    objADL.appendListIds()


def p_adl_lista_ids_1(p):
    '''adl_lista_ids : ID'''

    objADL.appendId(p[1])
    
def p_adl_lista_ids_2(p):
    '''adl_lista_ids : ID COMMA adl_lista_ids'''

    objADL.appendId(p[1])

# =================================================================================================== #
# =========================================== END ADL =============================================== #
# =================================================================================================== #




# =================================================================================================== #
# =========================================== STRIPS ================================================ #
# =================================================================================================== #


def p_strips_formalization_1(p):
    '''strips_formalization : strips_initial_state strips_goal_state strips_actions_def'''

def p_strips_initial_state_1(p):
    '''strips_initial_state : INITIAL STATE COLON strips_lista_predicados'''
    
    errorhandler.linestrips = plex.lexer.lineno


def p_strips_lista_predicados_1(p):
    '''strips_lista_predicados : strips_predicado'''

    # print("\t",objStrips.lista_ids_sep)
    objStrips.dealWithPredicates()

def p_strips_lista_predicados_2(p):
    '''strips_lista_predicados : strips_predicado COMMA strips_lista_predicados'''
    errorhandler.linestrips = plex.lexer.lineno

def p_strips_predicado_1(p):
    '''strips_predicado : ID LPAREN strips_lista_ids RPAREN'''

    objStrips.appendPredName(p[1])
    # print("\t",objStrips.lista_ids_sep)
    objStrips.appendListIds()

def p_strips_predicado_2(p):
    '''strips_predicado : LNOT ID LPAREN strips_lista_ids RPAREN'''

    objStrips.appendPredName("!"+p[2])
    # print("\t",objStrips.lista_ids_sep)
    objStrips.appendListIds()

def p_strips_predicado_3(p):
    '''strips_predicado : ID LPAREN  RPAREN'''

    objStrips.appendPredName(p[1])
    # print("\t",objStrips.lista_ids_sep)
    objStrips.appendListIds()

def p_strips_predicado_4(p):
    '''strips_predicado : LNOT ID LPAREN  RPAREN'''

    objStrips.appendPredName("!"+p[2])
    # print("\t",objStrips.lista_ids_sep)
    objStrips.appendListIds()


def p_strips_lista_ids_1(p):
    '''strips_lista_ids : ID'''
    # print(">",p[1])
    objStrips.appendId(p[1])

def p_strips_lista_ids_2(p):
    '''strips_lista_ids : ID COMMA strips_lista_ids'''
    # print(p[1])
    objStrips.appendId(p[1])


def p_strips_goal_state_1(p):
    '''strips_goal_state : GOAL STATE COLON strips_lista_predicados'''

def p_strips_actions_def_1(p):
    '''strips_actions_def : '''

def p_strips_actions_def_2(p):
    '''strips_actions_def : ACTIONS COLON strips_lista_actions'''


def p_strips_lista_actions_1(p):
    '''strips_lista_actions : strips_action'''

def p_strips_lista_actions_2(p):
    '''strips_lista_actions : strips_action strips_lista_actions'''


def p_strips_action_1(p):
    '''strips_action : strips_predicado PRECONDITIONS COLON strips_lista_predicados EFFECT COLON strips_lista_predicados'''

# =================================================================================================== #
# ========================================= END STRIPS ============================================== #
# =================================================================================================== #





# =================================================================================================== #
# =================================================================================================== #
# ============================================ PDDL ================================================= #
# =================================================================================================== #
# =================================================================================================== #


# =================================================================================================== #
# ========================================== PROBLEM ================================================ #
# =================================================================================================== #

def p_problem_formalization_1(p):
    '''problem_formalization : def_problem def_domain_p def_objects def_init def_goal
                                | def_problem def_domain_p def_init def_goal
    '''
    unused_objects = objProblem.getUnusedObjects()
    # print("U>",unused_predicates,defined_predicates,used_predicates)
    if unused_objects:
        print("WARNING: Unused objects in problem definition (defined but not used): ",unused_objects)

def p_def_problem_1(p):
    '''def_problem : LPAREN PROBLEM ID RPAREN'''
    
    objProblem.setProblemName(p[3])

def p_def_domain_p_1(p):
    '''def_domain_p : LPAREN COLON DOMAIN ID RPAREN'''
    
    if p[4] != objDomain.domain_name:
        errorhandler.reportError(["]"+p[4],objDomain.domain_name])
    objProblem.setProblemDomain(p[4])

def p_def_objects_1(p):
    '''def_objects : LPAREN COLON OBJECTS lista_objects RPAREN'''
    
    if objProblem.lista_ids:
        objProblem.appendListIds()
    objProblem.setProblemObjects()
    objProblem.cleanProblemIds()

def p_lista_objects_1(p):
    '''lista_objects : '''
def p_lista_objects_2(p):
    '''lista_objects : lista_objids_p MINUS ID lista_objects'''
    
    if ("TYPING" in objDomain.domain_requirements) and (p[3] in objDomain.domain_types):
        objProblem.appendObjType(p[3])
    else:
        errorhandler.reportError("?"+p[3])


def p_lista_objects_3(p):
    '''lista_objects : lista_objids_p'''

def p_def_init_1(p):
    '''def_init : LPAREN COLON INIT lista_predicados_p RPAREN'''

    objProblem.setProblemPredicates("i","none")

def p_def_goal_1(p):
    '''def_goal : '''

def p_def_goal_2(p):
    '''def_goal : LPAREN COLON GOAL LPAREN AND lista_predicados_p RPAREN RPAREN'''

    objProblem.setProblemPredicates("g","and")

def p_def_goal_6(p):
    '''def_goal : LPAREN COLON GOAL LPAREN OR lista_predicados_or_p RPAREN RPAREN'''

    objProblem.setProblemPredicates("g","or")

def p_def_goal_5(p):
    '''def_goal : LPAREN COLON GOAL LPAREN NOT lista_predicados_p RPAREN RPAREN'''

def p_def_goal_3(p):
    '''def_goal : LPAREN COLON GOAL COLON AGENT agent_def COLON CONDITION lista_predicados_p RPAREN'''

def p_def_goal_4(p):
    '''def_goal : LPAREN COLON GOAL RPAREN'''


def p_lista_predicados_or_p_1(p):
    '''lista_predicados_or_p : '''

def p_lista_predicados_or_p_2(p):
    '''lista_predicados_or_p : LPAREN lista_ids_p RPAREN lista_predicados_p'''

    if objProblem.lista_ids:
        objProblem.appendListIds()
    # objProblem.setProblemObjects()
    objProblem.cleanProblemIds()

def p_lista_predicados_p_1(p):
    '''lista_predicados_p : '''

def p_lista_predicados_p_2(p):
    '''lista_predicados_p : LPAREN lista_ids_p RPAREN lista_predicados_p'''

    if objProblem.lista_ids:
        objProblem.appendListIds()
    # objProblem.setProblemObjects()
    objProblem.cleanProblemIds()

def p_lista_predicados_p_3(p):
    '''lista_predicados_p : LPAREN NOT lista_not_preds_p RPAREN lista_predicados_p'''

    # if objProblem.lista_ids:
    #     objProblem.appendListIds()
    # print(objProblem.lista_ids_sep)
    # # objProblem.setProblemObjects()
    # objProblem.cleanProblemIds()
    

def p_lista_not_preds_p_1(p):
    ''' lista_not_preds_p : '''
    

def p_lista_not_preds_p_2(p):
    ''' lista_not_preds_p : LPAREN lista_ids_not_p RPAREN lista_not_preds_p'''
    
def p_lista_ids_not_p_1(p):
    ''' lista_ids_not_p : '''

    # print(objProblem.lista_ids)
    if objProblem.lista_ids:
        objProblem.appendListIds()
    # print(objProblem.lista_obj_type)
    # print(objProblem.lista_ids_sep)
    # objProblem.setProblemObjects()
    objProblem.cleanProblemIds()
   
def p_lista_ids_not_p_2(p):
    ''' lista_ids_not_p : ID lista_ids_not_p'''

    if "NEGATIVE-PRECONDITIONS" in objDomain.domain_requirements:
        objProblem.appendId("!"+p[1])
    else:
        errorhandler.reportError("!"+p[1])


def p_lista_objids_p_1(p):
    '''lista_objids_p : '''

    if objProblem.lista_ids:
        objProblem.appendListIds()
        objProblem.cleanProblemIds()

def p_lista_objids_p_2(p):
    '''lista_objids_p : ID lista_objids_p'''

    if p[1] in objProblem.lista_ids:
        errorhandler.reportError("o*"+p[1])
    else:
        objProblem.appendId(p[1])



def p_lista_ids_p_1(p):
    '''lista_ids_p : '''
    # print(objProblem.lista_ids)
    if objProblem.lista_ids:
        objProblem.appendListIds()
        objProblem.cleanProblemIds()

def p_lista_ids_p_2(p):
    '''lista_ids_p : ID lista_ids_p'''
    # print(p[1])
    objProblem.appendId(p[1])

def p_lista_ids_p_5(p):
    '''lista_ids_p : COMP LPAREN ID lista_ids_p RPAREN NUM'''
 
    # objProblem.lista_ids.insert(0,"=")
    # objProblem.lista_ids.insert(1,p[3])
    objProblem.appendId(p[3])
    objProblem.appendId("=")
    objProblem.lista_ids.insert(0,str(p[6]))
    # print(objProblem.lista_ids)

def p_lista_ids_p_6(p):
    '''lista_ids_p : COMP LPAREN ID lista_ids_p RPAREN ID'''

    # objProblem.lista_ids.insert(0,"=")
    # objProblem.lista_ids.insert(1,p[3])
    objProblem.appendId(p[3])
    objProblem.appendId("=")
    objProblem.lista_ids.insert(0,p[6])
    # print(objProblem.lista_ids)

# =================================================================================================== #
# ========================================== END PROBLEM ============================================ #
# =================================================================================================== #



# =================================================================================================== #
# ========================================== DOMAIN ================================================= #
# =================================================================================================== #

def p_domain_formalization_1(p):
    '''domain_formalization : def_domain def_requirements def_types def_constants def_predicates def_functions def_actions'''
    unused_predicates = objDomain.getUnusedPredicates()
    if unused_predicates:
        print("\nWARNING: Unused predicates in domain definition (defined but not used): ",unused_predicates)
    
def p_domain_formalization_2(p):
    '''domain_formalization : def_domain def_requirements def_types def_predicates def_actions'''
    unused_predicates = objDomain.getUnusedPredicates()
    if unused_predicates:
        print("\nWARNING: Unused predicates in domain definition (defined but not used): ",unused_predicates)

def p_domain_formalization_3(p):
    '''domain_formalization : def_domain def_requirements def_types def_predicates def_functions def_actions'''
    unused_predicates = objDomain.getUnusedPredicates()
    if unused_predicates:
        print("\nWARNING: Unused predicates in domain definition (defined but not used): ",unused_predicates)

def p_domain_formalization_4(p):
    '''domain_formalization : def_domain def_requirements def_types def_constants def_predicates def_actions'''
    unused_predicates = objDomain.getUnusedPredicates()
    if unused_predicates:
        print("\nWARNING: Unused predicates in domain definition (defined but not used): ",unused_predicates)

def p_domain_formalization_5(p):
    '''domain_formalization : def_domain def_requirements def_predicates def_actions'''
    unused_predicates = objDomain.getUnusedPredicates()
    if unused_predicates:
        print("\nWARNING: Unused predicates in domain definition (defined but not used): ",unused_predicates)

def p_domain_formalization_6(p):
    '''domain_formalization : def_domain def_requirements def_predicates def_functions def_actions'''
    unused_predicates = objDomain.getUnusedPredicates()
    if unused_predicates:
        print("\nWARNING: Unused predicates in domain definition (defined but not used): ",unused_predicates)


def p_def_domain_1(p):
    '''def_domain : LPAREN DOMAIN ID RPAREN'''
    
    objDomain.setDomainName(p[3])


def p_def_requirements_1(p):
    '''def_requirements : LPAREN COLON REQUIREMENTS lista_requirements RPAREN'''
    # print("\n\t",objDomain.domain_requirements)

def p_lista_requirements_1(p):
    '''lista_requirements : '''

def p_lista_requirements_2(p):
    '''lista_requirements : COLON ID lista_requirements'''
    
    objDomain.domain_requirements.append(p[2].upper())

def p_def_types_1(p):
    '''def_types : LPAREN COLON TYPES lista_types RPAREN'''

def p_def_types_2(p):
    '''def_types : LPAREN COLON TYPES lista_types MINUS ID RPAREN'''

def p_lista_types_1(p):
    '''lista_types : '''

def p_lista_types_2(p):
    '''lista_types : ID lista_types'''
    
    if "TYPING" in objDomain.domain_requirements:
        if p[1] in objDomain.lista_types:
            errorhandler.reportError("t*"+p[1])
        else:
            objDomain.appendType(p[1])
    else:
        errorhandler.reportError("@"+p[1])

def p_def_constants_1(p):
    '''def_constants : LPAREN COLON CONSTANTS lista_constants RPAREN'''
    objDomain.appendConstants()


def p_lista_constants_1(p):
    '''lista_constants : '''


def p_lista_constants_2(p):
    '''lista_constants : lista_ids MINUS ID lista_constants'''

    if objDomain.pddl_ids:
        if len(objDomain.pddl_ids) != len(set(objDomain.pddl_ids)):
            errorhandler.reportError("c*")
        else:
            objDomain.appendListaPDDLids()
    objDomain.cleanPDDLids()
    if "TYPING" in objDomain.domain_requirements:
        objDomain.dealingWithType(p[3])
    else:    
        errorhandler.reportError("@"+p[3])

    
def p_lista_constants_3(p): # catch error dsd
    '''lista_constants : lista_ids MINUS ID lista_ids
                        | lista_ids'''

    errorhandler.reportError("const-typed")


def p_def_predicates_1(p):
    '''def_predicates : '''

def p_def_predicates_2(p):
    '''def_predicates : LPAREN COLON PREDICATES lista_predicates RPAREN'''
    # print(objDomain.lista_predicados) # predicates completo
    if len(objDomain.lista_predicados) != len(set(objDomain.lista_predicados)):
        # predicado com nome repetido
        errorhandler.reportError("*"+p[3])

    objDomain.setDomainPredicates()

def p_lista_predicates_1(p):
    '''lista_predicates : '''
    # print(objDomain.lista_predicados)

def p_lista_predicates_2(p):
    '''lista_predicates : LPAREN ID p_def RPAREN lista_predicates'''
    objDomain.appendPredicado(p[2])
    
    if objDomain.dealing_with_types:
        if "TYPING" in objDomain.domain_requirements:
            objDomain.dealingWithTypeSep()
        else:
            errorhandler.reportError("@"+p[2])

    # print(objDomain.lista_predicados)
    # print(objDomain.dealing_with_types)
    # print(objDomain.lista_pddl_vars)

def p_p_def_1(p):
    '''p_def : lista_var MINUS ID p_def'''
    # if objDomain.pddl_vars:
    objDomain.appendListaPDDLvars()

    objDomain.cleanPDDLvars()
    if ("TYPING" in objDomain.domain_requirements) and (p[3] in objDomain.domain_types):
        objDomain.dealingWithType(p[3])
    else:
        errorhandler.reportError("?"+p[3])

def p_p_def_2(p):
    '''p_def : lista_var'''

    objDomain.appendListaPDDLvars()
    objDomain.cleanPDDLvars()

    objDomain.dealingWithTypeSep()
    objDomain.appendListaPDDLPredVars()
    objDomain.cleanListaPDDLvars()


def p_def_functions_1(p):
    '''def_functions : LPAREN COLON FUNCTIONS lista_functions_def RPAREN'''
    
    if len(objDomain.lista_pddl_func) !=  len(set(objDomain.lista_pddl_func)):
        errorhandler.reportError("f*")
    objDomain.dealWithFunctionDef()
    objDomain.cleanPDDLvars() # clean antes de dealWithActions    
    objDomain.cleanListaPDDLvars()
    objDomain.cleanTypes()

def p_lista_functions_def_1(p):
    '''lista_functions_def : '''
    
    objDomain.lista_pddl_vars.append(objDomain.pddl_vars) # last vars 

def p_lista_functions_def_2(p):
    '''lista_functions_def : LPAREN ID lista_var MINUS ID RPAREN lista_functions_def'''

    objDomain.appendFunction(p[2])
    if "TYPING" in objDomain.domain_requirements:
        objDomain.appendType(p[5])
        objDomain.appendFuncType("(NOTYPE)")
    else:
        errorhandler.reportError("@"+p[5])
    

def p_lista_functions_def_3(p):
    '''lista_functions_def : LPAREN ID RPAREN lista_functions_def'''

    objDomain.appendFunction("0"+p[2])
    objDomain.appendType("(NOTYPE)")
    objDomain.appendFuncType("(NOTYPE)")


def p_lista_functions_def_4(p):
    '''lista_functions_def : LPAREN ID lista_var MINUS ID RPAREN MINUS ID lista_functions_def'''

    objDomain.appendFunction(p[2])
    objDomain.appendType(p[5])
    objDomain.appendFuncType(p[8])

def p_lista_functions_def_5(p):
    '''lista_functions_def : LPAREN ID RPAREN MINUS ID lista_functions_def'''

    objDomain.appendFunction("0"+p[2])
    # objDomain.lista_pddl_vars.append(["NULL"])
    objDomain.appendType("(NOTYPE)")
    objDomain.appendFuncType(p[5])

def p_def_actions_1(p):
    '''def_actions : '''

def p_def_actions_2(p):
    '''def_actions : LPAREN COLON ACTION ID a_def RPAREN def_actions'''
    
    if p[4] in objDomain.lista_actions:
        errorhandler.reportError(">"+p[4])

    objDomain.lista_actions.append(p[4])
    # objDomain.dealWithAction(p[4])
    objDomain.setDomainActions(p[4])

def p_def_actions_3(p):
    '''def_actions : LPAREN COLON ACTION ID COLON AGENT agent_def a_def RPAREN def_actions'''

def p_agent_def_1(p):
    '''agent_def : ID'''

def p_agent_def_2(p):
    '''agent_def : VAR ID'''

def p_agent_def_3(p):
    '''agent_def : VAR ID MINUS ID'''

def p_a_def_1(p):
    '''a_def : '''

def p_a_def_2(p):
    '''a_def : COLON PARAMETERS LPAREN lista_parameters RPAREN COLON PRECONDITION pddl_preconditions COLON EFFECT pddl_effects
            | COLON PARAMETERS LPAREN RPAREN COLON PRECONDITION pddl_preconditions COLON EFFECT pddl_effects
    '''


def p_pddl_preconditions_1(p):
    '''pddl_preconditions : lista_preds_op'''
    objDomain.dealWithPreconditions()

def p_pddl_effects_1(p):
    '''pddl_effects : lista_preds_op '''
    objDomain.dealWithEffects()

def p_lista_parameters_1(p):
    '''lista_parameters : '''
    # print("<<<############",objDomain.lista_pddl_vars)
    objDomain.dealWithParameters()

    # objDomain.cleanListaPDDLvars()


def p_lista_parameters_2(p):
    '''lista_parameters : lista_var MINUS ID lista_parameters'''
    # objDomain.cleanListaPDDLvars()
    if ("TYPING" in objDomain.domain_requirements) and (p[3] in objDomain.domain_types):
        objDomain.appendType(p[3])
    else:
        errorhandler.reportError("?"+p[3])

def p_lista_parameters_3(p):
    '''lista_parameters : lista_var '''

    objDomain.dealWithParameters()

def p_lista_preds_op_1(p):
    '''lista_preds_op : '''

def p_lista_preds_op_2(p):
    '''lista_preds_op : lista_predicados lista_preds_op'''
    # print("<<<<<<<<<FINAL_LOGIC>>>>",objDomain.curLogicalOperator)

def p_lista_preds_op_3(p):
    '''lista_preds_op : LPAREN AND lista_preds_op RPAREN '''
 
    objDomain.lista_predicados[0] = "&" + str(len(objDomain.lista_predicados)) + "*" + objDomain.lista_predicados[0]


def p_lista_preds_op_4(p):
    '''lista_preds_op : LPAREN FORALL lista_preds_op RPAREN '''

def p_lista_preds_op_5(p):
    '''lista_preds_op : LPAREN EXISTS lista_preds_op RPAREN '''

def p_lista_preds_op_6(p):
    '''lista_preds_op : LPAREN IMPLY lista_preds_op RPAREN '''

def p_lista_preds_op_7(p):
    '''lista_preds_op : LPAREN PREFERENCE '[' ID ']' RPAREN '''

def p_lista_preds_op_8(p):
    '''lista_preds_op : LPAREN WHEN lista_preds_op RPAREN'''


def p_lista_predicados_0(p):
    ''' lista_predicados : '''

def p_lista_predicados_1(p):
    '''lista_predicados : LPAREN ID lista_var RPAREN lista_preds_op'''

    if objDomain.pddl_vars:
        objDomain.appendListaPDDLvars()
    # else:
    #     # objDomain.pddl_vars = ["(NOVdAR)"]
    #     objDomain.appendListaPDDLvars()

    objDomain.cleanPDDLvars()

    if p[2] in [pred_name.name for pred_name in objDomain.domain_predicates]:
        objDomain.appendPredicado(p[2])
    else:
        errorhandler.reportError("#"+p[2])

    # if objDomain.dealing_with_types:
    #     objDomain.dealingWithTypeSep()

def p_lista_predicados_2(p):
    '''lista_predicados : LPAREN lista_var MINUS ID RPAREN lista_preds_op'''

def p_lista_predicados_3(p):
    '''lista_predicados : LPAREN COMP lista_var RPAREN lista_preds_op'''

def p_lista_predicados_4(p):
    '''lista_predicados : LPAREN VAR ID COMP ID RPAREN lista_preds_op'''

def p_lista_predicados_5(p):
    '''lista_predicados : LPAREN DECREASE LPAREN ID RPAREN NUM RPAREN'''

def p_lista_predicados_6(p):
    '''lista_predicados : LPAREN ID RPAREN lista_predicados '''
    # print(">>ID",p[2])
    objDomain.appendListaPDDLvars()
    objDomain.cleanPDDLvars()
    objDomain.appendVar(p[2])
    # objDomain.appendVar("(NOVAR)")
    objDomain.appendListaPDDLvars()

    if p[2] in [pred_name.name for pred_name in objDomain.domain_predicates]:
        objDomain.appendPredicado(p[2])
    else:
        errorhandler.reportError("#"+p[2])

    objDomain.cleanPDDLvars()

def p_lista_predicados_7(p):
    '''lista_predicados : LPAREN NOT lista_predicados_not RPAREN ''' 
    # objDomain.lista_predicados.append("AND")
    # print("\t\tNOT>>>>",objDomain.lista_predicados)


def p_lista_predicados_not_1(p):
    ''' lista_predicados_not : '''

def p_lista_predicados_not_2(p):
    ''' lista_predicados_not : LPAREN ID RPAREN lista_predicados_not'''
    objDomain.appendListaPDDLvars()
    objDomain.cleanPDDLvars()
    objDomain.appendVar(p[2])

    objDomain.appendListaPDDLvars()
    objDomain.appendPredicado("!"+p[2])
    objDomain.cleanPDDLvars()

def p_lista_predicados_not_3(p):
    '''lista_predicados_not : LPAREN ID lista_var RPAREN lista_predicados_not'''

    if objDomain.pddl_vars:
        objDomain.appendListaPDDLvars()

    objDomain.cleanPDDLvars()
    objDomain.appendPredicado("!"+p[2])

def p_lista_var_1(p):
    '''lista_var : '''
 
    if objDomain.pddl_vars:
        objDomain.appendListaPDDLvars()
        objDomain.cleanPDDLvars()

def p_lista_var_2(p):
    '''lista_var : VAR ID lista_var'''

    if p[2] in objDomain.pddl_vars:
        errorhandler.reportError("vp*"+p[2]) # var repetida
    else:
        objDomain.appendVar(p[2])

def p_lista_var_3(p):
    '''lista_var : ID lista_var'''
    
    objDomain.appendVar(p[0])

def p_lista_ids_1(p):
    '''lista_ids : '''
    
    if objDomain.pddl_ids:
        objDomain.appendListaPDDLids()
    objDomain.cleanPDDLids()

def p_lista_ids_2(p):
    '''lista_ids : ID lista_ids'''
    
    objDomain.appendPDDLid(p[1])

# =================================================================================================== #
# =========================================== FIM DOMAIN ============================================ #
# =================================================================================================== #

# =================================================================================================== #
# =================================================================================================== #
# ============================================ FIM PDDL ============================================= #
# =================================================================================================== #
# =================================================================================================== #

def p_error(p):
    # print("Syntax error in %s line %d"%(p.value,plex.lexer.lineno))
    if p != None:
        errorhandler.reportError(p.value)
    else:
        errorhandler.reportError("(")

pparser = yacc.yacc()
objDomain = pddldomain.PDDLDomainParse()
objProblem = pddlproblem.PDDLProblemParse()
objADL = adl.ADLFormParse()
objStrips = strips.StripsFormParse()


def parse(pmode, filelist):
    if pmode == "pddl":

        domain_f = open(filelist[0]).read()
        problem_f = open(filelist[1]).read()

        errorhandler.run_mode = "pddldomain"
        p = pparser.parse(domain_f)
        plex.lexer.lineno = 0
        errorhandler.run_mode = "pddlproblem"
        p = pparser.parse(problem_f)

        # objDomain.printDomainInfo()
        # objProblem.printProblemInfo()

        
        # print("U>",unused_predicates,defined_predicates,used_predicates)
        

        return objDomain.getPDDLDomain(), objProblem.getPDDLProblem()

    elif pmode == "adl":
        adl_f = open(filelist[0]).read()

        errorhandler.run_mode = "adl"
        p = pparser.parse(adl_f)
       
        # objADL.printADLInfo()
        return objADL.getADL()

    else: # strips
        strips_f = open(filelist[0]).read()

        errorhandler.run_mode = "strips"
        p = pparser.parse(strips_f)

        # objStrips.printStripsInfo()
        return objStrips.getStrips() # return obj
