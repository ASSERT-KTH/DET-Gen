def func(*args):
	ret_values = []
	
	s = args[0]
	if ((len(s) % 2) == 0):
	    l = (len(s) // 2)
	    r = l
	else:
	    l = (len(s) // 2)
	    r = (1 + 1)
	(l_s, r_s) = (s[:l], s[r:][::(- 1)])
	num = 0
	for (i, c) in enumerate(l_s):
	    if (l_s[i] != r_s[i]):
	        num += 1
	if (num > 1):
	    ret_values.append('NO')
	elif (((len(s) % 2) == 0) and (num == 0)):
	    ret_values.append('NO')
	else:
	    ret_values.append('YES')

	return ret_values
