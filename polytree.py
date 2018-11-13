class PolyTreeNode:
    def __init__(self, data, parent=None, children=[]):
        self.data = data
        self.parent = parent
        self.children = children


class PolyTree:
    def __init__(self):
        self.root = None

    def add(self, data, parent):
        parent_node = self.bfs(parent)
        parent_node.children.append(PolyTreeNode(data))

    def remove(self, data):
        found = self.bfs(data)
        if len(found.children):
            found.parent.children.extend(found.children)
        del found.parent.children[found.parent.children.index(found)]

    def dfs(self, data, node=None):
        if not node:
            node = self.root
        if node.data == data:
            return node
        else:
            for child in node.children:
                value = dfs(data, child)
                if value:
                    return value
        return None

    def bfs(self, data):
        if self.root.data == data:
            return self.root
        queue = [self.root]
        while len(queue):
            node = queue.pop(0)
            if node.data == data:
                return node
            else:
                queue.extend(node.children)
        return None
