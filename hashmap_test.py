import unittest

from hashmap import HashMap


class TestHashMap(unittest.TestCase):
    def setUp(self):
        self.map = HashMap()

    def test_put(self):
        self.map.put("key", "value")
        self.assertTrue("key" in self.map)

    def test_get(self):
        self.map.put("key", "value")
        result = self.map.get("key")
        self.assertEqual("value", result)

    def test_get_fail(self):
        with self.assertRaises(LookupError):
            self.map.get("key")

    def test_remove(self):
        self.map.put("key", "value")
        self.map.remove("key")
        self.assertFalse("key" in self.map)

    def test_keys(self):
        keys = [n for n in range(10)]
        for n in keys:
            k = str(n)
            self.map.put(k, n)
        self.assertEqual(set(list(self.map.keys())), set([str(k) for k in keys]))

    def test_len(self):
        self.assertEqual(len(self.map), 0)
        self.map.put("test", "cool")
        self.map.put("test", "what")
        self.assertEqual(len(self.map), 1)
        self.map.put("whoa", "what")
        self.assertEqual(len(self.map), 2)
