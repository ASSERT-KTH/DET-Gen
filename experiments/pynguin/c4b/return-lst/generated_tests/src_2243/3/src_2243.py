def func(*args):
	ret_values = []
	
	x = args[0]
	x = str(x)
	ans = 0
	o = 0
	z = 0
	isdanger = False
	for i in range(x.__len__()):
	    if (x[i] == '0'):
	        z += 1
	        o = 0
	        if (z >= 7):
	            isdanger = True
	    else:
	        z = 0
	        o += 1
	        if (o >= 7):
	            isdanger = True
	if isdanger:
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
