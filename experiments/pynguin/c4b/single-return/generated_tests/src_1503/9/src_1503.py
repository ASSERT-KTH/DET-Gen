def func(*args):
	
	
	def read():
	    return [int(x) for x in args[0].split()]
	(x, y) = read()
	i = 0
	while (x <= y):
	    x *= 3
	    y *= 2
	    i += 1
	return(i)
