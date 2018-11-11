class LinkNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def peek(self):
        if not self.head or not self.head.next:
            return self.head
        else:
            node = self.head
            while node.next:
                node = node.next
        return node

    def add(self, data, idx=None):
        if idx:
            node = self.head
            cur_idx = 0
            while node:
                if cur_idx == idx:
                    new_next = node.next
                    node.next = LinkNode(data)
                    node.next.next = new_next
                    return True
                node = node.next
                cur_idx += 1
            return False
        else:
            node = self.peek()
            if not node:
                self.head = LinkNode(data)
            else:
                node.next = LinkNode(data)

    def remove(self, data):
        node = self.head
        if not node:
            return False
        if node.data == data:
            if not node.next:
                raise ValueError("No other node can be head")
            self.head = node.next
            return True
        while node.next:
            if node.next.data == data:
                removed = node.next
                node.next = node.next.next
                return removed
            node = node.next
        return False

    def find(self, data):
        node = self.head
        while node:
            if node.data == data:
                return node
            node = node.next
        return False

    def poll(self):
        if not self.head.next:
            raise ValueError("No other node can be head")
        removed = self.head
        self.head = self.head.next
        return removed

    def pop(self):
        node = self.head
        if not node:
            raise ValueError("Empty list")
        next_node = node.next
        if not next_node.next:
            removed = self.head
            self.head = next_node
            return removed
        while node.next and next_node.next:
            node = node.next
            next_node = next_node.next
        node.next = None
        return next_node

    @property
    def size(self):
        length = 0
        node = self.head
        while node:
            length += 1
            node = node.next
        return length

    @property
    def is_empty(self):
        return self.size > 0
