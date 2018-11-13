class BinaryTreeNode:
    def __init__(self, data, parent=None, left=None, right=None):
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right


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
        pass

    def dfs(self, target, node=None):
        if not node:
            node = self.root
        if node.data == target:
            return node
        elif node.data > target:
            if node.right:
                return dfs(target, node.right)
        elif node.data < target:
            if node.left:
                return dfs(target, node.left)
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
