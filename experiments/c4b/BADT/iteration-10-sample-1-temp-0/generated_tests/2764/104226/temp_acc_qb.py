def patched_func(*args):
	global_list = []
	
	import math
	(n, z) = map(int, args[0].split())
	S = []
	k = 2
	q = round(math.sqrt(n))
	while (k <= q):
	    if ((n % k) == 0):
	        S.append(k)
	        n //= k
	        q = round(math.sqrt(n))
	    else:
	        k += 1
	S.append(n)
	s = ''
	p = 1
	if (len(S) < z):
	    global_list.append((- 1))
	elif (z > 1):
	    for a in range((z - 2)):
	        s += (str(S[a]) + ' ')
	    s += str(S[(z - 2)])
	    for b in range((z - 1), len(S)):
	        p *= S[b]
	    if (p > 1):
	        s += (' ' + str(p))
	    global_list.append(s)
	else:
	    p = 1
	    for c in S:
	        p *= c
	    global_list.append(p)
	return global_list