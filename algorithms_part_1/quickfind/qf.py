class QuickFind:
    def __init__(self, size):
        self.storage = [i for i in range(size)]
        self.size = size

    def connected(self, a, b):
        """ O(1) connection check """
        return self.storage[a] == self.storage[b]

    def union(self, a, b):
        """ O(N) union op """
        if a > self.size or b > self.size:
            raise Exception("Index out of range. Please check component indexes and try again.")

        if self.connected(a, b):
            return

        a_root = self.storage[a]
        b_root = self.storage[b]

        for i in range(len(self.storage)):
            if self.storage[i] == b_root:
                self.storage[i] = a_root
