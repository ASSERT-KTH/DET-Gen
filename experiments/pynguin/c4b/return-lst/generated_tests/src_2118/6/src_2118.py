def func(*args):
	ret_values = []
	
	DELITELI = (4, 7, 44, 47, 74, 77, 444, 447, 474, 477)
	n = int(args[0])
	i = 0
	k = 0
	if ((n % 4) == 0):
	    k = 1
	elif (n in DELITELI):
	    k = 1
	else:
	    for i in DELITELI:
	        if ((n % i) == 0):
	            k = 1
	            break
	if (k == 1):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
