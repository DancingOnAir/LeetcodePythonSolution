from typing import List


class Solution:
    class UnionFind(object):
        def __init__(self):
            self.parent = list(range(26))

        def find(self, index):
            if index == self.parent[index]:
                return index

            self.parent[index] = self.find(self.parent[index])
            return self.parent[index]

        def union(self, index1, index2):
            self.parent[self.find(index1)] = self.find(index2)

    def equationsPossible(self, equations: List[str]) -> bool:
        uf = Solution.UnionFind()
        for e in equations:
            if e[1] == "=":
                index1 = ord(e[0]) - ord('a')
                index2 = ord(e[3]) - ord('a')
                uf.union(index1, index2)

        for e in equations:
            if e[1] == "!":
                index1 = ord(e[0]) - ord('a')
                index2 = ord(e[3]) - ord('a')
                if uf.find(index1) == uf.find(index2):
                    return False

        return True


def test_equations_possible():
    solution = Solution()
    assert not solution.equationsPossible(["a==b", "b!=a"]), 'wrong result'
    assert solution.equationsPossible(["b==a", "a==b"]), 'wrong result'
    assert solution.equationsPossible(["a==b", "b==c", "a==c"]), 'wrong result'
    assert not solution.equationsPossible(["a==b", "b!=c", "c==a"]), 'wrong result'
    assert solution.equationsPossible(["c==c", "b==d", "x!=z"]), 'wrong result'


if __name__ == '__main__':
    test_equations_possible()
