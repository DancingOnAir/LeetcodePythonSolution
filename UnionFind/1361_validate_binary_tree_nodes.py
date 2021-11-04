from typing import List


class Solution:
    class UF(object):
        def __init__(self, n):
            self.parent = list(range(n))
            self.sz = [1] * n
            self.cnt = n

        def find(self, p):
            while p != self.parent[p]:
                self.parent[p] = self.parent[self.parent[p]]
                p = self.parent[p]

            return p

        def unite(self, p, q):
            rp = self.find(p)
            rq = self.find(q)

            # exist cycle
            if rp == rq:
                return False

            if self.sz[rp] < self.sz[rq]:
                self.parent[rp] = rq
                self.sz[rq] += self.sz[rp]
            else:
                self.parent[rq] = rp
                self.sz[rp] += self.sz[rq]

            self.cnt -= 1
            return True

    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        uf = Solution.UF(n)
        in_degree = [0] * n
        for parent, (lc, rc) in enumerate(zip(leftChild, rightChild)):
            if lc != -1:
                if not uf.unite(parent, lc):
                    return False
                in_degree[lc] += 1
                if in_degree[lc] > 1:
                    return False

            if rc != -1:
                if not uf.unite(parent, rc):
                    return False
                in_degree[rc] += 1
                if in_degree[rc] > 1:
                    return False

        return uf.cnt == 1

        # m = set()
        # for i in range(n):
        #     # m.add(i)
        #     if leftChild[i] != -1:
        #         if leftChild[i] in m or uf.find(leftChild[i]) == uf.find(i):
        #             return False
        #         m.add(leftChild[i])
        #         uf.unite(i, leftChild[i])
        #
        #     if rightChild[i] != -1:
        #         if rightChild[i] in m or uf.find(rightChild[i]) == uf.find(i):
        #             return False
        #         m.add(rightChild[i])
        #         uf.unite(i, rightChild[i])
        #
        # if uf.cnt != 1:
        #     return False
        #
        # return True


def test_validate_binary_tree_nodes():
    solution = Solution()

    assert solution.validateBinaryTreeNodes(4, [3, -1, 1, -1], [-1, -1, 0, -1]), 'wrong result'
    assert solution.validateBinaryTreeNodes(4, [1, -1, 3, -1], [2, -1, -1, -1]), 'wrong result'
    assert not solution.validateBinaryTreeNodes(4, [1, -1, 3, -1], [2, 3, -1, -1]), 'wrong result'
    assert not solution.validateBinaryTreeNodes(2, [1, 0], [-1, -1]), 'wrong result'
    assert not solution.validateBinaryTreeNodes(6, [1, -1, -1, 4, -1, -1], [2, -1, -1, 5, -1, -1]), 'wrong result'


if __name__ == '__main__':
    test_validate_binary_tree_nodes()

