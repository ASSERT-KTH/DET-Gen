def func(*args):
	ret_values = []
	
	(r, g, b) = map(int, args[0].split())
	ret_values.append((max((3 * ((r - 1) // 2)), (1 + (3 * ((g - 1) // 2))), (2 + (3 * ((b - 1) // 2)))) + 30))

	return ret_values