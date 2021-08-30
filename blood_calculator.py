def interface():
	print('Blood calculator')
	keeprunning = True
	while keeprunning:
		print('make a choice')
		print('1-HDL analysis')
		print('2-LDL analysis')
		print('9 - quit')
		choice = int(input('Enter your choice: '))

		if choice==9:
			keeprunning = False
		elif choice==1:
			HDL_Driver()
		elif choice==2:
			LDL_Driver()

	print(choice)
	return choice

# HDL level checker
def HDL_Driver():
	HDL_value = hdl_input()
	HDL_character = hdl_analysis(HDL_value)
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


# LDL level checker
def LDL_Driver():
	LDL_value = ldl_input()
	ldl_level = ldl_analysis(LDL_value)
	print('The LDL value of {} is considered {}'.format(LDL_value,ldl_level))

def ldl_input():
	ldl_level = int(input('Enter LDL level: '))
	return ldl_level

def ldl_analysis(level):
	if level<130:
		return 'Normal'
	elif 130 <= level <= 159:
		return 'borderline high'
	elif 159 < level <190:
		return 'high'
	else:
		return 'very high'


interface()

