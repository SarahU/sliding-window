import pytest
from src.sliding_window import sliding_window_brute_force_max_sum \
    # , sliding_window_brute_force_all_totals


def test_sliding_window_brute_force_max_sum():
    input = [12, 20, 36, 4, 18, 8]
    k = 3
    actualResult = sliding_window_brute_force_max_sum(input, k)

    expectedResult = 68
    assert expectedResult == actualResult


# def test_sliding_window_brute_force_max_sum():
#     input = [12, 20, 36, 4, 18, 8]
#     k = 3
#     actualResult = sliding_window_brute_force_all_totals()
#
#     expectedResult = [68, 60, 58]
#     assert expectedResult == actualResult
