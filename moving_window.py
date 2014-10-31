def moving_window(sequence,winsize,step):
	"""Returns a python generator that will iterate through defined chunks ('winsize') a given distance ('step') 
	apart for, an input list ('sequence'). The input sequence must be iterable and the window size must reflect
	the underlying distribution to give meaningful indices.
	
	If you want to do a moving-window average quickly, call this to make the window."""
	
	#import 
	import itertools
	
	# Verify the inputs
	try: it = iter(sequence)
	except TypeError:
		raise Exception("**ERROR** sequence must be iterable.")
	if not ((type(winsize) == type(0)) and (type(step) == type(0))):
		raise Exception("**ERROR** type(winsize) and type(step) must be int.")
	if step > winsize:
		raise Exception("**ERROR** step must not be larger than winsize.")
	if winsize > len(sequence):
		raise Exception("**ERROR** winsize must not be larger than sequence length.")
	
	#pre-compute number of chunks to emit
	numOfChunks=((len(sequence)-winsize)/step)+1
	
	#do work
	for i in range(0,numOfChunks*step,step):
		yield sequence[i:i+winsize]			
