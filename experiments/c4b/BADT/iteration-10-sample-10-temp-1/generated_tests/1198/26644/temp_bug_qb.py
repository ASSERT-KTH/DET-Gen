def original_func(*args):
	global_list = []
	
	word = args[0]
	global_list.append(('YES' if ((word.find(chr(72)) > (- 1)) or (word.find(chr(81)) > (- 1)) or (word.find('+') > (- 1)) or (word.find('9') > (- 1))) else 'NO'))
	return global_list