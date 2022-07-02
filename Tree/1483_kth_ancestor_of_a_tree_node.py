from typing import List


class TreeAncestor:
    def __init__(self, n: int, parent: List[int]):
        # parent = [(p, i) for i, p in enumerate(parent)]
        # parent.sort()
        self.parent = parent
        pass

    # def build(self, parent):
    #     for p, _ in parent:

    def getKthAncestor(self, node: int, k: int) -> int:
        res = node
        while k:
            if not res:
                return -1
            res = self.parent[res]
            k -= 1
        return res


# Your TreeAncestor object will be instantiated and called as such:
def test_tree_ancestor():
    obj = TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2])
    assert obj.getKthAncestor(3, 1) == 1, 'wrong result'
    assert obj.getKthAncestor(5, 2) == 0, 'wrong result'
    assert obj.getKthAncestor(6, 3) == -1, 'wrong result'