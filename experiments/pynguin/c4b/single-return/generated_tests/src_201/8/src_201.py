def func(*args):
	
	(a, b) = map(int, args[0].split())
	r = 0
	while ((a > 0) and (b > 0) and ((a + b) > 2)):
	    if (a < b):
	        (a, b) = (b, a)
	    a -= 2
	    b += 1
	    r += 1
	return(r)
