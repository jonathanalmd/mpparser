  (define (domain caoticroom) ; There is no block comment like
    (:requirements :strips :negative-preconditions)
    (:predicates
      (insideroom)
      (dirty)
      (droped)
      (stored)
      (organized)
    )
    (:action enter
      :parameters ()
      :precondition (and
        (not (insideroom))
      )
      :effect (and
        (insideroom)
      )
    )
    (:action leave
      :parameters ()
      :precondition (and
        (insideroom)
      )
      :effect (and
        (not(insideroom)
        )
      )
    )
    (:action clean
      :parameters ()
      :precondition (and
        (dirty)
        (insideroom)
      )
      :effect (and
        (not (dirty)
        )
      )
    )
    (:action dropout
      :parameters ()
      :precondition (and
        (not
          (insideroom)
          (dirty)
        )
      )
      :effect (and
        (droped)
      )
    )
    (:action store
      :parameters()
      :precondition
        (and
        (insideroom)
        (droped)
        (not 
          (dirty)
        )
        )
      :effect
        (and
        (stored)
        )
    )
    (:action organize
      :parameters()
      :precondition
        (and
        (stored)
        (droped)
        (insideroom)
        (not 
          (dirty)
        )
        )
      :effect
        (and
        (organized)
        )
    )

  )