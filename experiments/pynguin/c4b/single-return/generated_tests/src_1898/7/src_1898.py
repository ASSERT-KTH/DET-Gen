def func(*args):
	
	from sys import stdin
	
	def main():
	    uno = 'I hate'
	    dos = 'I love'
	    n = int(stdin.readline().strip())
	    i = 1
	    res = 'I hate'
	    while (i < n):
	        if ((i % 2) == 0):
	            res = ((res + ' that ') + uno)
	        else:
	            res = ((res + ' that ') + dos)
	        i += 1
	    return((res + ' it'))
	main()
