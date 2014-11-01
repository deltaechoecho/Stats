def daily_baseline (sequence, nyrs, refstart, refend):

	""" when given a list ('sequence') corresponding to several years ('nyrs') of daily temperature data, 
	will compute a baseline year of daily values from the reference period ('refstart', 'refend')."""

	from numpy import tile
	from numpy import zeros

	ythresh=zeros((360))
	waves=zeros((nyrs))
	for day in range(0,360):
		baseline=0
		for year in range(refstart,refend):
			baseline+=sequence[day+(year*360)]
		ythresh[day]=baseline/(refend-refstart)
	return ythresh
