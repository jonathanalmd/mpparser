(define (problem BLOCKS40)

(:domain BLOCKS)

(:objects D B A C - gripper
			X Y Z - room
)

(:INIT 	
	(CLEAR C) 
	(CLEAR A)   
	(CLEAR B) 
	(CLEAR D) 
		(NOT(HANDEMPTY))

	(ONTABLE C) 
	(= (ondblock C A B D) 1)
	(NOT(on AAA)
	(onB BBBBBB CC))
	(ONTABLE A)
	(ONTABLE B) 
	(ONTABLE D) 
	(NOT(HANDEMPTY))
	
)



(:goal 
	(AND
		(CLEAR B) 
		(CLEAR D) 
		(ONTABLE A)
		(= (onblock Cds dsd dsd ) D)
		(NOT
				(CLEAR B) 
			
		)
				(ONTABLE C) 
		(= (onblock Cds dsd dsd ) D)

	)
)

)
