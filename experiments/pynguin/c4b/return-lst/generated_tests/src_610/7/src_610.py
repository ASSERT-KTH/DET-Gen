def func(*args):
	ret_values = []
	
	ret_values.append(['Washington', 'Adams', 'Jefferson', 'Madison', 'Monroe', 'Adams', 'Jackson', 'Van Buren', 'Harrison', 'Tyler', 'Polk', 'Taylor', 'Fillmore', 'Pierce', 'Buchanan', 'Lincoln', 'Johnson', 'Grant', 'Hayes', 'Garfield', 'Arthur', 'Cleveland', 'Harrison', 'Cleveland', 'McKinley', 'Roosevelt', 'Taft', 'Wilson', 'Harding', 'Coolidge', 'Hoover', 'Roosevelt', 'Truman', 'Eisenhower', 'Kennedy', 'Johnson', 'Nixon', 'Ford', 'Carter', 'Reagan'][(int(args[0]) - 1)])

	return ret_values
