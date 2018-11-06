def pset(arr):
    if not len(arr):
        return [[]]

    last = arr[-1]
    rest = pset(arr[:-1])
    return rest + [el + [last] for el in rest]


def permutations(arr):
    arr_len = len(arr)
    if arr_len == 1:
        return [arr]
    elif arr_len == 0:
        return [[]]

    perms = []
    for perm in permutations(arr[1:]):
        for i in range(arr_len):
            perms.append(perm[:i] + arr[0:1] + perm[i:])
    return perms


def combinations(arr, comb_len):
    return [i for i in pset(arr) if len(i) == comb_len]


def rotate(arr, degree):
    pivot = degree % len(arr)
    return arr[pivot:] + arr[:pivot]


def flatten(arr, level=0):
    flattened = []
    for el in arr:
        if isinstance(el, list):
            if level > 0:
                flattened.append(flatten(el, level - 1))
            else:
                flattened.extend(flatten(el))
        else:
            flattened.append(el)
    return flattened
