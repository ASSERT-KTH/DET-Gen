def func(*args):
	
	
	def ginp():
	    return map(int, args[0].split())
	n = (int(args[1]) % 6)
	x = int(args[2])
	m = [[0, 1, 2], [1, 0, 2], [1, 2, 0], [2, 1, 0], [2, 0, 1], [0, 2, 1]]
	return(m[n][x])
