def func(*args):
	
	import math
	x = int(args[0])
	digit = ''
	for i in range(10):
	    if (str(i) in str(x)):
	        digit += str(i)
	counter = 0
	for i in range(1, (int(math.sqrt(x)) + 1)):
	    if ((x % i) == 0):
	        for j in str(i):
	            if (j in digit):
	                counter += 1
	                break
	        for j in str((x // i)):
	            if ((j in digit) and ((x // i) > i)):
	                counter += 1
	                break
	return(counter)
