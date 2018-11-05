import unittest

from stack import Stack


class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_push(self):
        for i in range(10):
            self.stack.push(i)
        self.assertEqual(self.stack.size, 10)

    def test_pop(self):
        arr = [i for i in range(10)]
        for i in arr:
            self.stack.push(i)
        out = []
        for i in arr:
            out.append(self.stack.pop())
        self.assertEqual(arr, list(reversed(out)))

    def test_is_empty(self):
        self.stack.push(1)
        self.assertFalse(self.stack.is_empty)
        self.stack.pop()
        self.assertTrue(self.stack.is_empty)
