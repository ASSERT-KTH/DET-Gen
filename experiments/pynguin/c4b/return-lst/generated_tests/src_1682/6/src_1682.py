def func(*args):
	ret_values = []
	
	list = args[0]
	list = list.split(sep=' ')
	a = eval(list[0])
	b = eval(list[1])
	c = eval(list[2])
	d = eval(list[3])
	if ((((a + b) > c) and ((a + c) > b) and ((b + c) > a)) or (((a + b) > d) and ((a + d) > b) and ((b + d) > a)) or (((c + b) > d) and ((c + d) > b) and ((b + d) > c)) or (((a + c) > d) and ((a + d) > c) and ((c + d) > a))):
	    ret_values.append('TRIANGLE')
	elif (((a + b) == c) or ((a + c) == b) or ((c + b) == a) or ((a + b) == d) or ((a + d) == b) or ((b + d) == a) or ((a + c) == d) or ((a + d) == c) or ((c + d) == a) or ((b + c) == d) or ((b + d) == c) or ((c + d) == b)):
	    ret_values.append('SEGMENT')
	else:
	    ret_values.append('IMPOSSIBLE')

	return ret_values
