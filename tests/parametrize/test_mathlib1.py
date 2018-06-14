import mathlib1
import pytest

@pytest.mark.parametrize("test_input, expected_output",
                         [
                             (5,25),
                             (9,81),
                             (10,100)
                         ])
def test_calc_sqaure(test_input, expected_output):
    result = mathlib1.calc_square(test_input)
    assert result == expected_output

