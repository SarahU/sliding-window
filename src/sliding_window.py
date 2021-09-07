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
    return 0

#
# def sliding_window_brute_force_all_totals(arr, k):
#     max: int = len(arr)
#     totals: int[k]
#
#     for i in range(0, max):
#         if i + k < max:
#             total = 0
#             for j in range(0, k):
#                 total += arr[i + j]
#             totals[i] = total
#             print('totals[i]', totals[i], i)
#         else:
#             return totals

# input = [12, 20, 36, 4, 18, 8]
#     k = 3
