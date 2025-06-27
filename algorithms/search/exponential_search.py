def binary_search(arr, target, left, right):
    while left < right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return -1

def exponential_search(arr, target):
    if len(arr) == 0:
        return -1
    if arr[0] == target:
        return 0

    index = 1
    while index < len(arr) and arr[index] <= target:
        index *= 2

    return binary_search(arr, target, index // 2, min(index, len(arr)))