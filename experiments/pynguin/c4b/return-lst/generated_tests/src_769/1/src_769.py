def func(*args):
	ret_values = []
	
	p = [2]
	n = (int(args[0]) + 1)
	for i in range(3, n):
	    y = 1
	    for j in p:
	        y = (y and (i % j))
	    if y:
	        p += [i]
	ret_values.append(sum([(2 == sum([(not (i % j)) for j in p])) for i in range(6, n)]))

	return ret_values
