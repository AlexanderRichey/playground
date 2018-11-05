class HashMap:
    def __init__(self, len=32):
        self.store = [[None, None] for _ in range(len)]

    def get(self, k):
        idx = self._to_idx(k)
        if self.store[idx][0] != k:
            raise LookupError(f"'{k}' is not present")
        return self.store[idx][1]

    def put(self, k, v):
        idx = self._to_idx(k)
        if self.store[idx][0] and self.store[idx][0] != k:
            raise LookupError(f"'{k}' creates hashing collision")
        else:
            self.store[idx][0] = k
            self.store[idx][1] = v
        return True

    def remove(self, k):
        try:
            idx = self._to_idx(k)
            self.store[idx][0] = None
            self.store[idx][1] = None
        except IndexError:
            raise LookupError(f"'{k}' is not present")
        return True

    def keys(self):
        for pair in self.store:
            if pair[0]:
                yield pair[0]
            else:
                continue

    def _to_idx(self, k):
        return self._hash(k) % len(self.store)

    def _hash(self, k):
        hash = 0
        for char in k:
            hash = hash ^ ord(char)
        return hash
