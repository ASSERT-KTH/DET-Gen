def func(*args):
	
	(a, b, c) = [int(x) for x in args[0].split()]
	ans = (2 * ((a + b) + c))
	if (c > (a + b)):
	    ans = (2 * (a + b))
	else:
	    if (c < a):
	        ans = (2 * (b + c))
	    if (c < b):
	        ans = min(ans, (2 * (a + c)))
	    ans = min(ans, ((a + b) + c))
	return(ans)
