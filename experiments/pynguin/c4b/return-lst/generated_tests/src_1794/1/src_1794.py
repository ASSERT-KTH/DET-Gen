def func(*args):
	ret_values = []
	
	a = args[0]
	b = int(a[(- 1)])
	a = a[0:(- 1)]
	if ((b == 1) or (b == 8)):
	    b = 0
	else:
	    b = 1
	if ((a == 'a') or (a == 'h')):
	    a = 0
	else:
	    a = 1
	if ((a == 1) and (b == 1)):
	    ret_values.append(8)
	elif ((a == 0) and (b == 1)):
	    ret_values.append(5)
	elif ((a == 1) and (b == 0)):
	    ret_values.append(5)
	else:
	    ret_values.append(3)

	return ret_values
