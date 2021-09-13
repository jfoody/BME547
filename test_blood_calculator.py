import pytest


@pytest.mark.parametrize('HDL_value, expected', [
    (65, 'Normal'),
    (45, 'Borderline low'),
    (15, 'Low'),
    (70, 'Normal')])    # must be identical to the function def
def test_hdl_analysis(HDL_value, expected):
    from blood_calculator import hdl_analysis
    answer = hdl_analysis(HDL_value)
    assert answer == expected
