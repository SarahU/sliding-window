import pytest
from src.sliding_window import max_sum_brute_force \
                              ,max_sum_sliding_window


def test_max_sum_brute_force():
    input = [18, 8, 4, 20, 36, 12]
    k = 3
    actual_result = max_sum_brute_force(input, k)

    expected_result = 68
    assert actual_result == expected_result


def test_max_sum_sliding_window():
    input = [18, 8, 4, 20, 36, 12]
    k = 3
    actual_result = max_sum_sliding_window(input, k)

    expected_result = 68
    assert actual_result == expected_result

