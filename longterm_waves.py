def longterm_waves (sequence, mask, thresh, nyrs, startyr, refstart, refend, switch, leaps):

	""" when given a list ('sequence') corresponding to several years ('startyr', 'nyrs') of daily temperature data, 
	 and a value for the threshold for a 'cold' or 'hot' day ('thresh'), will compute the number of winter cold-waves 
	 (switch equal to 1) or summer heat-waves (switch equal to 0) from a reference period ('refstart', 'refend')
	 
	 'leaps' is a signifier for whether the incoming list is model data (with 360 day years) or observed (365/6
	 day years).
	 """


	from numpy import tile
	from numpy import zeros
	import is_leap_year
	import consecutive_threshold
	
	if leaps==1: ndays=365 
	else: ndays=360

	ythresh=zeros((ndays))
	waves=zeros((nyrs))
	for day in range(0,ndays):
		baseline=0
		nleaps=0
		for year in range(refstart,refend):
			baseline+=sequence[day+(year*ndays)+nleaps]
			nleaps+=is_leap_year(year)
		ythresh[day]=baseline/(refend-refstart)
	series_thresh=tile(ythresh,(nyrs))
	
	# Should be able to collapse these two cases into one with some clever thinking.
	if switch == 1:
		nleaps=0
		for nyr in range (0,nyrs):
			location=sequence[90+(nyr*ndays)+nleaps:270+(nyr*ndays)+nleaps]
			seas_thresh=series_thresh[90+(nyr*ndays)+nleaps:270+(nyr*ndays)+nleaps]+thresh
			waves[nyr]=consecutive_threshold(location,mask,seas_thresh,1,7)
			nleaps+=is_leap_year(nyr+startyr)*leaps
	if switch == 0:	
		nleaps=0
		for nyr in range (0,nyrs):
			if nyr == (nyrs-1):
				waves[nyr]=-1
			else:
				location=sequence[270+(nyr*ndays)+nleaps:450+(nyr*ndays)+nleaps]
				seas_thresh=series_thresh[270+(nyr*ndays)+nleaps:450+(nyr*ndays)+nleaps]-thresh
				waves[nyr]=consecutive_threshold(location,mask,seas_thresh,0,7)
				nleaps+=is_leap_year(nyr+startyr)*leaps
	return waves
