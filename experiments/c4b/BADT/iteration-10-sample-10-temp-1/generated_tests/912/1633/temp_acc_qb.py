def patched_func(*args):
	global_list = []
	
	string = args[0]
	numbers = string.split(' ')
	problems = int(numbers[0])
	minutes = int(numbers[1])
	total = 0
	i = 0
	while ((total <= (240 - minutes)) and (i <= problems)):
	    i += 1
	    total += (i * 5)
	global_list.append((i - 1))
	return global_list