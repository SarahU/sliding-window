import pytest
from src.sliding_window import max_sum_brute_force \
                              ,max_sum_sliding_window


def test_max_sum_brute_force():
    input = [18, 8, 4, 20, 36, 12]
    k = 3
    actual_result = max_sum_brute_force(input, k)

    expected_result = 68
    assert actual_result == expected_result


# def test_max_sum
# _sliding_window():
#     input = [4, 20, 36, 12, 18, 8]
#     k = 3
#     actualResult = max_sum_sliding_window(input, k)
#
#     expectedResult = 68
#     assert expectedResult == actualResult


# def test_sliding_window_brute_force_max_sum():
#     input = [4, 20, 36, 12, 18, 8]
#     k = 3
#     actualResult = sliding_window_brute_force_all_totals(input, k)
#
#     expectedResult = [68, 60, 58]
#     assert expectedResult == actualResult
