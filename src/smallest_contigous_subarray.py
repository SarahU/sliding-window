# brute-force and sliding windows solution for problem:
# Find the minimal length of a contiguous sub-array of which the sum ≥ s.

def smallest_contiguos_subarray_sum_over_s_brute_force(arr, s):
    smallest_element_count = len(arr) + 1

    for i in range(0, len(arr)):
        local_sum = 0
        element_count = 0
        for j in range(i, len(arr)-1):
            local_sum += arr[j]
            element_count += 1
            if local_sum >= s:
                if element_count < smallest_element_count:
                    smallest_element_count = element_count

    if smallest_element_count == (len(arr) + 1):
        return 0

    return smallest_element_count


def smallest_contiguos_subarray_sum_over_s_sliding_window(arr, s):
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
