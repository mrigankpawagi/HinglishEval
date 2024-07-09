def smallest_change(arr):
    changes = 0
    i = 0
    j = len(arr) - 1
    while i <= j:
        if arr[i] != arr[j]:
            changes += 1
        i += 1
        j -= 1
    return changes