
(define (domain dinner) 
  (:requirements :strips)
  	(:types room ball gripper) 


  	(:constants left right - typed a b c - bola)

  (:predicates
		(free ?d1 ?d2)
		(free ?f)
		(free)
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