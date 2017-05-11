(define (problem pb1)
  (:domain dinner lanche)
  (:init
    (garbage)
    (clean)
    (quiet)
  )
  (:goal 
  	(and
    	(dinner)
    	(present)
   			(garbage)
   			(not(quiet))
    )
  )
)