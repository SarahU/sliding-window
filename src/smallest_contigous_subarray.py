# brute-force and sliding windows solution for problem:
# Find the minimal length of a contiguous sub-array of which the sum ≥ s.

def smallest_contiguos_subarray_sum_over_s_brute_force(arr, s):
    smallest_element_count = len(arr) + 1

    for i in range(0, len(arr)):
        local_sum = 0
        element_count = 0
        for j in range(i, len(arr) - 1):
            local_sum += arr[j]
            element_count += 1
            if local_sum >= s:
                if element_count < smallest_element_count:
                    smallest_element_count = element_count

    if smallest_element_count == (len(arr) + 1):
        return 0

    return smallest_element_count


def smallest(a, b):
    if a >= b:
        return a
    else:
        return b


def smallest_contiguos_subarray_sum_over_s_sliding_window(arr, s):
    smallest_element_count = len(arr) + 1
    local_sum = 0  # keep track of running total
    start = 0  # beginning of window

    for end in range(0, len(arr)):  # end is the end of the window
        local_sum = local_sum + arr[end]
        while local_sum >= s:  # condition is met
            smallest_element_count = min(smallest_element_count, end + 1 - start)
            local_sum = local_sum - arr[start]
            start = start + 1

    if smallest_element_count == (len(arr) + 1):
        return 0

    return smallest_element_count


def smallest_contiguos_subarray_sum_over_s_sliding_window_with_output(arr, s):
    smallest_element_count = len(arr) + 1
    local_sum = 0  # keep track of running total
    start = 0  # beginning of window

    for end in range(0, len(arr)):  # end is the end of the window
        print("In outer, end = ", end)
        local_sum = local_sum + arr[end]
        print("local_sum = ", local_sum)
        while local_sum >= s:  # condition is met
            print("condition met!")
            smallest_element_count = min(smallest_element_count, end + 1 - start)
            print("smallest_element_count=", smallest_element_count)
            local_sum = local_sum - arr[start]
            print("local_sum=", local_sum)
            start = start + 1
            print("start=", start)

    if smallest_element_count == (len(arr) + 1):
        return 0

    return smallest_element_count
