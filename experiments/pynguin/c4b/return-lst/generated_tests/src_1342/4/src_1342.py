def func(*args):
	ret_values = []
	
	s = [int(i) for i in args[0].split(' ')]
	t = [int(i) for i in args[1].split(' ')]
	d = [(a - b) for (a, b) in zip(s, t)]
	for (i, _) in enumerate(d):
	    if (d[i] < 0):
	        for (j, _) in enumerate(d):
	            while ((d[j] > 1) and (d[i] < 0)):
	                d[j] -= 2
	                d[i] += 1
	worked = True
	for i in d:
	    if (i < 0):
	        worked = False
	        break
	if worked:
	    ret_values.append('Yes')
	else:
	    ret_values.append('No')

	return ret_values
