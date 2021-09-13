import pytest


# test functionality of point_on_line.py
@pytest.mark.parametrize('point_one, point_two, new_x, expected', [
    [0, 0], [10,10], 3, 3])
def test_point_on_line(point_one, point_two, new_x, expected):
    from point_on_line import find_y_coord
    answer = find_y_coord(point_one, point_two, new_x)
    assert answer == expected