import unittest

from binarytree import BinaryTree


class BinaryTreeTest(unittest.TestCase):
    def setUp(self):
        self.tree = BinaryTree()

    def test_add(self):
        for i in range(5, 10):
            self.tree.add(i)
        for i in range(0, 4):
            self.tree.add(i)
        for i in range(10):
            node = self.tree.dfs(i)
            if node:
                self.assertEqual(node.data, i)

    def test_remove(self):
        for i in range(10):
            self.tree.add(i)
        for i in range(0, 10, 2):
            self.tree.remove(i)
        for i in range(10):
            if i % 2 == 0:
                self.assertIsNone(self.tree.dfs(i))
            else:
                self.assertIsNotNone(self.tree.dfs(i))
