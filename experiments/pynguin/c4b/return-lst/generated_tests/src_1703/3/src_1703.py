def func(*args):
	ret_values = []
	
	s = args[0]
	ans = s[0]
	for i in range(1, len(s)):
	    if ((s[(i - 1)] == '/') and (s[i] == '/')):
	        continue
	    ans += s[i]
	if ((ans[(- 1)] == '/') and (len(ans) > 1)):
	    ret_values.append(ans[:(- 1)])
	else:
	    ret_values.append(ans)

	return ret_values
