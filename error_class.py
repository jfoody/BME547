def test_fcn():
	try:
		from my_math_calculator import sqrt
	except ModuleNotFoundError:
		from math import sqrt

	x = sqrt(4)
	print(x)


def main():
	test_fcn()
	from my_math_calculator import add_positive_ints
	try:
		x = add_positive_ints(-2, 3)
		print(x)
	except ValueError as e:
		print(e)
	except TypeError:
		print('got TypeError')
	# except:
	# 	print('All other errors')


if __name__ == '__main__':
	main()