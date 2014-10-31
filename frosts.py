def frosts (sequence,win_FROST,AF,GF,HY):
	""" when given a list ('sequence') corresponding to a year of daily minimum temperature data, 
	a window ('win_FROST') over which to compute thresholds, a value for air frosts ('AF'), grass frosts ('GF') and 
	the half year point of the sequence ('HY'), returns an array of seven values, corresponding 
	to the first (0) and last (1) air frosts, the number of air frost days (2), the 
	first (3) and last (4) grass frosts, the number of grass frost days (5), and the 
	accumulated number of frost days (6). Returns -1 as a missing value"""

	from numpy import zeros
	import first_threshold
	import count_threshold

	first_half=sequence[HY:]
	second_half=sequence[:HY]
	frost_array=zeros((7))
	
	#get first air and grass frosts	
	a=first_threshold(first_half,win_FROST,1,AF,0)
	if a != -1:frost_array[0]=a+HY
	if a == -1: frost_array[0]=-1
	b=first_threshold(first_half,win_FROST,1,GF,0)
	if b != -1:frost_array[3]=b+HY
	
	#get last air and grass frosts
	revloc=second_half[::-1]	# reverses order of location in order to find last instance of frost
	af=first_threshold(revloc,win_FROST,1,AF,0)
	if af != -1:frost_array[1]=HY-af
	gf=first_threshold(revloc,win_FROST,1,GF,0)
	if gf != -1:frost_array[4]=HY-gf
	
	# get air frost days, grass frost days, and accumulated frost days
	frost_array[2]=count_threshold(sequence,0,AF,0)
	frost_array[5]=count_threshold(sequence,0,GF,0)
	for p in sequence:
		if p < AF and frost_array[0] != -1: frost_array[6] += p

	return frost_array
