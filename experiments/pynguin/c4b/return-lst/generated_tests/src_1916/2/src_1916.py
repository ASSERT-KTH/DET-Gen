def func(*args):
	ret_values = []
	
	(m, d) = [int(x) for x in args[0].split()]
	if (m == 2):
	    if (d == 1):
	        ret_values.append('4')
	    if (d != 1):
	        ret_values.append('5')
	elif ((m == 4) or (m == 6) or (m == 9) or (m == 11)):
	    if (d == 7):
	        ret_values.append('6')
	    if (d != 7):
	        ret_values.append('5')
	elif ((m == 1) or (m == 3) or (m == 5) or (m == 7) or (m == 8) or (m == 10) or (m == 12)):
	    if ((d == 6) or (d == 7)):
	        ret_values.append('6')
	    else:
	        ret_values.append('5')

	return ret_values
