def original_func(*args):
	global_list = []
	
	s = args[0]
	if (('H' in s) or ('Q' in s)):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list