import pytest
import itf.check_digit as check_digit


@pytest.mark.parametrize("code,expected", [
    (31,                  0),
    (201,                 1),
    (80037,               2),
    (80030,               3),
    (123456789,           5),
    (4801412551324138493, 8),
])
def test_calculate_check_digit(code, expected):
    assert expected == check_digit.calculate_check_digit(code)


@pytest.mark.parametrize("code,expected", [
    (31,                  310),
    (201,                 2011),
    (80037,               800372),
    (80030,               800303),
    (123456789,           1234567895),
    (4801412551324138493, 48014125513241384938),
])
def test_append_check_digit(code, expected):
    assert expected == check_digit.append_check_digit(code)
