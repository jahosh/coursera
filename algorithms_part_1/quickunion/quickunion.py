from typing import Tuple


class QuickUnion:
    def __init__(self, size: int) -> None:
        self.size = size
        self.storage = [i for i in range(size)]

    def _check_indicies(self, a: int, b: int) -> None:
        if a > self.size or b > self.size:
            raise Exception("""
                Index ouit of range error. Please check index of
                a or b and try again.
            """)

    def _get_roots(self, a: int, b: int) -> Tuple[int, int]:
        a_root = a
        b_root = b
        while (
            self.storage[a_root] != a_root
            or self.storage[b_root] != b_root
        ):
            a_root = self.storage[a_root]
            b_root = self.storage[b_root]
        return (a_root, b_root)

    def is_connected(self, a: int, b: int) -> bool:
        self._check_indicies(a, b)
        a_root, b_root = self._get_roots(a, b)
        return a_root == b_root

    def union(self, a: int, b: int) -> None:
        self._check_indicies(a, b)
        a_root, b_root = self._get_roots(a, b)
        self.storage[b_root] = a_root

