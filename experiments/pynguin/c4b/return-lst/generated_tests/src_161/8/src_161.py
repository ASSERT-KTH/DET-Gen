def func(*args):
	ret_values = []
	
	'input\n1 1 1\n'
	(s1, s2, s3) = map(int, args[0].split())
	(a, b, c) = (((s1 * s3) // s2), ((s1 * s2) // s3), ((s2 * s3) // s1))
	ret_values.append(int((4 * (((a ** 0.5) + (b ** 0.5)) + (c ** 0.5)))))

	return ret_values
