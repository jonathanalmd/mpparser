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
		:precondition (and(at-robby ?from3 ?from33)(at-robby ?from333 ?from333))
		:effect (and  (at-robby ?to4) (at-robbyx ?from5 ?from6))
	)

	(:action pick
		:parameters (?roomAAA ?e3 - rm)
		:precondition  (and  (at ?obj11 ?room11) (at-robby ?room) (free ?gripper))
		:effect (and (carry ?obj ?gripper) (not (at ?obj ?room)) (not (free ?gripperd))))

	;(:action drop
	;	:parameters (?obj - ball ?room - room ?gripper - gripper)
	;	:precondition (and (ball ?obj) (room ?room) (gripper ?gripper) (carry ?obj ?gripper) (at-robby ?room))
	;	:effect (and (at ?obj ?room) (free ?gripper) (not (carry ?obj ?gripper))))
)






