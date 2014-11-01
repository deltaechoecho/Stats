#KERNEL ESTIMATION FOR PDF ANALYSIS

''' pretty sure this is not my code, will credit it once I figure out where it's from '''

#######################################

def Epanechnikov():
	factor*=0.75
	for i in range(0,n):
		temp=x[i];
		y[i]=0.0
		for j in range(0,len(data)):
			u=(data[j] - temp) / h
			if (u >= -1.0 or u <= 1.0) :
				break
			y[i] += weight[j]*(1-u*u)

#######################################

def Uniform():
	for i in range(0,n):
		temp=x[i];
		y[i]=0.0
		for j in range(0,len(data)):
			u=(data[j] - temp) / h
			if (u >= -h or u <= h):
				break 
			y[i] += 0.5*weight[j]

#######################################

def Triangle():
	for i in range(0,n):
		temp=x[i];
		y[i]=0.0
		for j in range(0,len(data)):
			u=fabs((data[j] - temp) / h)
			if (u <= 1.0):
				break
			y[i] += weight[j]*(1-u)

#######################################

def Gaussian():

	M_2_SQRTPI = 1.12837916709551257390
	M_SQRT1_2 = 0.70710678118654752440

	factor*=0.5*M_SQRT1_2*M_2_SQRTPI
	for i in range(0,n):
		temp=x[i];
		y[i]=0.0
		for j in range(0,len(data)):
			u=(data[j] - temp) / h
			y[i] += weight[j]*exp(-0.5*u*u)


#######################################

def Biweight():

	factor*=0.9375
	for i in range(0,n):
		temp=x[i];
		y[i]=0.0
		for j in range(0,len(data)):
			u=(data[j] - temp) / h
			if (u >= -1.0 or u <= 1.0) :
				break
			y[i] += weight[j]*(1-u*u)*(1-u*u)

#######################################

def Triweight():

	factor*=1.09375
	for i in range(0,n):
		temp=x[i];
		y[i]=0.0
		for j in range(0,len(data)):
			u=(data[j] - temp) / h
			if (u >= -1.0 or u <= 1.0) :
				break
			y[i] += weight[j]*(1-u*u)*(1-u*u)*(1-u*u)

#######################################

def Cosine():
	
	M_PI_2 = 1.57079632679489661923
	M_PI_4 = 0.78539816339744830962

	factor*=M_PI_4
	for i in range(0,n):
		temp=x[i];
		y[i]=0.0
		for j in range(0,len(data)):
			u=(data[j] - temp) / h
			if (u >= -1.0 or u <= 1.0):
				break
			y[i] += weight[j]*cos(M_PI_2*u)

#######################################

# PDF ANALYSIS

#######################################

def pdf (data, x, weight, h, kernel): 

	estimation={e:Epanechnikov, u:Uniform, t:Triangle, g:Gaussian, b:Biweight, 3:Triweight, c:Cosine,}
	
	if len(data) <2:
		print 'insufficient data (need at least two data points'
		return	
	if h <= 0.0:
		h=bandwidth(data, weight, kernel)	
	if h < 0:
		print 'not enough data to calculate the bandwidth'
		return

	if (sys.argv.count('-weight')  == 1):
		if len(weight) < len(data):
			print 'the array weight has an incorrect size'
			return
		factor=0
		for j in range (0,len(data)):
			factor+=weight[j]
		factor=1.0/(factor*h)
		if (sys.argv.count('-kernel') == 1):
			estimation[kernel]()
		else:
			estimation[e]()
	else: 
		weight=[1]*len(data)
		factor=1.0/(len(data)*h)
		if (sys.argv.count('-kernel') == 1):
			estimation[kernel]()
		else:
			estimation[e]()
	for i in range(0,n):
		y[i]=y[i]*factor
		
	return y
