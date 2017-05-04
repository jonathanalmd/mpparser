(define (problem BLOCKS40)

(:domain BLOCKS)

(:objects D B A C - block
			X Y Z - block2
)

(:INIT 	(CLEAR C) 
	(CLEAR A) 
	(CLEAR B) 
	(CLEAR D) 
	(ONTABLE C) 
	(ONTABLE A)
	(ONTABLE B) 
	(ONTABLE D) 
	(HANDEMPTY)
	(= (ondblock C) D)
)



(:goal 
	:agent agent1 :condition (lifted table)
	(AND
		(NOT
			(AND
				(CLEAR B) 
				(CLEAR D) 
				(ONTABLE C) 
			)
		)
		(CLEAR B) 
		(CLEAR D) 
		(ONTABLE C) 
		(ONTABLE A)
		(= (onblock C) D)
	)
)

)
