def func(*args):
	ret_values = []
	
	(x, y) = map(int, args[0].split())
	x = (7 - max(x, y))
	y = 6
	while (((x % 2) == 0) and ((y % 2) == 0)):
	    x /= 2
	    y /= 2
	while (((x % 3) == 0) and ((y % 3) == 0)):
	    x /= 3
	    y /= 3
	ret_values.append(('%d%s%d' % (x, '/', y)))

	return ret_values
