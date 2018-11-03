import unittest
import random

from sorting import msort, qsort


class TestSortingFunctions(unittest.TestCase):
    def test_msort(self):
        arr = [random.randint(0, 1000) for i in range(100)]
        self.assertEqual(sorted(arr), msort(arr))

    def test_msort_cb(self):
        arr = [random.randint(0, 1000) for i in range(100)]
        cb = lambda a, b: a > b
        self.assertEqual(list(reversed(sorted(arr))), msort(arr, cb))

    def test_qsort(self):
        arr = [random.randint(0, 1000) for i in range(100)]
        self.assertEqual(sorted(arr), qsort(arr))

    def test_qsort_cb(self):
        arr = [random.randint(0, 1000) for i in range(100)]
        cb = lambda a, b: a > b
        self.assertEqual(list(reversed(sorted(arr))), qsort(arr, cb))


if __name__ == "__main__":
    unittest.main()
