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
	(= (ondblock C A B D) 1)
	(NOT(on AAA))
	(ONTABLE A)
	(ONTABLE B) 
	(ONTABLE D) 
	(NOT(HANDEMPTY))
	
)



(:goal 
	(AND
		(CLEAR B) 
		(CLEAR D) 
		(ONTABLE C) 
		(ONTABLE A)
		(= (onblock Cds dsd dsd ) D)
		(NOT
				(CLEAR B) 
			
		)
	)
)

)
