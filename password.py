password = '12345'
x = 3
while x > 0:
	x = x - 1
	pwd = input('Please enter your password:')
	if pwd == password:
		print('Welcome Back!')
		break
	else:
		print('Incorrect Password!')
		if x > 0:
			print('You have', x, 'more chances.')
		else:
			print('Too many failed login attempts. Please try again in 30 minutes.')

