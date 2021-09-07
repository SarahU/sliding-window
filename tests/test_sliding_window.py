import pytest
from src.max_sum import max_sum_brute_force,\
                        max_sum_sliding_window

from src.smallest_contigous_subarray import smallest_contiguos_subarray_sum_over_s_brute_force, \
                        smallest_contiguos_subarray_sum_over_s_sliding_window


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


def test_smallest_contigous_array_sum_over_s_brute_force():
    input = [13, 32, 7, 21, 45, 19]
    actual_result = smallest_contiguos_subarray_sum_over_s_brute_force(input, 60)

    expected_result = 2
    assert actual_result == expected_result


# def test_smallest_contigous_array_sum_over_s_sliding_window():
#     input = [13, 32, 7, 21, 45, 19]
#     actual_result = smallest_contiguos_subarray_sum_over_s_sliding_window(input, 60)
#
#     expected_result = 2
#     assert actual_result == expected_result