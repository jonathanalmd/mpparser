(define (problem pb1)
  (:domain dinner)

  (:init
    (garbage f)
    (clean f)
    (quiet f)
  )
  (:goal (and
    (dinner f)
    (present f)
    (not (garbage))
  ))
)