(define (problem pb1)
  (:domain dinner)
  (:init

    (clean)
    (not(garbage))
    (not(garbage))
    (quiet)
  )
  (:goal (and
    (dinner)
    (present)
    (not (garbage))
        (present)

    (not (garbage))
    (not (garbage))
    (not (garbage))
  ))
)