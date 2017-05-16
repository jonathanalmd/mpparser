(define (problem pb1)
  (:domain caoticroom)
  (:init
    (dirty)
    (not(insideroom))
    (not(droped))
    (not(stored))
    (not(organized))
 )
  (:goal 
  	(and
    	(stored)
      (organized)
      (not
        (insideroom)
        (dirty)
      )
    )
  )
)