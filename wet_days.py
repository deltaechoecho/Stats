def wet_days (sequence,WET):

	""" when given a list ('sequence') corresponding to a year of daily precipitation data, 
	 and a value for the threshold for a 'wet' day ('WET'), will compute eight indices; wet (0) 
	 and dry (1) days, wet (2) and dry (3) spells, wettest week amount (4) and date (5), 
	 precipitation intensity (6), and a modified fournier index (7). Returns -1 as a missing value"""

	from numpy import zeros
	import count_threshold
	import consecutive_threshold
	import moving_window

	wet_days=zeros((8))
	
	#get wet and dry days
	wet_days[0]=count_threshold(sequence,0,WET,1)
	wet_days[1]=count_threshold(sequence,0,WET,0)
			
	#get wet and dry spells
	wet_days[2]=consecutive_threshold(sequence,0,WET,1,3)
	wet_days[3]=consecutive_threshold(sequence,0,WET,0,3)
	
	# get wettest week amount and date
	chunks=moving_window(sequence,7,1)
	m=1
	for chunk in chunks:
		if sum(chunk) > wet_days[4]: wet_days[5]=m+6
		if sum(chunk) > wet_days[4]: wet_days[4]=sum(chunk)
		m+=1
			
	#get prec intensity
	for p in sequence:
		if p > WET: wet_days[6] += p
	wet_days[6]=wet_days[6]/wet_days[1]
					
	# get fournier index
	prec_total=sum(sequence)
	month=0
	for m in range(1,12): 
		month+=sum(sequence[m-1+30*(m-1):30*m-1])**2
	wet_days[7]=month/prec_total	
	
	return wet_days
