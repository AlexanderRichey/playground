import unittest
import itertools
import random

from array import (
    pset,
    permutations,
    combinations,
    rotate,
    flatten,
    select,
    reject,
    all,
    some,
    none,
    map,
    reduce,
    zip,
)


class TestCombinationFunctions(unittest.TestCase):
    def test_pset(self):
        arr = [1, 2, 3]
        ans = [[], [1], [2], [3], [2, 3], [1, 2], [1, 3], [1, 2, 3]]
        power_set = pset(arr)
        self.assertCountEqual(power_set, ans)

    def test_permutations(self):
        arr = [random.randint(0, 1000) for _ in range(3)]
        ans = [list(i) for i in list(itertools.permutations(arr))]
        perms = permutations(arr)
        self.assertCountEqual(perms, ans)

    def test_combinations(self):
        arr = [random.randint(0, 1000) for _ in range(5)]
        ans = [list(i) for i in list(itertools.combinations(arr, 3))]
        combos = combinations(arr, 3)
        sans = [sorted(list(el)) for el in ans]
        scombos = [sorted(el) for el in combos]
        self.assertCountEqual(scombos, sans)

    def test_rotate(self):
        arr = [i for i in range(10)]
        ans = [5, 6, 7, 8, 9, 0, 1, 2, 3, 4]
        self.assertListEqual(rotate(arr, 5), ans)

    def test_flatten(self):
        arr = [[1], [[[3, 4], 5]], 5]
        self.assertListEqual(flatten(arr), [1, 3, 4, 5, 5])
        self.assertListEqual(flatten(arr, 1), [[1], [3, 4, 5], 5])
        self.assertListEqual(flatten(arr, 3), [[1], [[[3, 4], 5]], 5])

    def test_select(self):
        arr = [i for i in range(10)]
        ans = [0, 2, 4, 6, 8]
        cb = lambda a: a % 2 == 0
        self.assertListEqual(select(arr, cb), ans)

    def test_reject(self):
        arr = [i for i in range(10)]
        ans = [1, 3, 5, 7, 9]
        cb = lambda a: a % 2 == 0
        self.assertListEqual(reject(arr, cb), ans)

    def test_all(self):
        arr = [i for i in range(10)]
        cb = lambda a: a % 1 == 0
        self.assertTrue(all(arr, cb))

    def test_some(self):
        arr = [i for i in range(10)]
        cb = lambda a: a == 8
        self.assertTrue(some(arr, cb))
        cb = lambda a: a == -1
        self.assertFalse(some(arr, cb))

    def test_none(self):
        arr = [i for i in range(10)]
        cb = lambda a: a == 8
        self.assertFalse(none(arr, cb))
        cb = lambda a: a == -1
        self.assertTrue(none(arr, cb))

    def test_map(self):
        arr = [i for i in range(10)]
        ans = [str(i) for i in arr]
        cb = lambda a: str(a)
        self.assertListEqual(map(arr, cb), ans)

    def test_reduce(self):
        arr = [i for i in range(10)]
        ans = 45
        cb = lambda acc, val: acc + val
        self.assertEqual(reduce(arr, cb), ans)

        initial = 10
        self.assertEqual(reduce(arr, cb, initial), ans + initial)

    def test_zip(self):
        arr = [i for i in range(10)]
        ans = [
            [0, 0],
            [1, 1],
            [2, 2],
            [3, 3],
            [4, 4],
            [5, 5],
            [6, 6],
            [7, 7],
            [8, 8],
            [9, 9],
        ]
        self.assertListEqual(zip(arr, arr), ans)

        ans = [
            [0, 1, 2],
            [1, 2, 3],
            [2, 3, 4],
            [3, 4, 5],
            [4, 5, 6],
            [5, 6, 7],
            [6, 7, 8],
            [7, 8, 9],
            [8, 9, 10],
            [9, 10, 11],
        ]
        self.assertListEqual(
            zip(list(range(10)), list(range(1, 11)), list(range(2, 12))), ans
        )
