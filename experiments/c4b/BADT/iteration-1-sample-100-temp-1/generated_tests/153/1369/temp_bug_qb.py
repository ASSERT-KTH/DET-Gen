def original_func(*args):
	global_list = []
	
	n = int(args[0])
	global_list.append(int((((n / 2) - 1) / 2)))
	return global_list