def func(*args):
	ret_values = []
	
	x = 1
	step = 1
	(a, b) = map(int, args[0].split())
	while True:
	    if (step == 1):
	        if (x > a):
	            break
	        a -= x
	        x += 1
	        step = 0
	    else:
	        if (x > b):
	            break
	        b -= x
	        x += 1
	        step = 1
	if (step == 1):
	    ret_values.append('Vladik')
	else:
	    ret_values.append('Valera')

	return ret_values
