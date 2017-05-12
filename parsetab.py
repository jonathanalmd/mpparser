
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "DEFINE DOMAIN REQUIREMENTS TYPES CONSTANTS PREDICATES FUNCTIONS ACTION PARAMETERS PRECONDITION EFFECT FORALL EXISTS INCREASE DECREASE ASSIGN IMPLY PREFERENCE WHEN AGENT PROBLEM OBJECTS INIT GOAL CONDITION INITIAL STATE ACTIONS PRECONDITIONS PRECOND AND NOT OR OPERATOR ID NUM MINUS LOR LAND LNOT LT LE GT GE EQ NE VAR LPAREN RPAREN LBRACKET RBRACKET COMMA COLON COMPprograma : LPAREN DEFINE domain_formalization RPAREN\n    programa : LPAREN DEFINE problem_formalization RPARENprograma : strips_formalizationprograma : adl_formalizationprograma : LPAREN DOMAIN RPARENadl_formalization : adl_initial_state adl_goal_state adl_actions_defadl_initial_state : error adl_goal_state adl_actions_defadl_initial_state : INIT LPAREN adl_lista_predicados RPARENadl_initial_state : INIT error adl_lista_predicados RPARENadl_lista_predicados : adl_predicadoadl_lista_predicados : adl_predicado AND adl_lista_predicadosadl_goal_state : GOAL LPAREN adl_lista_predicados RPARENadl_actions_def : adl_actionadl_actions_def : adl_action adl_actions_defadl_action : ACTION LPAREN ID LPAREN adl_params RPAREN COMMA adl_precond adl_effect RPARENadl_action : ACTION LPAREN ID LPAREN RPAREN COMMA adl_precond adl_effect RPARENadl_params : ID COLON adl_parametro COMMA adl_paramsadl_params : ID COLON adl_parametroadl_parametro : IDadl_precond : PRECOND COLON adl_lista_predicadosadl_effect : EFFECT COLON adl_lista_predicadosadl_predicado : ID LPAREN adl_lista_ids RPARENadl_predicado : AND ID LPAREN adl_lista_ids RPAREN adl_predicado : ID LPAREN RPAREN adl_predicado : AND ID LPAREN RPARENadl_predicado : LNOT ID LPAREN adl_lista_ids RPARENadl_predicado : AND LNOT ID LPAREN adl_lista_ids RPAREN adl_predicado : LNOT ID LPAREN RPAREN adl_predicado : AND LNOT ID LPAREN RPARENadl_lista_ids : IDadl_lista_ids : ID COMMA adl_lista_idsstrips_formalization : strips_initial_state strips_goal_state strips_actions_defstrips_initial_state : INITIAL STATE COLON strips_lista_predicadosstrips_lista_predicados : strips_predicadostrips_lista_predicados : strips_predicado COMMA strips_lista_predicadosstrips_predicado : ID LPAREN strips_lista_ids RPARENstrips_predicado : LNOT ID LPAREN strips_lista_ids RPARENstrips_predicado : ID LPAREN  RPARENstrips_predicado : LNOT ID LPAREN  RPARENstrips_lista_ids : IDstrips_lista_ids : ID COMMA strips_lista_idsstrips_goal_state : GOAL STATE COLON strips_lista_predicadosstrips_actions_def : strips_actions_def : ACTIONS COLON strips_lista_actionsstrips_lista_actions : strips_actionstrips_lista_actions : strips_action strips_lista_actionsstrips_action : strips_predicado PRECONDITIONS COLON strips_lista_predicados EFFECT COLON strips_lista_predicadosproblem_formalization : def_problem def_domain_p def_objects def_init def_goal\n                                | def_problem def_domain_p def_init def_goal\n    def_problem : LPAREN PROBLEM ID RPARENdef_domain_p : LPAREN COLON DOMAIN ID RPARENdef_objects : LPAREN COLON OBJECTS lista_objects RPARENlista_objects : lista_objects : lista_objids_p MINUS ID lista_objectslista_objects : lista_objids_pdef_init : LPAREN COLON INIT lista_predicados_p RPARENdef_goal : def_goal : LPAREN COLON GOAL LPAREN AND lista_predicados_p RPAREN RPARENdef_goal : LPAREN COLON GOAL LPAREN OR lista_predicados_or_p RPAREN RPARENdef_goal : LPAREN COLON GOAL LPAREN NOT lista_predicados_p RPAREN RPARENdef_goal : LPAREN COLON GOAL COLON AGENT agent_def COLON CONDITION lista_predicados_p RPARENdef_goal : LPAREN COLON GOAL RPARENlista_predicados_or_p : lista_predicados_or_p : LPAREN lista_ids_p RPAREN lista_predicados_plista_predicados_p : lista_predicados_p : LPAREN lista_ids_p RPAREN lista_predicados_plista_predicados_p : LPAREN NOT lista_not_preds_p RPAREN lista_predicados_p lista_not_preds_p :  lista_not_preds_p : LPAREN lista_ids_not_p RPAREN lista_not_preds_p lista_ids_not_p :  lista_ids_not_p : ID lista_ids_not_plista_objids_p : lista_objids_p : ID lista_objids_plista_ids_p : lista_ids_p : ID lista_ids_plista_ids_p : COMP LPAREN ID lista_ids_p RPAREN NUMlista_ids_p : COMP LPAREN ID lista_ids_p RPAREN IDdomain_formalization : def_domain def_requirements def_types def_constants def_predicates def_functions def_actionsdomain_formalization : def_domain def_requirements def_types def_predicates def_actionsdomain_formalization : def_domain def_requirements def_types def_predicates def_functions def_actionsdomain_formalization : def_domain def_requirements def_types def_constants def_predicates def_actionsdomain_formalization : def_domain def_requirements def_predicates def_actionsdomain_formalization : def_domain def_requirements def_predicates def_functions def_actionsdef_domain : LPAREN DOMAIN ID RPARENdef_requirements : LPAREN COLON REQUIREMENTS lista_requirements RPARENlista_requirements : lista_requirements : COLON ID lista_requirementsdef_types : LPAREN COLON TYPES lista_types RPARENdef_types : LPAREN COLON TYPES lista_types MINUS ID RPARENlista_types : lista_types : ID lista_typesdef_constants : LPAREN COLON CONSTANTS lista_constants RPARENlista_constants : lista_constants : lista_ids MINUS ID lista_constantslista_constants : lista_ids MINUS ID lista_ids\n                        | lista_idsdef_predicates : def_predicates : LPAREN COLON PREDICATES lista_predicates RPARENlista_predicates : lista_predicates : LPAREN ID p_def RPAREN lista_predicatesp_def : lista_var MINUS ID p_defp_def : lista_vardef_functions : LPAREN COLON FUNCTIONS lista_functions_def RPARENlista_functions_def : lista_functions_def : LPAREN ID lista_var MINUS ID RPAREN lista_functions_deflista_functions_def : LPAREN ID RPAREN lista_functions_deflista_functions_def : LPAREN ID lista_var MINUS ID RPAREN MINUS ID lista_functions_deflista_functions_def : LPAREN ID RPAREN MINUS ID lista_functions_defdef_actions : def_actions : LPAREN COLON ACTION ID a_def RPAREN def_actionsdef_actions : LPAREN COLON ACTION ID COLON AGENT agent_def a_def RPAREN def_actionsagent_def : IDagent_def : VAR IDagent_def : VAR ID MINUS IDa_def : a_def : COLON PARAMETERS LPAREN lista_parameters RPAREN COLON PRECONDITION pddl_preconditions COLON EFFECT pddl_effects\n            | COLON PARAMETERS LPAREN RPAREN COLON PRECONDITION pddl_preconditions COLON EFFECT pddl_effects\n    pddl_preconditions : lista_preds_oppddl_effects : lista_preds_op lista_parameters : lista_parameters : lista_var MINUS ID lista_parameterslista_parameters : lista_var lista_preds_op : lista_preds_op : lista_predicados lista_preds_oplista_preds_op : LPAREN AND lista_preds_op RPAREN lista_preds_op : LPAREN FORALL lista_preds_op RPAREN lista_preds_op : LPAREN EXISTS lista_preds_op RPAREN lista_preds_op : LPAREN IMPLY lista_preds_op RPAREN lista_preds_op : LPAREN PREFERENCE '[' ID ']' RPAREN lista_preds_op : LPAREN WHEN lista_preds_op RPAREN lista_predicados : lista_predicados : LPAREN ID lista_var RPAREN lista_preds_oplista_predicados : LPAREN lista_var MINUS ID RPAREN lista_preds_oplista_predicados : LPAREN COMP lista_var RPAREN lista_preds_oplista_predicados : LPAREN VAR ID COMP ID RPAREN lista_preds_oplista_predicados : LPAREN DECREASE LPAREN ID RPAREN NUM RPARENlista_predicados : LPAREN ID RPAREN lista_predicados lista_predicados : LPAREN NOT lista_predicados_not RPAREN  lista_predicados_not :  lista_predicados_not : LPAREN ID RPAREN lista_predicados_notlista_predicados_not : LPAREN ID lista_var RPAREN lista_predicados_notlista_var : lista_var : VAR ID lista_varlista_var : ID lista_varlista_ids : lista_ids : ID lista_ids"
    
_lr_action_items = {'LPAREN':([0,9,10,15,23,24,31,38,45,47,56,60,63,67,68,71,72,79,83,86,91,92,93,94,97,101,122,125,131,138,153,161,167,168,174,190,194,199,203,205,206,213,219,225,226,227,230,243,244,246,247,249,263,288,300,303,306,310,314,323,328,332,334,336,337,338,339,342,346,347,349,358,366,367,368,369,370,371,373,375,376,378,382,387,388,389,392,394,395,396,399,400,401,],[2,18,20,32,46,48,52,62,69,73,82,85,90,95,98,102,104,109,114,117,-84,-50,123,98,128,104,155,128,164,172,128,188,-85,196,-51,-88,-98,-52,231,234,-56,-92,-103,172,253,172,172,274,128,188,-89,164,172,231,188,172,172,128,188,329,329,329,188,329,329,329,329,329,363,364,-124,374,329,329,-125,-126,-127,-128,329,-137,-130,329,-138,-132,329,-134,364,-129,-133,329,364,-135,-136,]),'INITIAL':([0,],[7,]),'error':([0,9,],[8,19,]),'INIT':([0,105,135,],[9,138,138,]),'$end':([1,3,4,12,25,26,29,30,43,44,51,55,75,76,78,107,110,113,145,147,180,265,268,292,],[0,-3,-4,-43,-5,-32,-6,-13,-1,-2,-14,-34,-44,-45,-42,-46,-35,-38,-36,-39,-37,-47,-16,-15,]),'DEFINE':([2,],[10,]),'DOMAIN':([2,20,74,],[11,41,106,]),'GOAL':([5,6,8,30,34,51,54,55,58,64,110,113,136,145,147,180,268,292,],[13,15,15,-13,-7,-14,-33,-34,-8,-9,-35,-38,168,-36,-39,-37,-16,-15,]),'STATE':([7,13,],[16,28,]),'RPAREN':([11,21,22,35,36,40,45,53,62,65,66,67,68,72,82,84,85,87,88,89,90,93,94,96,97,100,101,103,109,111,112,114,115,116,117,119,120,121,122,124,125,127,130,131,133,134,137,138,139,142,146,148,149,150,151,152,153,154,157,158,161,162,163,165,166,167,168,169,170,171,172,173,179,181,182,184,185,186,187,189,190,192,193,194,195,198,201,202,203,204,206,208,209,213,215,217,218,219,220,221,222,223,225,226,227,229,230,231,232,233,238,241,244,246,247,248,249,251,252,253,254,255,257,259,260,261,262,263,264,266,267,271,272,273,274,275,277,279,280,281,282,283,284,285,287,288,289,290,291,293,295,296,298,299,300,301,302,303,304,305,306,308,310,314,315,316,317,318,319,320,321,324,326,327,332,333,334,336,337,338,339,341,342,344,347,349,350,352,353,354,355,357,358,359,361,365,366,367,368,369,370,371,373,375,376,377,378,380,381,382,383,384,385,386,387,388,389,390,392,393,394,395,396,397,398,399,400,401,402,],[25,43,44,58,-10,64,-97,80,89,91,92,-97,-109,-57,113,-11,116,-30,119,-24,121,-97,-109,-82,-109,-86,-57,-49,143,-40,145,147,148,-25,150,-22,152,-28,-109,-79,-109,-83,-90,-99,167,-48,-53,-65,174,177,180,-23,181,-29,-31,-26,-109,-81,-80,-93,-104,190,-90,194,-86,-85,198,199,-55,-72,-74,206,-41,-27,-78,213,-96,-145,-115,219,-88,-91,-142,-98,-87,-62,-73,230,-68,-74,-56,-19,-18,-92,-146,244,246,-103,247,-142,249,-102,-65,-63,-65,-53,-65,-70,263,-75,268,-93,-109,-104,-89,-144,-99,-142,282,-74,284,285,-112,-54,-66,288,-70,-65,-74,-17,292,-95,-94,-115,297,-110,-106,-100,-142,-143,302,303,304,305,-113,-68,-71,-67,309,-21,310,311,-122,314,-104,-101,-58,-65,-59,-60,-65,-69,-109,-104,-108,-64,327,-114,-77,-76,-111,-120,-105,-61,-123,-121,-104,-123,-123,-123,-123,358,-123,-142,-139,-124,-107,368,369,370,371,373,-131,376,378,382,-123,-123,-125,-126,-127,-128,-123,-137,-130,388,-123,391,392,-138,-117,-119,-116,394,-132,-123,-134,396,-139,399,-129,-133,-123,401,-140,-139,-135,-136,-141,]),'ACTIONS':([12,55,78,110,113,145,147,180,],[27,-34,-42,-35,-38,-36,-39,-37,]),'ACTION':([14,17,30,80,129,159,183,268,292,],[31,31,31,-12,160,160,160,-16,-15,]),'COLON':([16,27,28,46,48,69,73,95,98,100,102,104,108,123,128,141,155,166,168,187,207,212,239,256,257,273,287,297,311,318,323,328,330,331,332,335,349,358,368,369,370,371,373,375,376,378,382,387,388,389,394,395,396,400,401,],[33,49,50,70,74,99,105,126,129,132,135,136,140,156,159,176,183,132,197,216,235,240,269,286,-112,294,-113,312,322,-114,-123,-123,348,-118,-123,351,-124,-131,-125,-126,-127,-128,-123,-137,-130,-123,-138,-132,-123,-134,-129,-133,-123,-135,-136,]),'ID':([18,19,32,33,37,39,41,42,49,50,52,55,57,59,61,62,76,81,82,85,90,106,109,110,113,114,117,118,130,132,137,140,144,145,147,158,160,163,164,171,172,176,180,186,188,191,193,200,204,214,218,221,224,228,229,231,234,235,236,240,241,242,250,251,253,258,262,264,265,269,274,276,278,280,307,309,313,324,325,329,341,344,345,356,360,362,363,364,374,379,381,],[38,38,38,56,60,63,65,66,56,56,79,-34,83,38,86,87,56,56,111,87,87,139,141,-35,-38,111,87,87,163,166,171,56,111,-36,-39,186,187,163,193,171,204,208,-37,186,218,220,221,229,204,241,221,221,251,257,171,262,264,56,141,38,186,257,280,221,204,287,262,204,-47,38,221,299,300,221,318,319,324,221,334,341,221,221,362,372,377,221,380,381,341,390,221,]),'AND':([18,19,32,36,59,89,116,119,121,148,150,152,181,196,240,269,329,],[37,37,37,59,37,-24,-25,-22,-28,-23,-29,-26,-27,225,37,37,336,]),'LNOT':([18,19,32,33,37,49,50,55,59,76,81,110,113,140,145,147,180,235,240,265,269,],[39,39,39,57,61,57,57,-34,39,57,57,-35,-38,57,-36,-39,-37,57,39,-47,39,]),'PROBLEM':([20,],[42,]),'EFFECT':([36,55,84,89,110,113,116,119,121,145,147,148,150,152,175,180,181,211,237,270,348,351,],[-10,-34,-11,-24,-35,-38,-25,-22,-28,-36,-39,-23,-29,-26,207,-37,-27,239,239,-20,366,367,]),'COMMA':([55,87,111,113,143,145,147,177,180,208,209,],[81,118,144,-38,178,-36,-39,210,-37,-19,236,]),'REQUIREMENTS':([70,],[100,]),'PRECONDITIONS':([77,113,145,147,180,],[108,-38,-36,-39,-37,]),'TYPES':([99,],[130,]),'PREDICATES':([99,126,156,],[131,131,131,]),'OBJECTS':([105,],[137,]),'CONSTANTS':([126,],[158,]),'FUNCTIONS':([129,183,],[161,161,]),'MINUS':([130,137,158,162,163,170,171,185,186,192,193,201,215,218,221,223,229,241,245,246,248,251,271,274,280,281,287,298,314,324,329,341,343,357,362,374,],[-90,-72,-145,191,-90,200,-72,214,-145,-91,-142,-73,-146,-142,-142,250,-72,-145,276,278,-144,-142,214,-142,-142,-143,307,313,325,-142,-142,-142,360,-144,-142,-142,]),'NOT':([172,196,329,374,],[203,227,347,347,]),'COMP':([172,204,253,264,329,362,374,],[205,205,205,205,344,379,344,]),'PRECOND':([178,210,],[212,212,]),'VAR':([193,218,221,228,242,251,274,280,324,329,341,344,362,374,381,],[224,224,224,258,258,224,224,224,224,345,224,224,224,345,224,]),'OR':([196,],[226,]),'AGENT':([197,216,],[228,242,]),'PARAMETERS':([216,294,],[243,243,]),'CONDITION':([286,],[306,]),'NUM':([309,391,],[320,397,]),'PRECONDITION':([312,322,],[323,328,]),'FORALL':([329,],[337,]),'EXISTS':([329,],[338,]),'IMPLY':([329,],[339,]),'PREFERENCE':([329,],[340,]),'WHEN':([329,],[342,]),'DECREASE':([329,374,],[346,346,]),'[':([340,],[356,]),']':([372,],[386,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'strips_formalization':([0,],[3,]),'adl_formalization':([0,],[4,]),'strips_initial_state':([0,],[5,]),'adl_initial_state':([0,],[6,]),'strips_goal_state':([5,],[12,]),'adl_goal_state':([6,8,],[14,17,]),'domain_formalization':([10,],[21,]),'problem_formalization':([10,],[22,]),'def_domain':([10,],[23,]),'def_problem':([10,],[24,]),'strips_actions_def':([12,],[26,]),'adl_actions_def':([14,17,30,],[29,34,51,]),'adl_action':([14,17,30,],[30,30,30,]),'adl_lista_predicados':([18,19,32,59,240,269,],[35,40,53,84,270,293,]),'adl_predicado':([18,19,32,59,240,269,],[36,36,36,36,36,36,]),'def_requirements':([23,],[45,]),'def_domain_p':([24,],[47,]),'strips_lista_predicados':([33,50,81,140,235,],[54,78,110,175,265,]),'strips_predicado':([33,49,50,76,81,140,235,],[55,77,55,77,55,55,55,]),'def_types':([45,],[67,]),'def_predicates':([45,67,93,],[68,94,122,]),'def_objects':([47,],[71,]),'def_init':([47,71,],[72,101,]),'strips_lista_actions':([49,76,],[75,107,]),'strips_action':([49,76,],[76,76,]),'adl_lista_ids':([62,85,90,117,118,],[88,115,120,149,151,]),'def_constants':([67,],[93,]),'def_actions':([68,94,97,122,125,153,244,310,],[96,124,127,154,157,182,275,321,]),'def_functions':([68,94,122,],[97,125,153,]),'def_goal':([72,101,],[103,134,]),'strips_lista_ids':([82,114,144,],[112,146,179,]),'lista_requirements':([100,166,],[133,195,]),'adl_params':([109,236,],[142,266,]),'lista_types':([130,163,],[162,192,]),'lista_predicates':([131,249,],[165,279,]),'lista_objects':([137,229,],[169,259,]),'lista_objids_p':([137,171,229,],[170,201,170,]),'lista_predicados_p':([138,225,227,230,263,303,306,],[173,252,255,260,290,316,317,]),'lista_constants':([158,241,],[184,272,]),'lista_ids':([158,186,241,],[185,215,271,]),'lista_functions_def':([161,246,300,314,334,],[189,277,315,326,350,]),'lista_ids_p':([172,204,253,264,],[202,233,283,291,]),'adl_parametro':([176,],[209,]),'adl_precond':([178,210,],[211,237,]),'a_def':([187,273,],[217,295,]),'p_def':([193,280,],[222,301,]),'lista_var':([193,218,221,251,274,280,324,329,341,344,362,374,381,],[223,245,248,281,298,223,298,343,357,361,281,343,393,]),'lista_not_preds_p':([203,288,],[232,308,]),'adl_effect':([211,237,],[238,267,]),'lista_predicados_or_p':([226,],[254,]),'agent_def':([228,242,],[256,273,]),'lista_ids_not_p':([231,262,],[261,289,]),'lista_parameters':([274,324,],[296,333,]),'pddl_preconditions':([323,328,],[330,335,]),'lista_preds_op':([323,328,332,336,337,338,339,342,366,367,373,378,388,396,],[331,331,349,352,353,354,355,359,384,384,387,389,395,400,]),'lista_predicados':([323,328,332,336,337,338,339,342,358,366,367,373,378,388,396,],[332,332,332,332,332,332,332,332,375,332,332,332,332,332,332,]),'lista_predicados_not':([347,392,399,],[365,398,402,]),'pddl_effects':([366,367,],[383,385,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> LPAREN DEFINE domain_formalization RPAREN','programa',4,'p_programa_1','multipparser.py',183),
  ('programa -> LPAREN DEFINE problem_formalization RPAREN','programa',4,'p_programa_2','multipparser.py',187),
  ('programa -> strips_formalization','programa',1,'p_programa_3','multipparser.py',190),
  ('programa -> adl_formalization','programa',1,'p_programa_4','multipparser.py',193),
  ('programa -> LPAREN DOMAIN RPAREN','programa',3,'p_programa_5','multipparser.py',196),
  ('adl_formalization -> adl_initial_state adl_goal_state adl_actions_def','adl_formalization',3,'p_adl_formalization_1','multipparser.py',208),
  ('adl_initial_state -> error adl_goal_state adl_actions_def','adl_initial_state',3,'p_adl_formalization_bad','multipparser.py',211),
  ('adl_initial_state -> INIT LPAREN adl_lista_predicados RPAREN','adl_initial_state',4,'p_adl_initial_state_1','multipparser.py',218),
  ('adl_initial_state -> INIT error adl_lista_predicados RPAREN','adl_initial_state',4,'p_initial_state_bad','multipparser.py',221),
  ('adl_lista_predicados -> adl_predicado','adl_lista_predicados',1,'p_adl_lista_predicados_1','multipparser.py',228),
  ('adl_lista_predicados -> adl_predicado AND adl_lista_predicados','adl_lista_predicados',3,'p_adl_lista_predicados_2','multipparser.py',238),
  ('adl_goal_state -> GOAL LPAREN adl_lista_predicados RPAREN','adl_goal_state',4,'p_adl_goal_state_1','multipparser.py',243),
  ('adl_actions_def -> adl_action','adl_actions_def',1,'p_adl_actions_def_1','multipparser.py',247),
  ('adl_actions_def -> adl_action adl_actions_def','adl_actions_def',2,'p_adl_actions_def_2','multipparser.py',251),
  ('adl_action -> ACTION LPAREN ID LPAREN adl_params RPAREN COMMA adl_precond adl_effect RPAREN','adl_action',10,'p_adl_action_1','multipparser.py',254),
  ('adl_action -> ACTION LPAREN ID LPAREN RPAREN COMMA adl_precond adl_effect RPAREN','adl_action',9,'p_adl_action_2','multipparser.py',261),
  ('adl_params -> ID COLON adl_parametro COMMA adl_params','adl_params',5,'p_adl_params_1','multipparser.py',268),
  ('adl_params -> ID COLON adl_parametro','adl_params',3,'p_adl_params_2','multipparser.py',273),
  ('adl_parametro -> ID','adl_parametro',1,'p_adl_parametro_1','multipparser.py',278),
  ('adl_precond -> PRECOND COLON adl_lista_predicados','adl_precond',3,'p_adl_precond_1','multipparser.py',287),
  ('adl_effect -> EFFECT COLON adl_lista_predicados','adl_effect',3,'p_adl_effect_1','multipparser.py',290),
  ('adl_predicado -> ID LPAREN adl_lista_ids RPAREN','adl_predicado',4,'p_adl_predicado_1','multipparser.py',294),
  ('adl_predicado -> AND ID LPAREN adl_lista_ids RPAREN','adl_predicado',5,'p_adl_predicado_2','multipparser.py',300),
  ('adl_predicado -> ID LPAREN RPAREN','adl_predicado',3,'p_adl_predicado_3','multipparser.py',304),
  ('adl_predicado -> AND ID LPAREN RPAREN','adl_predicado',4,'p_adl_predicado_4','multipparser.py',309),
  ('adl_predicado -> LNOT ID LPAREN adl_lista_ids RPAREN','adl_predicado',5,'p_adl_predicado_5','multipparser.py',314),
  ('adl_predicado -> AND LNOT ID LPAREN adl_lista_ids RPAREN','adl_predicado',6,'p_adl_predicado_6','multipparser.py',320),
  ('adl_predicado -> LNOT ID LPAREN RPAREN','adl_predicado',4,'p_adl_predicado_7','multipparser.py',324),
  ('adl_predicado -> AND LNOT ID LPAREN RPAREN','adl_predicado',5,'p_adl_predicado_8','multipparser.py',329),
  ('adl_lista_ids -> ID','adl_lista_ids',1,'p_adl_lista_ids_1','multipparser.py',335),
  ('adl_lista_ids -> ID COMMA adl_lista_ids','adl_lista_ids',3,'p_adl_lista_ids_2','multipparser.py',339),
  ('strips_formalization -> strips_initial_state strips_goal_state strips_actions_def','strips_formalization',3,'p_strips_formalization_1','multipparser.py',355),
  ('strips_initial_state -> INITIAL STATE COLON strips_lista_predicados','strips_initial_state',4,'p_strips_initial_state_1','multipparser.py',358),
  ('strips_lista_predicados -> strips_predicado','strips_lista_predicados',1,'p_strips_lista_predicados_1','multipparser.py',363),
  ('strips_lista_predicados -> strips_predicado COMMA strips_lista_predicados','strips_lista_predicados',3,'p_strips_lista_predicados_2','multipparser.py',369),
  ('strips_predicado -> ID LPAREN strips_lista_ids RPAREN','strips_predicado',4,'p_strips_predicado_1','multipparser.py',373),
  ('strips_predicado -> LNOT ID LPAREN strips_lista_ids RPAREN','strips_predicado',5,'p_strips_predicado_2','multipparser.py',380),
  ('strips_predicado -> ID LPAREN RPAREN','strips_predicado',3,'p_strips_predicado_3','multipparser.py',387),
  ('strips_predicado -> LNOT ID LPAREN RPAREN','strips_predicado',4,'p_strips_predicado_4','multipparser.py',394),
  ('strips_lista_ids -> ID','strips_lista_ids',1,'p_strips_lista_ids_1','multipparser.py',402),
  ('strips_lista_ids -> ID COMMA strips_lista_ids','strips_lista_ids',3,'p_strips_lista_ids_2','multipparser.py',407),
  ('strips_goal_state -> GOAL STATE COLON strips_lista_predicados','strips_goal_state',4,'p_strips_goal_state_1','multipparser.py',414),
  ('strips_actions_def -> <empty>','strips_actions_def',0,'p_strips_actions_def_1','multipparser.py',417),
  ('strips_actions_def -> ACTIONS COLON strips_lista_actions','strips_actions_def',3,'p_strips_actions_def_2','multipparser.py',420),
  ('strips_lista_actions -> strips_action','strips_lista_actions',1,'p_strips_lista_actions_1','multipparser.py',424),
  ('strips_lista_actions -> strips_action strips_lista_actions','strips_lista_actions',2,'p_strips_lista_actions_2','multipparser.py',427),
  ('strips_action -> strips_predicado PRECONDITIONS COLON strips_lista_predicados EFFECT COLON strips_lista_predicados','strips_action',7,'p_strips_action_1','multipparser.py',431),
  ('problem_formalization -> def_problem def_domain_p def_objects def_init def_goal','problem_formalization',5,'p_problem_formalization_1','multipparser.py',453),
  ('problem_formalization -> def_problem def_domain_p def_init def_goal','problem_formalization',4,'p_problem_formalization_1','multipparser.py',454),
  ('def_problem -> LPAREN PROBLEM ID RPAREN','def_problem',4,'p_def_problem_1','multipparser.py',466),
  ('def_domain_p -> LPAREN COLON DOMAIN ID RPAREN','def_domain_p',5,'p_def_domain_p_1','multipparser.py',471),
  ('def_objects -> LPAREN COLON OBJECTS lista_objects RPAREN','def_objects',5,'p_def_objects_1','multipparser.py',478),
  ('lista_objects -> <empty>','lista_objects',0,'p_lista_objects_1','multipparser.py',487),
  ('lista_objects -> lista_objids_p MINUS ID lista_objects','lista_objects',4,'p_lista_objects_2','multipparser.py',489),
  ('lista_objects -> lista_objids_p','lista_objects',1,'p_lista_objects_3','multipparser.py',498),
  ('def_init -> LPAREN COLON INIT lista_predicados_p RPAREN','def_init',5,'p_def_init_1','multipparser.py',501),
  ('def_goal -> <empty>','def_goal',0,'p_def_goal_1','multipparser.py',506),
  ('def_goal -> LPAREN COLON GOAL LPAREN AND lista_predicados_p RPAREN RPAREN','def_goal',8,'p_def_goal_2','multipparser.py',509),
  ('def_goal -> LPAREN COLON GOAL LPAREN OR lista_predicados_or_p RPAREN RPAREN','def_goal',8,'p_def_goal_6','multipparser.py',514),
  ('def_goal -> LPAREN COLON GOAL LPAREN NOT lista_predicados_p RPAREN RPAREN','def_goal',8,'p_def_goal_5','multipparser.py',520),
  ('def_goal -> LPAREN COLON GOAL COLON AGENT agent_def COLON CONDITION lista_predicados_p RPAREN','def_goal',10,'p_def_goal_3','multipparser.py',523),
  ('def_goal -> LPAREN COLON GOAL RPAREN','def_goal',4,'p_def_goal_4','multipparser.py',526),
  ('lista_predicados_or_p -> <empty>','lista_predicados_or_p',0,'p_lista_predicados_or_p_1','multipparser.py',530),
  ('lista_predicados_or_p -> LPAREN lista_ids_p RPAREN lista_predicados_p','lista_predicados_or_p',4,'p_lista_predicados_or_p_2','multipparser.py',533),
  ('lista_predicados_p -> <empty>','lista_predicados_p',0,'p_lista_predicados_p_1','multipparser.py',543),
  ('lista_predicados_p -> LPAREN lista_ids_p RPAREN lista_predicados_p','lista_predicados_p',4,'p_lista_predicados_p_2','multipparser.py',546),
  ('lista_predicados_p -> LPAREN NOT lista_not_preds_p RPAREN lista_predicados_p','lista_predicados_p',5,'p_lista_predicados_p_3','multipparser.py',556),
  ('lista_not_preds_p -> <empty>','lista_not_preds_p',0,'p_lista_not_preds_p_1','multipparser.py',567),
  ('lista_not_preds_p -> LPAREN lista_ids_not_p RPAREN lista_not_preds_p','lista_not_preds_p',4,'p_lista_not_preds_p_2','multipparser.py',571),
  ('lista_ids_not_p -> <empty>','lista_ids_not_p',0,'p_lista_ids_not_p_1','multipparser.py',574),
  ('lista_ids_not_p -> ID lista_ids_not_p','lista_ids_not_p',2,'p_lista_ids_not_p_2','multipparser.py',585),
  ('lista_objids_p -> <empty>','lista_objids_p',0,'p_lista_objids_p_1','multipparser.py',596),
  ('lista_objids_p -> ID lista_objids_p','lista_objids_p',2,'p_lista_objids_p_2','multipparser.py',603),
  ('lista_ids_p -> <empty>','lista_ids_p',0,'p_lista_ids_p_1','multipparser.py',613),
  ('lista_ids_p -> ID lista_ids_p','lista_ids_p',2,'p_lista_ids_p_2','multipparser.py',620),
  ('lista_ids_p -> COMP LPAREN ID lista_ids_p RPAREN NUM','lista_ids_p',6,'p_lista_ids_p_5','multipparser.py',645),
  ('lista_ids_p -> COMP LPAREN ID lista_ids_p RPAREN ID','lista_ids_p',6,'p_lista_ids_p_6','multipparser.py',656),
  ('domain_formalization -> def_domain def_requirements def_types def_constants def_predicates def_functions def_actions','domain_formalization',7,'p_domain_formalization_1','multipparser.py',677),
  ('domain_formalization -> def_domain def_requirements def_types def_predicates def_actions','domain_formalization',5,'p_domain_formalization_2','multipparser.py',683),
  ('domain_formalization -> def_domain def_requirements def_types def_predicates def_functions def_actions','domain_formalization',6,'p_domain_formalization_3','multipparser.py',689),
  ('domain_formalization -> def_domain def_requirements def_types def_constants def_predicates def_actions','domain_formalization',6,'p_domain_formalization_4','multipparser.py',695),
  ('domain_formalization -> def_domain def_requirements def_predicates def_actions','domain_formalization',4,'p_domain_formalization_5','multipparser.py',701),
  ('domain_formalization -> def_domain def_requirements def_predicates def_functions def_actions','domain_formalization',5,'p_domain_formalization_6','multipparser.py',707),
  ('def_domain -> LPAREN DOMAIN ID RPAREN','def_domain',4,'p_def_domain_1','multipparser.py',714),
  ('def_requirements -> LPAREN COLON REQUIREMENTS lista_requirements RPAREN','def_requirements',5,'p_def_requirements_1','multipparser.py',720),
  ('lista_requirements -> <empty>','lista_requirements',0,'p_lista_requirements_1','multipparser.py',724),
  ('lista_requirements -> COLON ID lista_requirements','lista_requirements',3,'p_lista_requirements_2','multipparser.py',727),
  ('def_types -> LPAREN COLON TYPES lista_types RPAREN','def_types',5,'p_def_types_1','multipparser.py',732),
  ('def_types -> LPAREN COLON TYPES lista_types MINUS ID RPAREN','def_types',7,'p_def_types_2','multipparser.py',735),
  ('lista_types -> <empty>','lista_types',0,'p_lista_types_1','multipparser.py',738),
  ('lista_types -> ID lista_types','lista_types',2,'p_lista_types_2','multipparser.py',741),
  ('def_constants -> LPAREN COLON CONSTANTS lista_constants RPAREN','def_constants',5,'p_def_constants_1','multipparser.py',752),
  ('lista_constants -> <empty>','lista_constants',0,'p_lista_constants_1','multipparser.py',757),
  ('lista_constants -> lista_ids MINUS ID lista_constants','lista_constants',4,'p_lista_constants_2','multipparser.py',761),
  ('lista_constants -> lista_ids MINUS ID lista_ids','lista_constants',4,'p_lista_constants_3','multipparser.py',776),
  ('lista_constants -> lista_ids','lista_constants',1,'p_lista_constants_3','multipparser.py',777),
  ('def_predicates -> <empty>','def_predicates',0,'p_def_predicates_1','multipparser.py',783),
  ('def_predicates -> LPAREN COLON PREDICATES lista_predicates RPAREN','def_predicates',5,'p_def_predicates_2','multipparser.py',786),
  ('lista_predicates -> <empty>','lista_predicates',0,'p_lista_predicates_1','multipparser.py',795),
  ('lista_predicates -> LPAREN ID p_def RPAREN lista_predicates','lista_predicates',5,'p_lista_predicates_2','multipparser.py',799),
  ('p_def -> lista_var MINUS ID p_def','p_def',4,'p_p_def_1','multipparser.py',813),
  ('p_def -> lista_var','p_def',1,'p_p_def_2','multipparser.py',824),
  ('def_functions -> LPAREN COLON FUNCTIONS lista_functions_def RPAREN','def_functions',5,'p_def_functions_1','multipparser.py',835),
  ('lista_functions_def -> <empty>','lista_functions_def',0,'p_lista_functions_def_1','multipparser.py',845),
  ('lista_functions_def -> LPAREN ID lista_var MINUS ID RPAREN lista_functions_def','lista_functions_def',7,'p_lista_functions_def_2','multipparser.py',850),
  ('lista_functions_def -> LPAREN ID RPAREN lista_functions_def','lista_functions_def',4,'p_lista_functions_def_3','multipparser.py',861),
  ('lista_functions_def -> LPAREN ID lista_var MINUS ID RPAREN MINUS ID lista_functions_def','lista_functions_def',9,'p_lista_functions_def_4','multipparser.py',869),
  ('lista_functions_def -> LPAREN ID RPAREN MINUS ID lista_functions_def','lista_functions_def',6,'p_lista_functions_def_5','multipparser.py',876),
  ('def_actions -> <empty>','def_actions',0,'p_def_actions_1','multipparser.py',884),
  ('def_actions -> LPAREN COLON ACTION ID a_def RPAREN def_actions','def_actions',7,'p_def_actions_2','multipparser.py',887),
  ('def_actions -> LPAREN COLON ACTION ID COLON AGENT agent_def a_def RPAREN def_actions','def_actions',10,'p_def_actions_3','multipparser.py',897),
  ('agent_def -> ID','agent_def',1,'p_agent_def_1','multipparser.py',900),
  ('agent_def -> VAR ID','agent_def',2,'p_agent_def_2','multipparser.py',903),
  ('agent_def -> VAR ID MINUS ID','agent_def',4,'p_agent_def_3','multipparser.py',906),
  ('a_def -> <empty>','a_def',0,'p_a_def_1','multipparser.py',909),
  ('a_def -> COLON PARAMETERS LPAREN lista_parameters RPAREN COLON PRECONDITION pddl_preconditions COLON EFFECT pddl_effects','a_def',11,'p_a_def_2','multipparser.py',912),
  ('a_def -> COLON PARAMETERS LPAREN RPAREN COLON PRECONDITION pddl_preconditions COLON EFFECT pddl_effects','a_def',10,'p_a_def_2','multipparser.py',913),
  ('pddl_preconditions -> lista_preds_op','pddl_preconditions',1,'p_pddl_preconditions_1','multipparser.py',918),
  ('pddl_effects -> lista_preds_op','pddl_effects',1,'p_pddl_effects_1','multipparser.py',922),
  ('lista_parameters -> <empty>','lista_parameters',0,'p_lista_parameters_1','multipparser.py',926),
  ('lista_parameters -> lista_var MINUS ID lista_parameters','lista_parameters',4,'p_lista_parameters_2','multipparser.py',934),
  ('lista_parameters -> lista_var','lista_parameters',1,'p_lista_parameters_3','multipparser.py',942),
  ('lista_preds_op -> <empty>','lista_preds_op',0,'p_lista_preds_op_1','multipparser.py',947),
  ('lista_preds_op -> lista_predicados lista_preds_op','lista_preds_op',2,'p_lista_preds_op_2','multipparser.py',950),
  ('lista_preds_op -> LPAREN AND lista_preds_op RPAREN','lista_preds_op',4,'p_lista_preds_op_3','multipparser.py',954),
  ('lista_preds_op -> LPAREN FORALL lista_preds_op RPAREN','lista_preds_op',4,'p_lista_preds_op_4','multipparser.py',960),
  ('lista_preds_op -> LPAREN EXISTS lista_preds_op RPAREN','lista_preds_op',4,'p_lista_preds_op_5','multipparser.py',963),
  ('lista_preds_op -> LPAREN IMPLY lista_preds_op RPAREN','lista_preds_op',4,'p_lista_preds_op_6','multipparser.py',966),
  ('lista_preds_op -> LPAREN PREFERENCE [ ID ] RPAREN','lista_preds_op',6,'p_lista_preds_op_7','multipparser.py',969),
  ('lista_preds_op -> LPAREN WHEN lista_preds_op RPAREN','lista_preds_op',4,'p_lista_preds_op_8','multipparser.py',972),
  ('lista_predicados -> <empty>','lista_predicados',0,'p_lista_predicados_0','multipparser.py',976),
  ('lista_predicados -> LPAREN ID lista_var RPAREN lista_preds_op','lista_predicados',5,'p_lista_predicados_1','multipparser.py',979),
  ('lista_predicados -> LPAREN lista_var MINUS ID RPAREN lista_preds_op','lista_predicados',6,'p_lista_predicados_2','multipparser.py',998),
  ('lista_predicados -> LPAREN COMP lista_var RPAREN lista_preds_op','lista_predicados',5,'p_lista_predicados_3','multipparser.py',1001),
  ('lista_predicados -> LPAREN VAR ID COMP ID RPAREN lista_preds_op','lista_predicados',7,'p_lista_predicados_4','multipparser.py',1004),
  ('lista_predicados -> LPAREN DECREASE LPAREN ID RPAREN NUM RPAREN','lista_predicados',7,'p_lista_predicados_5','multipparser.py',1007),
  ('lista_predicados -> LPAREN ID RPAREN lista_predicados','lista_predicados',4,'p_lista_predicados_6','multipparser.py',1010),
  ('lista_predicados -> LPAREN NOT lista_predicados_not RPAREN','lista_predicados',4,'p_lista_predicados_7','multipparser.py',1026),
  ('lista_predicados_not -> <empty>','lista_predicados_not',0,'p_lista_predicados_not_1','multipparser.py',1032),
  ('lista_predicados_not -> LPAREN ID RPAREN lista_predicados_not','lista_predicados_not',4,'p_lista_predicados_not_2','multipparser.py',1035),
  ('lista_predicados_not -> LPAREN ID lista_var RPAREN lista_predicados_not','lista_predicados_not',5,'p_lista_predicados_not_3','multipparser.py',1045),
  ('lista_var -> <empty>','lista_var',0,'p_lista_var_1','multipparser.py',1054),
  ('lista_var -> VAR ID lista_var','lista_var',3,'p_lista_var_2','multipparser.py',1061),
  ('lista_var -> ID lista_var','lista_var',2,'p_lista_var_3','multipparser.py',1069),
  ('lista_ids -> <empty>','lista_ids',0,'p_lista_ids_1','multipparser.py',1074),
  ('lista_ids -> ID lista_ids','lista_ids',2,'p_lista_ids_2','multipparser.py',1081),
]
