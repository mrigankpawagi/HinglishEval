def maximum(arr, k):
    arr.sort()
    return arr[-k:] if k <= len(arr) else arr