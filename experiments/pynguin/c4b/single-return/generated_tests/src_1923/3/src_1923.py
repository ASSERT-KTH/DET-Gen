def func(*args):
	
	(n, k) = [int(x) for x in args[0].split()]
	p = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	s = ''
	l = 0
	for i in range(n):
	    s += p[l]
	    l += 1
	    if (l == k):
	        l = 0
	return(s)
