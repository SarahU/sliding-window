import pytest
from src.sliding_window import sliding_window_brute_force_max_sum

def test_sliding_window_brute_force():
    input = [12, 20, 36, 4, 18, 8]
    k = 3
    actualResult = sliding_window_brute_force_max_sum()

    expectedResult = 1
    assert expectedResult == actualResult