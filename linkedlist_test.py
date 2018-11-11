import unittest

from linkedlist import LinkedList


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.ll = LinkedList()
        for i in range(10):
            self.ll.add(i)

    def test_peek(self):
        self.assertEqual(self.ll.peek().data, 9)

    def test_add(self):
        self.ll.add(11)
        self.assertEqual(self.ll.find(11).data, 11)

    def test_remove(self):
        self.ll.remove(0)
        self.assertEqual(self.ll.head.data, 1)
        self.ll.remove(5)
        self.assertFalse(self.ll.find(5))

    def test_remove_with_cb(self):
        self.ll.add(["hello"])
        self.ll.add({})

        def finder(data, _):
            try:
                data[0] == "hello"
            except Exception:
                pass
            return False

        self.ll.remove(cb=finder)
        self.assertFalse(self.ll.find(cb=finder))

    def test_find(self):
        self.assertEqual(self.ll.find(0).data, 0)
        self.assertEqual(self.ll.find(1).data, 1)
        self.assertEqual(self.ll.find(9).data, 9)

    def test_poll(self):
        old_head = self.ll.poll()
        self.assertEqual(old_head.data, 0)
        self.assertEqual(self.ll.head.data, 1)

    def test_pop(self):
        last = self.ll.pop()
        self.assertEqual(last.data, 9)
        self.assertEqual(self.ll.size, 9)

    def test_size(self):
        self.assertEqual(self.ll.size, 10)
        self.ll.pop()
        self.assertEqual(self.ll.size, 9)

    def test_iter(self):
        out = []
        for val in self.ll:
            out.append(val)
        self.assertListEqual(out, list(range(10)))
