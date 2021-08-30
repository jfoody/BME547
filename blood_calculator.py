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
			HDL_Driver()

	print(choice)
	return choice

def HDL_Driver():
	HDL_value = hdl_input()
	HDL_character = hdl_analysis(HDL_value)
	print('test')
	hdl_output(HDL_value,HDL_character)

def hdl_input():
	hdl_value = int(input('Enter HDL value: '))
	return hdl_value

def hdl_analysis(HDL_value):
	if HDL_value >= 60:
		return 'Normal'
	elif 40 <= HDL_value < 60:
		return 'Borderline low'
	else:
		return 'Low'

def hdl_output(HDL_value, HDL_answer):
	print('The HDL value of {} is considered {}'.format(HDL_value,HDL_answer))
	return

interface()

