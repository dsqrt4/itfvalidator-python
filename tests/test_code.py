import pytest
import itf.code as code


@pytest.mark.parametrize("i25,expected", [
    (310,                  (31, 0)),
    (2011,                 (201, 1)),
    (800372,               (80037, 2)),
    (800303,               (80030, 3)),
    (1234567895,           (123456789, 5)),
    (48014125513241384938, (4801412551324138493, 8)),
])
def split_code(i25, expected):
    assert expected == code.split_code(i25)


@pytest.mark.parametrize("expected,i25", [
    (True, 310),
    (True, 2011),
    (True, 1234567895),
    (True, 48014125513241384938),
    (False, 311),
    (False, 2012),
    (False, 123456780),
    (False, 4801412551324138499),
])
def test_validate_code(expected, i25):
    assert expected == code.validate_code(i25)
