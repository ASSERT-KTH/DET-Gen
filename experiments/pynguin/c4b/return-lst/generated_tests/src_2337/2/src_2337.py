def func(*args):
	ret_values = []
	
	'th, hu, do, un = map(str, input())\nyear = int(th + hu + do + un)'
	year = int(args[0])
	for i in range((year + 1), 9100):
	    i = str(i)
	    if ((i[0] != i[1]) and (i[2] != i[3]) and (i[1] != i[3]) and (i[0] != i[2]) and (i[1] != i[2]) and (i[0] != i[3])):
	        ret_values.append(i)
	        break

	return ret_values
