def original_func(*args):
	global_list = []
	
	b = ([0] * 4)
	b[0] = int(args[0])
	b[1] = int(args[1])
	b[2] = int(args[2])
	b[3] = int(args[3])
	d = int(args[4])
	a = []
	if (1 in b):
	    global_list.append(d)
	else:
	    l = 0
	    for i in range(1, (d + 1)):
	        for j in range(4):
	            if ((i % b[j]) == 0):
	                l += 1
	                break
	    global_list.append(len(a))
	return global_list