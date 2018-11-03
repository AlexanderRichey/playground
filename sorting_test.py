import unittest
import random

from sorting import merge_sort, quick_sort

class TestSortingFunctions(unittest.TestCase):
    def test_merge_sort(self):
        arr = [random.randint(0, 1000) for i in range(100)]
        self.assertEqual(sorted(arr), merge_sort(arr))

    def test_merge_sort_cb(self):
        arr = [random.randint(0, 1000) for i in range(100)]
        cb = lambda a, b : a > b
        self.assertEqual(list(reversed(sorted(arr))), merge_sort(arr, cb))

    def test_quick_sort(self):
        arr = [random.randint(0, 1000) for i in range(100)]
        self.assertEqual(sorted(arr), quick_sort(arr))

    def test_quick_sort_cb(self):
        arr = [random.randint(0, 1000) for i in range(100)]
        cb = lambda a, b : a > b
        self.assertEqual(list(reversed(sorted(arr))), quick_sort(arr, cb))

if __name__ == '__main__':
    unittest.main()
