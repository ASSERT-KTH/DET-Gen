def func(*args):
	ret_values = []
	
	word = ''
	arr_1 = ['A', 'O', 'Y', 'E', 'U', 'I']
	arr_2 = ['a', 'o', 'y', 'e', 'u', 'i']
	arr_3 = []
	string = args[0]
	arr = []
	arr_final = []
	count = 0
	for i in string:
	    arr.append(i)
	for i in arr:
	    if ((i not in arr_1) and (i not in arr_2)):
	        arr_final.append(i.lower())
	ret_values.append(('.' + '.'.join(arr_final)))

	return ret_values
