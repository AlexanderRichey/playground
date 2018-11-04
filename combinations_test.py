import unittest
import itertools
import random

from combinations import pset, permutations, combinations


class TestCombinationFunctions(unittest.TestCase):
    def test_pset(self):
        arr = [1, 2, 3]
        ans = [[], [1], [2], [3], [2, 3], [1, 2], [1, 3], [1, 2, 3]]
        power_set = pset(arr)
        self.assertTrue(all(el in ans for el in power_set))
        self.assertTrue(all(el in power_set for el in ans))

    def test_permutations(self):
        arr = [random.randint(0, 1000) for _ in range(3)]
        ans = list(itertools.permutations(arr))
        perms = permutations(arr)
        self.assertTrue(all(tuple(el) in ans for el in perms))
        self.assertTrue(all(list(el) in perms for el in ans))

    def test_combinations(self):
        arr = [random.randint(0, 1000) for _ in range(5)]
        ans = list(itertools.combinations(arr, 3))
        combos = combinations(arr, 3)
        sans = [sorted(list(el)) for el in ans]
        scombos = [sorted(el) for el in combos]
        print(sans)
        print(scombos)
        self.assertTrue(all(el in scombos for el in sans))
        self.assertTrue(all(el in sans for el in scombos))
