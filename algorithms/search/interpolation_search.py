def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high and arr[low] <= target <= arr[high]:
        if arr[high] == arr[low]:
            if arr[low] == target:
                return low
            else:
                return -1

        pos = low + ((target - arr[low]) * (high - low) // (arr[high] - arr[low]))

        if pos < 0 or pos >= len(arr):
            return -1

        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1
