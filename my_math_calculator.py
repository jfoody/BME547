def sqrt(n):

	if n <= 0:
		raise ValueError('sqrt function cannot recieve a negative value')

	x = n
	y = 1

	# pick an accuracy level, e
	e = 0.000001
	while(x-y > e):
		x = (x+y)/2
		y = n / x

	return x


def add_positive_ints(a, b):
	if a < 0 or b < 0:
		raise ValueError('Cannot add negative numbers')
	if type(a) is not int or type(b) is not int:
		raise TypeError('Cannot add non-ints')
	return a + b