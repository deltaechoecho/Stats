def ami_ensemble_stats(indata,nlat,nlon):
	"""generates ensemble mean, max, and min for the ami data generated with get_amiuk.py
	the stats code is incredibly simple iteration with missing value handling, because 
	it used to be fortran code, nothing clever or optimised."""
	
	import numpy as np
	from pylab import average
	
	mean=np.zeros((149,nlat,nlon))
	meanobs=np.zeros((61,nlat,nlon))
	minm=np.zeros((149,nlat,nlon))
	minobs=np.zeros((61,nlat,nlon))
	maxm=np.zeros((149,nlat,nlon))
	maxobs=np.zeros((61,nlat,nlon))
	
	#mean map
	for j in range(0,nlat):
		for k in range(0,nlon):
			for i in range(0,149):
				mcount=0
				for h in range (0,10):
					if indata[h,i,j,k]!=-1.0:
						mean[i,j,k]=mean[i,j,k]+indata[h,i,j,k]
						mcount+=1
				if mcount > 0:
					mean[i,j,k]=mean[i,j,k]/mcount
				else:
					mean[i,j,k]=np.nan
			ocount=0	
			for i in range(0,61):
				if indata[11,i,j,k] !=-1.0:
					meanobs[i,j,k]=average(indata[11,i,j,k])
					ocount+=1
			if ocount > 0:
				meanobs[i,j,k]=meanobs[i,j,k]/ocount
			else:
				meanobs[i,j,k]=np.nan
			
	#minimal map
	for j in range(0,nlat):
		for k in range(0,nlon):
			for i in range(0,149):
				minm[i,j,k]=min(indata[0:10,i,j,k])
			mac=np.ma.count(indata[11,:,j,k])
			for i in range(0,61):
			# check to see if any values left after mask, if none, use missing value
				if mac < 2:
					minobs[i,j,k]=np.nan
				else:
					minobs[i,j,k]=min(indata[11,:,j,k])

	#maximal map
	for j in range(0,nlat):
		for k in range(0,nlon):
			for i in range(0,149):
				maxm[i,j,k]=max(indata[0:10,i,j,k])
			mac=np.ma.count(indata[11,:,j,k])
			for i in range(0,61):
			# check to see if any values left after mask, if none, use missing value
				if mac < 2:
					maxobs[i,j,k]=np.nan
				else:
					maxobs[i,j,k]=max(indata[11,:,j,k])
	
	return(mean, meanobs, maxm, maxobs, minm, minobs)
