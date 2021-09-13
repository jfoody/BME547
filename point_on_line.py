def main_interface():
	[point_one, point_two, x_new] = get_user_inputs()
	y_coord = find_y_coord(point_one, point_two, x_new)
	print_outputs(y_coord)


def get_user_inputs():
	print('Enter line coordinates in the format: [0, 0]')
	print('For point 1 what is the:')
	x1 = float(input('x coordinate '))
	y1 = float(input('y coordinate '))
	point_one = [x1, y1]
	print('For point 2 what is the:')
	x2 = float(input('x coordinate '))
	y2 = float(input('y coordinate '))
	point_two = [x2, y2]
	x_new = float(input("What is the x coordinate of the new point? "))
	return point_one, point_two, x_new


def find_line_slope(point_one, point_two):
	slope = (point_two[1] - point_one[1]) / (point_two[0] - point_one[0])
	return slope


def find_line_intercept(point_one, slope):
	intercept = point_one[1] - slope * point_one[0]
	return intercept


def find_y_coord(point_one, point_two, x_new):
	m = find_line_slope(point_one, point_two)
	b = find_line_intercept(point_one, m)
	y_coord = m * x_new + b
	return y_coord


def print_outputs(y_coord):
	print('The y value on the point on the line is {}'.format(y_coord))


if __name__ == '__main__':
	main_interface()
