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
import pddldomain
import pddlproblem

# Get the token map
tokens = plex.tokens


# -------------- RULES ----------------
()
def p_programa_1(p):
    '''programa : LPAREN DEFINE domain_formalization RPAREN
    '''

def p_programa_2(p):
    '''programa : LPAREN DEFINE problem_formalization RPAREN'''

def p_programa_3(p):
    '''programa : strips_formalization'''

def p_programa_4(p):
    '''programa : adl_formalization'''

def p_programa_5(p):
    '''programa : LPAREN DOMAIN RPAREN'''

# def p_error(p):
#     if p:
#         print("Syntax error at '%s'" % p.value)
#     else:
#         print("Syntax error at EOI")

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
    '''adl_lista_predicados : adl_strips_predicado'''

def p_adl_lista_predicados_2(p):
    '''adl_lista_predicados : adl_strips_predicado AND adl_lista_predicados'''

def p_adl_goal_state_1(p):
    '''adl_goal_state : GOAL LPAREN adl_lista_predicados RPAREN'''

def p_adl_actions_def_1(p):
    '''adl_actions_def : adl_action'''

def p_adl_actions_def_2(p):
    '''adl_actions_def : adl_action adl_actions_def'''

def p_adl_action_1(p):
    '''adl_action : ACTION LPAREN ID LPAREN adl_lista_parametros RPAREN COMMA adl_precond adl_effect RPAREN'''

def p_adl_lista_parametros_1(p):
    '''adl_lista_parametros : adl_parametro'''

def p_adl_lista_parametros_2(p):
    '''adl_lista_parametros : adl_parametro COMMA adl_lista_parametros'''

def p_adl_parametro_1(p):
    '''adl_parametro : ID COLON lista_ids'''

def p_adl_precond_1(p):
    '''adl_precond : PRECOND COLON adl_lista_predicados'''

def p_adl_effect_1(p):
    '''adl_effect : EFFECT COLON adl_lista_predicados'''

def p_strips_formalization_1(p):
    '''strips_formalization : strips_initial_state strips_goal_state strips_actions_def'''

def p_strips_initial_state_1(p):
    '''strips_initial_state : INITS STATE COLON strips_lista_predicados'''

def p_strips_lista_predicados_1(p):
    '''strips_lista_predicados : adl_strips_predicado'''

def p_strips_lista_predicados_2(p):
    '''strips_lista_predicados : adl_strips_predicado COMMA strips_lista_predicados'''

def p_adl_strips_predicado_1(p):
    '''adl_strips_predicado : ID LPAREN adl_strips_lista_ids RPAREN'''

def p_adl_strips_predicado_2(p):
    '''adl_strips_predicado : AND ID LPAREN adl_strips_lista_ids RPAREN'''

def p_adl_strips_lista_ids_1(p):
    '''adl_strips_lista_ids : ID'''

def p_adl_strips_lista_ids_2(p):
    '''adl_strips_lista_ids : ID COMMA adl_strips_lista_ids'''

def p_strips_goal_state_1(p):
    '''strips_goal_state : GOAL STATE COLON strips_lista_predicados'''

def p_strips_actions_def_1(p):
    '''strips_actions_def : '''

def p_strips_actions_def_2(p):
    '''strips_actions_def : ACTIONS COLON strips_lista_actions'''
    # {;}
()
def p_strips_lista_actions_1(p):
    '''strips_lista_actions : strips_action'''

def p_strips_lista_actions_2(p):
    '''strips_lista_actions : strips_action strips_lista_actions'''

def p_strips_action_1(p):
    '''strips_action : adl_strips_predicado PRECONDITIONS COLON strips_lista_predicados EFFECT COLON strips_lista_predicados'''






def p_problem_formalization_1(p):
    '''problem_formalization : def_problem def_domain_p def_objects def_init def_goal'''

def p_def_problem_1(p):
    '''def_problem : LPAREN PROBLEM ID RPAREN'''
    objProblem.setProblemName(p[3])
    # print(objProblem.problem_name)

def p_def_domain_p_1(p):
    '''def_domain_p : LPAREN COLON DOMAIN ID RPAREN'''
    objProblem.setProblemDomain(p[4])
    # print(objProblem.problem_domain)

def p_def_objects_1(p):
    '''def_objects : LPAREN COLON OBJECTS lista_objects RPAREN'''
    if objProblem.lista_ids:
        objProblem.appendListIds()
    # print(objProblem.lista_obj_type)
    # print(objProblem.lista_ids_sep)
    objProblem.setProblemObjects()
    objProblem.cleanProblemIds()

def p_lista_objects_1(p):
    '''lista_objects : '''
def p_lista_objects_2(p):
    '''lista_objects : lista_objids_p MINUS ID lista_objects'''
    objProblem.appendObjType(p[3])

def p_lista_objects_3(p):
    '''lista_objects : lista_objids_p'''

def p_def_init_1(p):
    '''def_init : LPAREN COLON INIT lista_predicados_p RPAREN'''
    # print(objProblem.lista_ids_sep)
    objProblem.setProblemInitPredicates()

def p_def_goal_1(p):
    '''def_goal : '''

def p_def_goal_2(p):
    '''def_goal : LPAREN COLON GOAL LPAREN AND lista_predicados_p RPAREN RPAREN'''

def p_def_goal_5(p):
    '''def_goal : LPAREN COLON GOAL LPAREN NOT lista_predicados_p RPAREN RPAREN'''

def p_def_goal_3(p):
    '''def_goal : LPAREN COLON GOAL COLON AGENT agent_def COLON CONDITION lista_predicados_p RPAREN'''

def p_def_goal_4(p):
    '''def_goal : LPAREN COLON GOAL RPAREN'''

def p_lista_predicados_p_1(p):
    '''lista_predicados_p : '''

def p_lista_predicados_p_2(p):
    '''lista_predicados_p : LPAREN lista_ids_p RPAREN lista_predicados_p'''
    # {;}
    if objProblem.lista_ids:
        objProblem.appendListIds()
    # print(objProblem.lista_obj_type)
    # print(objProblem.lista_ids_sep)
    # objProblem.setProblemObjects()
    objProblem.cleanProblemIds()

# def p_lista_predicados_p_3(p):
#     '''lista_predicados_p : LPAREN lista_ids_p RPAREN lista_predicados_op'''

# def p_lista_predicados_p_3(p):
#     '''lista_predicados_p : LPAREN NOT LPAREN lista_ids_p RPAREN RPAREN lista_predicados_p'''
#     print(objProblem.lista_ids_sep)
# def p_lista_predicados_p_4(p):
#     '''lista_predicados_p : LPAREN COMP LPAREN lista_ids_p RPAREN NUM RPAREN lista_predicados_p'''

# def p_lista_predicados_p_3(p):
#     '''lista_predicados_p : lista_predicados_op'''

# def p_lista_predicados_p_2(p):
#     '''lista_predicados_p : LPAREN AND lista_predicados_p RPAREN lista_predicados_p'''


# def p_lista_predicados_op_1(p):
#     '''lista_predicados_op : LPAREN COMP LPAREN lista_ids_p RPAREN NUM RPAREN lista_predicados_p'''
#     if objProblem.lista_ids:
#         objProblem.appendListIds()
#         objProblem.cleanProblemIds()
#     print("<EQUAL>",objProblem.lista_ids_sep)
#     print(p[4])
    
# def p_lista_predicados_op_2(p):
#     '''lista_predicados_op : LPAREN COMP LPAREN lista_ids_p RPAREN ID RPAREN lista_predicados_p'''
#     # print(objProblem.lista_ids_sep)
#     # objProblem.lista_ids_sep[-1].insert(len(objProblem.lista_ids)-1,"=")
#     # objProblem.lista_ids_sep[-1].insert(0,(p[6]))
#     # objProblem.appendListIds()
#     # objProblem.cleanProblemIds()
#     # print(p[4],p[5],p[6],p[7],plex.lexer.lineno)


# def p_lista_predicados_op_3(p):
#     '''lista_predicados_op : LPAREN NOT LPAREN lista_ids_p RPAREN lista_predicados_p RPAREN lista_predicados_p'''
#     if objProblem.lista_ids:
#         objProblem.appendListIds()
#         objProblem.cleanProblemIds()
#     print("<NOT>",objProblem.lista_ids_sep)
#     print(p[4])
    
# # def p_lista_predicados_p_6(p):
# #     '''lista_predicados_p : LPAREN AT NUM ID RPAREN lista_predicados_p'''
# #     # {;}
# # ()
def p_lista_objids_p_1(p):
    '''lista_objids_p : '''
    # print(objProblem.lista_ids)
    if objProblem.lista_ids:
        objProblem.appendListIds()
        objProblem.cleanProblemIds()

def p_lista_objids_p_2(p):
    '''lista_objids_p : ID lista_objids_p'''
    # print(p[1])
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

def p_lista_ids_p_3(p):
    '''lista_ids_p : NOT LPAREN ID lista_ids_p RPAREN '''
    # print(p[1],p[3])
    # print(objProblem.lista_ids)
    # objProblem.lista_ids.insert(0,"!")
    # objProblem.lista_ids.insert(1,p[3])
    objProblem.appendId(p[3])
    objProblem.appendId("!")
    # print(objProblem.lista_ids)

def p_lista_ids_p_4(p):
    '''lista_ids_p : COMP LPAREN ID lista_ids_p RPAREN NUM'''
    # print(objProblem.lista_ids)
    # print(p[1],p[3])
    # objProblem.lista_ids.insert(0,"=")
    # objProblem.lista_ids.insert(1,p[3])
    objProblem.appendId(p[3])
    objProblem.appendId("=")
    objProblem.lista_ids.insert(0,str(p[6]))
    # print(objProblem.lista_ids)

def p_lista_ids_p_5(p):
    '''lista_ids_p : COMP LPAREN ID lista_ids_p RPAREN  ID'''
    # print(objProblem.lista_ids)
    # print(p[1],p[3])
    # objProblem.lista_ids.insert(0,"=")
    # objProblem.lista_ids.insert(1,p[3])
    objProblem.appendId(p[3])
    objProblem.appendId("=")
    objProblem.lista_ids.insert(0,p[6])
    # print(objProblem.lista_ids)



def p_domain_formalization_1(p):
    '''domain_formalization : def_domain def_requirements def_types def_constants def_predicates def_functions def_actions'''

def p_domain_formalization_2(p):
    '''domain_formalization : def_domain def_requirements def_types def_predicates def_actions'''

def p_domain_formalization_3(p):
    '''domain_formalization : def_domain def_requirements def_types def_predicates def_functions def_actions'''

def p_domain_formalization_4(p):
    '''domain_formalization : def_domain def_requirements def_types def_constants def_predicates def_actions'''

def p_domain_formalization_5(p):
    '''domain_formalization : def_domain def_requirements def_predicates def_actions'''

def p_def_domain_1(p):
    '''def_domain : LPAREN DOMAIN ID RPAREN'''
    objDomain.setDomainName(p[3])

def p_def_requirements_1(p):
    '''def_requirements : '''

def p_def_requirements_2(p):
    '''def_requirements : LPAREN COLON REQUIREMENTS lista_requirements RPAREN'''

def p_lista_requirements_1(p):
    '''lista_requirements : '''

def p_lista_requirements_2(p):
    '''lista_requirements : COLON ID lista_requirements'''

def p_def_types_1(p):
    '''def_types : '''

def p_def_types_2(p):
    '''def_types : LPAREN COLON TYPES lista_types RPAREN'''

# CHECK TALVEZ TIRE
def p_def_types_3(p):
    '''def_types : LPAREN COLON TYPES lista_types MINUS ID RPAREN'''

def p_lista_types_1(p):
    '''lista_types : '''

def p_lista_types_2(p):
    '''lista_types : ID lista_types'''
    objDomain.appendType(p[1])

def p_def_constants_1(p):
    '''def_constants : '''

def p_def_constants_2(p):
    '''def_constants : LPAREN COLON CONSTANTS lista_constants RPAREN'''

def p_lista_constants_1(p):
    '''lista_constants : '''

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

def p_def_predicates_2(p):
    '''def_predicates : LPAREN COLON PREDICATES lista_predicates RPAREN'''
    # print(objDomain.lista_predicados) # predicates completo
    objDomain.setDomainPredicates()

def p_lista_predicates_1(p):
    '''lista_predicates : '''
    # print(objDomain.lista_predicados)

def p_lista_predicates_2(p):
    '''lista_predicates : LPAREN ID p_def RPAREN lista_predicates'''
    objDomain.appendPredicado(p[2])
    if objDomain.dealing_with_types:
        objDomain.dealingWithTypeSep()

    # print(objDomain.lista_predicados)
    # print(objDomain.dealing_with_types)
    # print(objDomain.lista_pddl_vars)

# def p_p_def_1(p):
#     '''p_def : lista_var MINUS ID'''
#     # {;}
#     if objDomain.pddl_vars:
#         objDomain.appendListaPDDLvars()
#     objDomain.cleanPDDLvars()
#     objDomain.dealingWithType(p[3])

def p_p_def_1(p):
    '''p_def : lista_var MINUS ID p_def'''
    # if objDomain.pddl_vars:
    objDomain.appendListaPDDLvars()

    objDomain.cleanPDDLvars()
    objDomain.dealingWithType(p[3])

    # print(p[3])

def p_p_def_2(p):
    '''p_def : lista_var'''

    objDomain.appendListaPDDLvars()

    objDomain.dealingWithTypeSep()
    objDomain.appendListaPDDLPredVars()
    objDomain.cleanListaPDDLvars()

def p_def_functions_1(p):
    '''def_functions : '''

def p_def_functions_(p):
    '''def_functions : LPAREN COLON FUNCTIONS lista_functions_def RPAREN'''
    objDomain.dealWithFunctionDef()
    objDomain.cleanPDDLvars() # clean antes de dealWithActions    
    objDomain.cleanListaPDDLvars()
    objDomain.cleanTypes()

def p_lista_functions_def_1(p):
    '''lista_functions_def : '''
    objDomain.lista_pddl_vars.append(objDomain.pddl_vars) # last vars 

def p_lista_functions_def_2(p):
    '''lista_functions_def : LPAREN ID lista_var MINUS ID RPAREN lista_functions_def'''
    # print("Function:",p[2])
    objDomain.appendFunction(p[2])
    objDomain.appendType(p[5])
    objDomain.appendFuncType("(NOTYPE)")

def p_lista_functions_def_3(p):
    '''lista_functions_def : LPAREN ID RPAREN lista_functions_def'''
    # print("Function:",p[2])
    objDomain.appendFunction("0"+p[2])
    objDomain.appendType("(NOTYPE)")
    objDomain.appendFuncType("(NOTYPE)")


def p_lista_functions_def_4(p):
    '''lista_functions_def : LPAREN ID lista_var MINUS ID RPAREN MINUS ID lista_functions_def'''
    # print("Function:",p[2])
    # print("\tvars type:",p[5])
    # print("\tfunc type:",p[8])
    objDomain.appendFunction(p[2])
    objDomain.appendType(p[5])
    objDomain.appendFuncType(p[8])

def p_lista_functions_def_5(p):
    '''lista_functions_def : LPAREN ID RPAREN MINUS ID lista_functions_def'''
    # print("Function:",p[2])
    # print("\tfunc type:",p[5])
    objDomain.appendFunction("0"+p[2])
    # objDomain.lista_pddl_vars.append(["NULL"])
    objDomain.appendType("(NOTYPE)")
    objDomain.appendFuncType(p[5])

def p_def_actions_1(p):
    '''def_actions : '''

def p_def_actions_2(p):
    '''def_actions : LPAREN COLON ACTION ID a_def RPAREN def_actions'''
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
    '''a_def : COLON PARAMETERS LPAREN lista_parameters RPAREN COLON PRECONDITION pddl_preconditions COLON EFFECT pddl_effects'''

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
    '''lista_parameters : VAR ID MINUS ID lista_parameters'''
    # objDomain.lista_pddl_vars.append(p[2])
    # print(objDomain.pddl_vars)
    # print(objDomain.lista_pddl_vars)
    # objDomain.cleanListaPDDLvars()

    objDomain.appendType(p[4])
    # print("<<<############",objDomain.lista_pddl_vars)

    objDomain.appendVar(p[2])

    objDomain.dealWithParameters()

def p_lista_parameters_3(p):
    '''lista_parameters : lista_var MINUS ID lista_parameters'''
    # print(objDomain.pddl_vars)
    # print(objDomain.lista_pddl_vars)
    # objDomain.cleanListaPDDLvars()
    objDomain.appendType(p[3])
    # print("<<<############",objDomain.lista_pddl_vars)

def p_lista_parameters_4(p):
    '''lista_parameters : lista_var '''
    # print(objDomain.pddl_vars)
    # print(objDomain.lista_pddl_vars)
    # objDomain.cleanListaPDDLvars()
    # print("<<<############",objDomain.lista_pddl_vars)

    objDomain.curLineAction = plex.lexer.lineno - 1

    objDomain.dealWithParameters()

def p_lista_preds_op_1(p):
    '''lista_preds_op : '''

def p_lista_preds_op_2(p):
    '''lista_preds_op : lista_predicados'''
    # print("<<<<<<<<<FINAL_LOGIC>>>>",objDomain.curLogicalOperator)

def p_lista_preds_op_3(p):
    '''lista_preds_op : LPAREN AND lista_preds_op RPAREN lista_preds_op'''
    # objDomain.appendPredicado(p[2])
    # if objDomain.dealing_with_types:
    #     objDomain.dealingWithTypeSep()
    objDomain.curLogicalOperator = "AND"
    # objDomain.lista_predicados.append("AND")
    # print("\t\tAND>>>>",objDomain.lista_predicados)
    objDomain.lista_predicados[0] = "&" + str(len(objDomain.lista_predicados)) + "*" + objDomain.lista_predicados[0]

def p_lista_preds_op_9(p):
    '''lista_preds_op : LPAREN NOT lista_predicados RPAREN '''
    objDomain.curLogicalOperator = "NOT"
    # objDomain.lista_predicados.append("AND")
    # print("\t\tNOT>>>>",objDomain.lista_predicados)
    objDomain.lista_predicados[0] = "!" + str(len(objDomain.lista_predicados)) + "*" +objDomain.lista_predicados[0]

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

def p_lista_predicados_1(p):
    '''lista_predicados : LPAREN ID lista_var RPAREN lista_preds_op'''
    # print(p[2])
    # print(objDomain.lista_pddl_vars)
    # print(">>>",objDomain.pddl_vars)

    # if objDomain.pddl_vars:
    objDomain.appendListaPDDLvars()
    objDomain.cleanPDDLvars()


    objDomain.appendPredicado(p[2])
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

def p_lista_var_1(p):
    '''lista_var : '''
    # print(">>kekekekekekeke>",objDomain.pddl_vars)
    # if objDomain.pddl_vars:
    objDomain.appendListaPDDLvars()
    objDomain.cleanPDDLvars()

def p_lista_var_2(p):
    '''lista_var : VAR ID lista_var'''
    # {;}
    # print(">",p[2])
    # print(">>>jajajajjajajajaj>>",objDomain.pddl_vars)
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



def p_error(p):
    if p.value == "(":
        print("Syntax error in line",plex.lexer.lineno-1)
        print("\tMissing or more ')' than expected OR")
        if run_mode == "pddlproblem":
            print("\tUsing more than one predicate inside 'NOT' operator: please apply 'NOT' operator on each predicate individually")
    else:
        print("Syntax error in %s line %d"%(p.value,plex.lexer.lineno))
    sys.exit()




pparser = yacc.yacc()
objDomain = pddldomain.PDDLDomain()
objProblem = pddlproblem.PDDLProblem()

run_mode = "pddlproblem"
def parse(data):
    pparser.error = 0
    p = pparser.parse(data)
    if pparser.error:
        return False
    else:
        # objDomain.printDomainInfo()
        objProblem.printProblemInfo()
        return True
