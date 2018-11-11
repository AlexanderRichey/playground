from functools import reduce
from linkedlist import LinkedList


class HashSet:
    def __init__(self):
        self.store = [LinkedList() for _ in range(32)]

    def add(self, v):
        idx = self._to_idx(v)
        ll = self.store[idx]
        if ll.find(v):
            return
        ll.add(v)

    def remove(self, v):
        idx = self._to_idx(v)
        ll = self.store[idx]
        ll.remove(v)

    def _hash(self, k):
        return hash(k)

    def _to_idx(self, k):
        return self._hash(k) % len(self.store)

    def __len__(self):
        length = 0
        for ll in self.store:
            for var in ll:
                length += 1
        return length

    def __contains__(self, v):
        idx = self._to_idx(v)
        ll = self.store[idx]
        if ll.find(v):
            return True
        return False

    def __iter__(self):
        for ll in self.store:
            for val in ll:
                yield val
