def _bsearch_cb(a, b):
    if a < b:
        return -1
    elif a == b:
        return 0
    elif a > b:
        return 1


def bsearch(arr, target, cb=_bsearch_cb):
    arr_len = len(arr)
    if not arr_len:
        return None

    probe = int(arr_len / 2)
    result = cb(target, arr[probe])

    if result == -1:
        return bsearch(arr[:probe], target)
    elif result == 0:
        return probe
    elif result == 1:
        start = probe + 1
        sub_result = bsearch(arr[start:], target)
        if sub_result is not None:
            return sub_result + start
        return sub_result
