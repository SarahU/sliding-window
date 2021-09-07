# brute-force and sliding windows solution for problem:
# Find the subset of k consecutive items that has the maximum sum

def max_sum_brute_force(arr, k):
    max_total: int = 0

    # remember that range() is up to and excluding
    for i in range(0, len(arr) - k + 1):
            total = 0
            for j in range(i, i + k):
                total += arr[j]
            if max_total < total:
                max_total = total

    return max_total


def max_sum_sliding_window(arr, k):
    total: int = 0

    # total of first window
    for i in range(0, k):
        total += arr[i]
    max_total = total

    # rest of the collection
    # keep a running total by removing the element not in the window
    # and by adding the element that is in the window
    for i in range(k, len(arr)):
        total -= arr[i-k]  # remove element out of window
        total += arr[i]  # add element within window
        if max_total < total:
            max_total = total

    return max_total


def smallest_contigous_array_sum_over_s_brute_force(arr, s):
    return 0


def smallest_contigous_array_sum_over_s_sliding_window(arr, s):
    return 0
