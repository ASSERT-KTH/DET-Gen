def func(*args):
	ret_values = []
	
	(n, m, k) = map(int, args[0].split())
	m -= n
	soon = False
	summ = 0
	g = 1
	i = 0
	for i in range(1, (1 + min((n - k), (k - 1)))):
	    summ += g
	    g += 2
	    if (summ > m):
	        soon = True
	        break
	if (not soon):
	    for i in range((1 + min((n - k), (k - 1))), (1 + max((n - k), (k - 1)))):
	        summ += g
	        g += 1
	        if (summ > m):
	            soon = True
	            break
	ret_values.append((i if soon else ((1 + i) + ((m - summ) // n))))

	return ret_values
