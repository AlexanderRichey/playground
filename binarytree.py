class BinaryTreeNode:
    def __init__(self, data, parent=None, left=None, right=None):
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

    @property
    def successor(self):
        parent = self
        successor = self.right
        while successor.left:
            parent = successor
            successor = successor.left
        return successor

    @property
    def is_leaf(self):
        return not (self.left or self.right)


class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, data):
        if not self.root:
            self.root = BinaryTreeNode(data)
        else:
            queue = [self.root]
            while len(queue):
                node = queue.pop(0)
                if node.data > data:
                    if node.right:
                        queue.append(node.right)
                    else:
                        node.right = BinaryTreeNode(data, node)
                else:
                    if node.left:
                        queue.append(node.left)
                    else:
                        node.left = BinaryTreeNode(data, node)

    def remove(self, data):
        target = self.bfs(data)
        if not target:
            return
        if target.is_leaf:
            target.parent = None
        elif target.left or target.right and not (target.left and target.right):
            if target.left:
                child = target.left
            else:
                child = target.right
            if target.parent:
                if target.parent.left is target:
                    target.parent.left = child
                else:
                    target.parent.right = child
            else:
                self.root = child
        else:
            if target.parent.left is target.successor:
                target.parent.left = target.successor.right
            else:
                target.parent.right = target.successor.right
        return target

    def dfs(self, target, node=None):
        if not node:
            node = self.root
        if node.data == target:
            return node
        elif node.data > target:
            if node.right:
                return self.dfs(target, node.right)
        elif node.data < target:
            if node.left:
                return self.dfs(target, node.left)
        return None

    def bfs(self, target):
        queue = [self.root]
        while len(queue):
            node = queue.pop(0)
            if node.data == target:
                return node
            elif node.data > target:
                if node.right:
                    queue.append(node.right)
            else:
                if node.left:
                    queue.append(node.left)
        return None

    def pinorder(self, node=None):
        if not node:
            node = self.root
        if node.left:
            self.pinorder(node.left)
        print(node)
        if node.right:
            self.pinorder(node.right)

    def ppreorder(self, node=None):
        if not node:
            node = self.root
        print(node)
        if node.left:
            self.ppreorder(node.left)
        if node.right:
            self.ppreorder(node.right)

    def ppostorder(self, node=None):
        if not node:
            node = self.root
        if node.left:
            self.ppostorder(node.left)
        if node.right:
            self.ppostorder(node.right)
        print(node)
