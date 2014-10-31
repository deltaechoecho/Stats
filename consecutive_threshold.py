def consecutive_threshold (sequence, mask, thresh, switch, num):
	""" returns the maximum number of consecutive entries over which a given threshold ('thresh') 
	is reached if that number of entries itself is over 'num'. If thresh is a list, it must be the same length 
	as the data being tested, and it will test the data element by element in both sequence and thresh. 
	Can be switched between positive (switch=1) and negative (switch=0) behaviour, and masked out with a -1 value.
	"""
		
	import numpy as np
	
	# determines proportion of data present, assuming missing value signifier is -999.9
	valid_idx=sequence+999.9 >= 0
	v_sequence=sequence[valid_idx]
	valid_perc=len(v_sequence)/len(sequence)*100	
	if type(thresh) != np.ndarray:
		thresh=np.tile(thresh,len(sequence))
	
	if valid_perc >= 85:
		countMax=0
      		q=0
		# for number of values in the sequence
      		for i in range(0, len(sequence)+1):
		# when above given threshold
			if switch == 1:
			# if at limit of data, or data is below threshold
      				if i == len(sequence) or sequence[i] <= thresh[i]:
				# store count if biggest so far
                  			if q > countMax:
           	    	          		countMax=q
					# restart count otherwise
                	        	q=0
                		else:           
				# increment count 
                     		   	q+=1
			# when below given threshold
			elif switch == 0:
      				if i == len(sequence) or sequence[i] >= thresh[i]:
                  			if q > countMax:
                         			countMax=q
                        		q=0
                		else:           
                        		q+=1
     		if countMax >= num and mask > -1:
			return countMax 
		elif mask > -1:
			return 0
		else:
			return -1
			
	if valid_perc < 85:
		countMax=0
		return countMax 
	
