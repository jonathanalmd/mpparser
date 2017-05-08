
(define (domain dinner) 
  (:requirements :strips)
  	(:types room ball gripper)cd



  (:predicates
		(free ?d1 ?d2)
		(free ?f)
		(free)
  )
   (:functions

     (road-length ?l1 ?l2 - location)
         (total-cost2)

     (total-cost ?ds - loc) - number3

  )
  (:action cook
    :parameters ()
    :precondition 
    	(and
      	(clean)
      	)
    :effect 
    	(and
      	(dinner ?f)
    	)
	)
)