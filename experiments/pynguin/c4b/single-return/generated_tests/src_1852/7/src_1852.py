def func(*args):
	
	(n, k) = (int(x) for x in args[0].split())
	time = (240 - k)
	r = 0
	while ((time >= 0) and (r <= n)):
	    r += 1
	    time -= (5 * r)
	return((r - 1))
