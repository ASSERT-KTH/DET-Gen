def func(*args):
	
	import sys
	import math
	
	def main():
	    stdin = [int(x) for x in sys.stdin.read().split()]
	    min_tot_dist(stdin)
	
	def min_tot_dist(A):
	    min_dist = math.inf
	    for a in A:
	        temp = sum([abs((x - a)) for x in A])
	        min_dist = min(min_dist, temp)
	    return(min_dist)
	if (__name__ == '__main__'):
	    main()
