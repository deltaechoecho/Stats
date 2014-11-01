def growing_season (sequence,win_GSL,GSL,HD,SFO,HY):

	""" when given a list ('sequence') corresponding to a year of daily average temperature data, 
	a window over which to compute thresholds ('win_GSL'), and values for	growing ('GSL') and 
	heating degree day ('HD') thresholds, a field operations threshold ('SFO'), and the half year 
	point of the sequence ('HY'), returns an array of seven values, corresponding to the start (0) and 
	end (1) of growing season, its range (2) and length (3), the number of growing (4) and 
	heating (5) degree days and the start of field operations (6). Returns -1 as a missing value"""

	from numpy import zeros
	import first_threshold
	import cumulative_threshold

	first_half=sequence[HY:]
	second_half=sequence[:HY]
	growing_array=zeros((7))
	
	#get growing season start
	growing_array[0]=first_threshold(sequence,win_GSL,1,GSL,1)
	
	#get growing season end and growing season range
	a=first_threshold(first_half,win_GSL,1,GSL,0)
	if a != -1:growing_array[1]=a+HY
	growing_array[2]=growing_array[1]-growing_array[0]
	
	#get growing season length
	season=sequence[growing_array[0]:growing_array[1]]
	growing_array[3]=count_days(season,0,GSL,1)
	
	#get growing degree days and heating degree days
	for p in sequence:
		if p > GSL and growing_array[0] != -1: 
			growing_array[4] += p 	
		elif growing_array[0] == -1:
			growing_array[4] = -1
		if p < HD and growing_array[0] != -1: 
			growing_array[5] += (HD-p)
		elif growing_array[0] == -1: 
			growing_array[5] = -1
			
	# get start of field operations
	if growing_array[0] != -1:
		growing_array[6]=cumulative_threshold(sequence,SFO)
	else: 
		growing_array[6]=-1
	
	return growing_array
