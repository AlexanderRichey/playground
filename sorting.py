def msort(arr, cb=lambda a, b: a < b):
    arr_len = len(arr)
    if arr_len <= 1:
        return arr

    middle = int(arr_len / 2)
    left = arr[:middle]
    right = arr[middle:]

    return _merge(msort(left, cb), msort(right, cb), cb)


def _merge(left, right, cb):
    merged = []

    while len(left) and len(right):
        if cb(left[0], right[0]):
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))

    return merged + left + right


def qsort(arr, cb=lambda a, b: a < b):
    arr_len = len(arr)
    if arr_len == 0:
        return []
    elif arr_len == 1:
        return arr

    middle = int(arr_len / 2)
    pivot = arr.pop(middle)

    left = []
    right = []
    while len(arr):
        val = arr.pop()
        if cb(val, pivot):
            left.append(val)
        else:
            right.append(val)

    return qsort(left, cb) + [pivot] + qsort(right, cb)
