def func(*args):
	ret_values = []
	
	a = [1 for i in range(26)]
	c = 0
	s = args[0]
	for l in s:
	    if a[(ord(l) - 97)]:
	        c += 1
	        a[(ord(l) - 97)] = 0
	if ((c % 2) == 1):
	    ret_values.append('IGNORE HIM!')
	else:
	    ret_values.append('CHAT WITH HER!')

	return ret_values
