from functools import reduce
from linkedlist import LinkedList


class HashMap:
    def __init__(self, len=32):
        self.store = [LinkedList() for _ in range(len)]

    def __len__(self):
        length = 0
        for i in self.keys():
            length += 1
        return length

    def __contains__(self, k):
        try:
            self.get(k)
        except LookupError:
            return False
        return True

    def get(self, k):
        idx = self._to_idx(k)
        ll = self.store[idx]
        found = ll.find(cb=lambda data, _: data[0] == k)
        if not found:
            raise LookupError(f"'{k}' is not present")
        return found.data[1]

    def put(self, k, v):
        idx = self._to_idx(k)
        ll = self.store[idx]
        found = ll.find(cb=lambda data, _: data[0] == k)
        if found:
            found.data[1] = v
        else:
            ll.add([k, v])
        return True

    def remove(self, k):
        idx = self._to_idx(k)
        ll = self.store[idx]
        ll.remove(cb=lambda data, _: data[0] == k)
        return True

    def keys(self):
        for node in self.store:
            for val in node:
                yield val[0]
            else:
                continue

    def _to_idx(self, k):
        return self._hash(k) % len(self.store)

    def _hash(self, k):
        return reduce(lambda acc, chr: acc ^ ord(chr), k, 0)
