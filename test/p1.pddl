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
	(ONTABLE A)
	(ONTABLE B) 
	(ONTABLE D) 
	(HANDEMPTY)
	(= (ondblock C D E F) 10)
	(NOT(con AAA BBB CCC))
	(NOT(con AAA))
	(NOT(con AAA))

)



(:goal 
	
)

)
