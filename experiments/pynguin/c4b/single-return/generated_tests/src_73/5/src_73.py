def func(*args):
	
	a = int(args[0])
	b = int(args[1])
	c = int(args[2])
	cc = (c // 4)
	bb = (b // 2)
	return(((min(cc, bb, a) + (2 * min(a, bb, cc))) + (4 * min(a, bb, cc))))
