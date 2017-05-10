;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; 4 Op-blocks world
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(define (domain BLOCKS)
  (:requirements :strips)
  (:predicates (on ?x ?y)
	       (ontable ?x)
	       (clear ?x)
	       (handempty ?h)
	       (holding ?x)
	       )

  (:action pick-up
	     :parameters (?x - t)
	     :precondition (and (clear ?x) (ontable ?x) (handempty ?h))
	     :effect
	     (and 
 		   	(holding ?x)

	     	(not (ontable ?x))
		   	(not (clear ?x))
		   	(not (handempty ?h))
		  )
	)

  (:action put-down
	     :parameters (?x)
	     :precondition (holding ?x)
	     :effect
	     (and 
		   (clear ?x)
		   (handempty ?h)
		   (ontable ?x)
		   (not (holding ?x))
		   ))
  (:action stack
	     :parameters (?x ?y)
	     :precondition (and (holding ?x) (clear ?y))
	     :effect
	     (and 
	     (clear ?x)
		   (handempty ?h)
		   (on ?x ?y)(not (holding ?x))
		   (not (clear ?y))
		   ))
  (:action unstack
	     :parameters (?x ?y)
	     :precondition (and (on ?x ?y) (clear ?x) (handempty ?h))
	     :effect
	     (and (holding ?x)
		   (clear ?y)
		   (not (clear ?x))
		   (not (handempty ?h))
		   (not (on ?x ?y)))))
