def func(*args):
	
	n = int(args[0])
	s = ''
	if ((n % 2) == 0):
	    s += ((n // 2) * '1')
	else:
	    s += '7'
	    s += (((n - 3) // 2) * '1')
	return(int(s))
