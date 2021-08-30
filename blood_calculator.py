def interface():
	print('Blood calculator')
	keeprunning = True
	while keeprunning:
		print('make a choice')
		print('1-HDL analysis')
		print('9 - quit')
		choice = int(input('Enter your choice: '))

		if choice==9:
			keeprunning = False
		elif choice==1:
			HDL_driver()

	print(choice)
	return choice

interface()

# def HDL_driver():
# 	hdl_input()
# 	hdl_analysis()
# 	hdl_output()

# def HDL_input():
