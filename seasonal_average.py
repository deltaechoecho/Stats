def seasonal_average (sequence, mask, nyrs, season, startyr, leaps):

  ''' if given a list ('sequence') corresponding to a daily value for a number of years ('startyr', 'nyrs')
  will compute seasonal averages of that value for a given season ('season'). Accepts "mam", "jja", "son" 
  and "djf" for 'season'. Can be masked out, needs to know if the incoming list is model data or observed ('leaps') '''

  # IN DEVELOPMENT

	from numpy import reshape
	import numpy as np
	import is_leap_year
	import how_many_leaps
	
	# does this work? need to test
  while season not in ['mam', 'jja', 'son', 'djf']:
		print "You must specify a season. Exiting."
            	sys.exit(1)
	
	# do leap year calculation for model or observed data
	if leaps==1: 
		ndays=365 
		blp=is_leap_year(startyr)  
	else: 
		ndays=360
		blp=0
	nleaps=how_many_leaps(startyr,nyrs)
	fullyears=nyrs*ndays+(nleaps*leaps)
	
	# initialise arrays
	seas_avg=np.zeros((nyrs-1,4))
	savg=np.zeros((nyrs-1))
	
	#ignore first 60 days as prior year and last 30 days as last year
	shortened=sequence[60-(1-blp):fullyears-300]
	
	#remove all leap days AND the tail end of each season to regulate it down to 90 days
	if leaps == 1:
		outshort=[]
		for i in range(0,nyrs-1):
			# how many leap years up to now
			lptot=how_many_leaps(startyr,i)
			sd=(i*ndays)+lptot
			outshort.extend(shortened[sd+0:sd+90])
			outshort.extend(shortened[sd+92:sd+182])
			outshort.extend(shortened[sd+184:sd+274])
			outshort.extend(shortened[sd+275:sd+365])
		seas_matrix=np.array(outshort).reshape((nyrs-1,4,90))
	
	#model data is 360 days long	
	if leaps == 0:
		seas_matrix=shortened.reshape((nyrs-1,4,90))
		
	for i in range(0,nyrs-2):
		for j in range(0,4):
			seas_avg[i,j]=(sum(seas_matrix[i,j,:]))/90
	if season == 'mam': savg=seas_avg[:,0]
	if season == 'jja': savg=seas_avg[:,1]
	if season == 'son': savg=seas_avg[:,2]
	if season == 'djf': savg=seas_avg[:,3]

	return savg
