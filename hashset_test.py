import unittest

from hashset import HashSet


class TestHashSet(unittest.TestCase):
    def setUp(self):
        self.hs = HashSet()

    def test_add(self):
        self.hs.add(1)
        self.hs.add("hello")
        self.assertTrue(1 in self.hs)
        self.assertTrue("hello" in self.hs)
        self.assertTrue("bye" not in self.hs)

    def test_remove(self):
        self.hs.add(1)
        self.hs.add("hello")
        self.assertTrue(1 in self.hs)
        self.hs.remove(1)
        self.assertTrue(1 not in self.hs)
        self.hs.remove("hello")
        self.assertTrue("hello" not in self.hs)

    def test_iter(self):
        for i in range(10):
            self.hs.add(i)
        out = []
        for i in self.hs:
            out.append(i)
        self.assertCountEqual(out, range(10))

    def test_len(self):
        for i in range(10):
            self.hs.add(i)
        self.assertEqual(len(self.hs), 10)
        self.hs.remove(5)
        self.assertEqual(len(self.hs), 9)
