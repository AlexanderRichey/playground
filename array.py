from typing import Callable, Any


def pset(arr: list) -> list:
    if not len(arr):
        return [[]]

    last = arr[-1]
    rest = pset(arr[:-1])
    return rest + [el + [last] for el in rest]


def permutations(arr: list) -> list:
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


def combinations(arr: list, comb_len: int) -> list:
    return [i for i in pset(arr) if len(i) == comb_len]


def rotate(arr: list, degree: int) -> list:
    pivot = degree % len(arr)
    return arr[pivot:] + arr[:pivot]


def flatten(arr: list, level: int = 0) -> list:
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


def first_index(arr: list, cb: Callable[[Any], bool]) -> int:
    for i, v in enumerate(arr):
        if cb(v):
            return i
    return -1


def select(arr: list, cb: Callable[[Any], bool]) -> list:
    return [i for i in arr if cb(i)]


def select_indicies(arr: list, cb: Callable[[Any], bool]) -> list:
    return [i for i, v in enumerate(arr) if cb(v)]


def reject(arr: list, cb: Callable[[Any], bool]) -> list:
    return [i for i in arr if not cb(i)]


def reject_indicies(arr: list, cb: Callable[[Any], bool]) -> list:
    return [i for i, v in enumerate(arr) if not cb(v)]


def all(arr: list, cb: Callable[[Any], bool]) -> bool:
    for i in arr:
        if not cb(i):
            return False
    return True


def some(arr: list, cb: Callable[[Any], bool]) -> bool:
    for i in arr:
        if cb(i):
            return True
    return False


def none(arr: list, cb: Callable[[Any], bool]) -> bool:
    for i in arr:
        if cb(i):
            return False
    return True


def map(arr: list, cb: Callable[[], Any]) -> list:
    return [cb(i) for i in arr]


def reduce(arr: list, cb: Callable[[Any, Any], Any], initial: Any = 0) -> Any:
    acc = initial
    for i in arr:
        acc = cb(acc, i)
    return acc


def zip(*arrs: list) -> list:
    zipper = []
    _, shortest = max(enumerate(arrs), key=lambda arr: len(arr[1]))
    for i in range(len(shortest)):
        zipper.append([arr[i] for arr in arrs])
    return zipper
