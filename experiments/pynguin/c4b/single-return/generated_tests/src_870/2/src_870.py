def func(*args):
	
	(x, y) = map(int, args[0].split(' '))
	c = min(x, y)
	s = 1
	i = 1
	while (i <= c):
	    s = (s * i)
	    i = (i + 1)
	return(s)
