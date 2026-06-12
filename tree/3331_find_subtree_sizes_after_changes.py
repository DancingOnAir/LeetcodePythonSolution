from typing import List
from collections import defaultdict


class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        g = [[] for _ in range(n)]

        for i in range(1, n):
            g[parent[i]].append(i)

        ancestor = defaultdict(lambda: -1)

        def rebuild(x):
            old = ancestor[s[x]]
            ancestor[s[x]] = x
            for i in range(len(g[x])):
                y = g[x][i]
                cur = ancestor[s[y]]
                if cur != -1:
                    g[cur].append(y)
                    g[x][i] = -1
                rebuild(y)
            ancestor[s[x]] = old
        rebuild(0)

        res = [1] * n

        def dfs(x):
            for y in g[x]:
                if y != -1:
                    dfs(y)
                    res[x] += res[y]
        dfs(0)
        return res


def test_find_subtree_sizes():
    solution = Solution()
    assert solution.findSubtreeSizes([-1, 0, 0, 1, 1, 1], "abaabc") == [6, 3, 1, 1, 1, 1], 'wrong result'
    assert solution.findSubtreeSizes([-1, 0, 4, 0, 1], "abbba") == [5, 2, 1, 1, 1], 'wrong result'


if __name__ == '__main__':
    test_find_subtree_sizes()
