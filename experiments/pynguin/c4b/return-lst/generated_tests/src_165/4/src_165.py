def func(*args):
	ret_values = []
	
	'input\n11 5 6 11\n'
	from itertools import combinations as combo
	l = list(combo(list(map(int, args[0].split())), 3))
	(t, s) = (0, 0)
	for x in l:
	    if (((x[0] + x[1]) > x[2]) and ((x[0] + x[2]) > x[1]) and ((x[1] + x[2]) > x[0])):
	        t = 1
	        break
	    elif (((x[0] + x[1]) >= x[2]) and ((x[0] + x[2]) >= x[1]) and ((x[1] + x[2]) >= x[0])):
	        s = 1
	if (t == 1):
	    ret_values.append('TRIANGLE')
	elif (s == 1):
	    ret_values.append('SEGMENT')
	else:
	    ret_values.append('IMPOSSIBLE')

	return ret_values
