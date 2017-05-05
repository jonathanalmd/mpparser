(define (domain gripper-typed)
	(:requirements :strips :typing)

	(:types room ball gripper)

	(:constants left right - gripper)

	(:predicates
		(at-robby ?r ?r2 - room ?b1 - ball)
		(at ?b - ball ?r - room)
		(free ?g - gripper)
		(carry ?o - ball ?g - gripper ?t - teste))

	(:action move
		:parameters  (?from1 ?to2 - room
						?from11 ?to22 - ball)
		:precondition 
			(at-robby1 ?from11 ?from11)
		(and
			(a ?aa ?aaa)
			(NOT(b ?b ?bb))
			(not(at-robby2 ?from22 ?from22))
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
			(free ?gripper)
		)
		:effect (and 
			(carry ?obj ?gripper)
			(IRRA ?i ?i2)

			(not(free ?gripperd)
			 (at ?obj ?room))
		)
	)

	(:action drop
		:parameters (?room ?room2 - room)
		:precondition (and (ball ?obj) (room ?room) (gripper ?gripper) (carry ?obj ?gripper) (at-robby ?room))
		:effect (and (at ?obj ?room) (free ?gripper) (not (carry ?obj ?gripper))))
)






