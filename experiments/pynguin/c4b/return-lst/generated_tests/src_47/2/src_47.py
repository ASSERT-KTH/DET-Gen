def func(*args):
	ret_values = []
	
	(a, b, c) = [int(i) for i in args[0].split()]
	(x, y, z) = [int(i) for i in args[1].split()]
	a1 = [0, 0, 0]
	a1[0] = max(0, (a - x))
	a1[1] = max(0, (b - y))
	a1[2] = max(0, (c - z))
	lost = ((max(0, (x - a)) + max(0, (y - b))) + max(0, (z - c)))
	for i in a1:
	    lost -= (i // 2)
	if (lost <= 0):
	    ret_values.append('Yes')
	else:
	    ret_values.append('No')

	return ret_values
