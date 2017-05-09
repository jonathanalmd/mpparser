; This is a comment line
(define (domain dinner) ; There is no block comment like
  (:requirements :strips)
  (:predicates
    (clean)
    (dinner)
    (quiet)
    (present)
    (garbage)
  )
  (:action cook
    :parameters ()
    :precondition (and
      (clean)
    )
    :effect (and
      (dinner)
    )
  )
  (:action wrap
    :parameters ()
    :precondition (and
      (quiet)
    )
    :effect (and
      (present)
    )
  )
  (:action carry
    :parameters (?frlom ?to)
    :precondition (and
      (garbage)

      (clean ?d1 ?d2)
      (quiet)
      (cleaner ?d)
    )
    :effect (and
            (quiet)

      (clean ?d1 ?d2)
        (garbage)
      (cleaner ?d)
        (garbage)
      (cldsdsdsdeaner ?sd)

    )
  )
)