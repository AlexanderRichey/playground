import unittest
import random

from bsearch import bsearch


class TestBinarySearch(unittest.TestCase):
    def test_bsearch_positive(self):
        for _ in range(100):
            arr = sorted(list(set([random.randint(0, 1000) for _ in range(100)])))
            idx = random.randint(0, len(arr) - 1)
            target = arr[idx]
            result = bsearch(arr, target)
            self.assertEqual(result, idx)

    def test_bsearch_negative(self):
        for _ in range(100):
            arr = sorted(list(set([random.randint(0, 1000) for _ in range(100)])))
            while True:
                target = random.randint(0, 10000)
                if target not in arr:
                    break
            result = bsearch(arr, target)
            self.assertEqual(result, None)
