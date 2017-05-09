(define (domain gripper-typedd)
	(:requirements :strips :typing)

	(:types room ball gripper)

	(:constants left right - gripper)

	(:predicates
		(at ?b - ball ?r - room)
		(free ?g - gripper)

		(carry ?o - ball ?g - gripper ?t - teste)
	)
  (:functions

     (road-length ?l1 ?l2 - location)
         (total-cost2)

     (total-cost ?ds - loc) - number3

  )
	(:action move
		:parameters  (?from1 ?from2 - t ?to22 - re ?t2 - teste3)
		:precondition 
		(and
			(at-robby1 ?from11 ?from11)
			
		)
		:effect (and
			(not
			(at-robby3 ?to4)
			
			(at-robbyx4 ?from5 ?from6)
			)
		)
	)

	(:action pick
		:parameters (?roomAAA ?e3 - rm ?aaa - sad)
		:precondition  (and 
			(at ?obj11 ?room11)
			(at-robby ?room)
			(not(frede ?gripper))

		)
		:effect (and 
			(carry ?obj ?gripper)
			(IRRA ?i ?i2)






		)
	)

	(:action drop
		:parameters (?room ?room2 - room)
		:precondition (and (ball ?obj) (room ?room) (gripper ?gripper) (carry ?obj ?gripper) (at-robby ?room))
		:effect 
			(and 


			(at ?obj ?room)
						(at2 ?obj ?room) 

			(not (carry1 ?obj1 ?gripper1)

			(carry2 ?obj2 ?gripper2))
			(not (carry3 ?obj3 ?gripper3))
			(not (carry4 ?obj4 ?gripper4))


			)
	)
)




