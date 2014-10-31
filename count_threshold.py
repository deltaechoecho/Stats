def count_threshold (sequence,mask,thresh,switch):
	""" returns the number of times a given threshold ('thresh') is reached 
	within a given list ('sequence'). Note that the LESS THAN function is given
	by a 0 switch, and MORE THAN function is given by a 1 switch. This
	module can by bypassed with a -1 mask value
	
	Want to count the number of frosts in a year? This code has your back."""
	
	q=0
	if mask != -1:
		for p in sequence:
			if switch == 0:
				if p <= thresh: q=q+1
			if switch == 1:
				if p >= thresh: q=q+1
			if not (0 <= switch <= 1):
				raise Exception("**ERROR** Switch must be 0 or 1")
				import sys
				sys.exit(1)
		return q
	else:
		return -1
