def sliding_window_brute_force_max_sum(arr, k):
    max: int = len(arr)
    max_total: int = 0

    for i in range(0, max):
        if i+k < max:
            total = 0
            for j in range(0, k):
                total += arr[i+j]
            if max_total < total:
                max_total = total

    return max_total

# def sliding_window_brute_force_all_totals():
#     return 0
#
# input = [12, 20, 36, 4, 18, 8]
#     k = 3