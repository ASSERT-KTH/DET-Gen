def original_func(*args):
	global_list = []
	
	(l, r) = list(map(int, args[0].split()))
	if (r == 0):
	    global_list.append('NO')
	else:
	    global_list.append(('YES' if (abs((l - r)) <= 1) else 'NO'))
	return global_list