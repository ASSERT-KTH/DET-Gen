def func(*args):
	ret_values = []
	
	import math
	import re
	from fractions import Fraction
	from collections import Counter
	
	class Task():
	    (a, b) = (0, 0)
	    answer = 0
	
	    def __init__(self):
	        (self.a, self.b) = [x for x in args[0].split()]
	
	    def solve(self):
	        (a, b) = (self.a, self.b)
	        self.answer = (int(a) + int(b[::(- 1)]))
	
	    def printAnswer(self):
	        ret_values.append(self.answer)
	task = Task()
	task.solve()
	task.printAnswer()

	return ret_values
