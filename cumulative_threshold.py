def cumulative_threshold (sequence, thresh):
	""" returns the number of list items ('dys') before a given threshold ('thresh') is 
	cumulatively attainted within a given list ('sequence'), returns -1 if that threshold 
	is never reached.
	
	If you want to count how many days it takes for daily temperature to add up to 200, you can use this."""

	#import
	from numpy import cumsum

	lim=1
	dys=0
	for n in sequence:
		y=cumsum(sequence[0:lim])
		maxy=max(y)
		if maxy >= thresh: return dys
		dys=dys+1
		lim=lim+1
	return -1
