(define (problem BLOCKS40)

(:domain BLOCKS)

(:objects D B A C - block
			X Y Z - block2
)

(:INIT 	
	(CLEAR C) 
	(CLEAR A) 
	(CLEAR B) 
	(CLEAR D) 
	(ONTABLE C) 
	(= (ondblock C) 1)
	(NOT(on AAA))
	(ONTABLE A)
	(ONTABLE B) 
	(ONTABLE D) 
	(HANDEMPTY)
	
)



(:goal 
	(AND
		(CLEAR B) 
		(CLEAR D) 
		(ONTABLE C) 
		(ONTABLE A)
		(= (onblock Cdsd) D)
		(NOT
				(CLEAR B) 
			
		)
	)
)

)
