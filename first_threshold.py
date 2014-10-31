def first_threshold (sequence, winsize, step, thresh, switch):
	""" returns the first position ('i') a given threshold ('thresh') is exceeded (for switch=1),
	or not exceeded (for switch=0), in a given list ('sequence') for a moving window 
	specified by the moving_window module.
	
	If you want to see which week in a year the temperature first exceeds 15 degrees, this will do that for you."""
	
	import numpy as np
	import moving_window
	
	try: chunks=moving_window(sequence,winsize,step)
	except TypeError:
		raise Exception("**ERROR** moving_window poorly specified**")
		import sys
		sys.exit(1)
	i=0
	for chunk in chunks:
		if switch == 1: test1 = chunk > thresh
		if switch == 0: test1 = chunk < thresh
		if not (0 <= switch <= 1):
				raise Exception("**ERROR** Switch must be 0 or 1")
				import sys
				sys.exit(1)
		testchunk = all(test1)
		if testchunk:
			if switch == 1: return i
			if switch == 0: return i
		i=i+1
	return -1
