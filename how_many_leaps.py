def how_many_leaps(startyr, nyrs):
""" counts how many leapyears happen in an 'nyrs' period from a given 'startyr' """
import is_leap_year
	n=0
	years=range(startyr,startyr+nyrs+1)
	for yr in years:
		n+=is_leap_year(yr)
	return n
