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
    :parameters ()
    :precondition (and
      (garbage)
    )
    :effect (and
      (not (garbage)
      (clean)
      )
    )
  )
  (:action dolly
    :parameters ()
    :precondition (and
      (garbage)
    )
    :effect (and
      (not (garbage)
      (quiet))
    )
  )
  (:action dirty
    :parameters()
    :precondition
      (and
      (quiet)
      (not (garbage)(garbage))
      )
    :effect
      (and
      (garbage)
      (garbage)
      (garbage)

      (garbage)
                  (not (quiet)(quiet))

      )
  )
)


