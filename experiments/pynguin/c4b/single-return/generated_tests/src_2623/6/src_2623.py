def func(*args):
	
	i = (lambda : map(int, args[0].split()))
	(a, b) = i()
	c = 0
	while (a <= b):
	    a = (a * 3)
	    b = (b * 2)
	    c = (c + 1)
	return(c)
