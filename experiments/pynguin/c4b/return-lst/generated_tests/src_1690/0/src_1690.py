def func(*args):
	ret_values = []
	
	list = args[0].split()
	a = []
	for i in range(0, len(list)):
	    a.append(int(list[i]))
	q = 2
	for i in range(0, 4):
	    if (((a[i] + a[((i + 1) % 4)]) >= a[((i + 2) % 4)]) and ((a[((i + 1) % 4)] + a[((i + 2) % 4)]) >= a[i]) and ((a[((i + 2) % 4)] + a[i]) >= a[((i + 1) % 4)])):
	        if (((a[i] + a[((i + 1) % 4)]) == a[((i + 2) % 4)]) or ((a[((i + 1) % 4)] + a[((i + 2) % 4)]) == a[i]) or ((a[((i + 2) % 4)] + a[i]) == a[((i + 1) % 4)])):
	            if (q > 1):
	                q = 1
	        else:
	            q = 0
	            break
	if (q == 0):
	    ret_values.append('TRIANGLE')
	elif (q == 1):
	    ret_values.append('SEGMENT')
	else:
	    ret_values.append('IMPOSSIBLE')

	return ret_values
