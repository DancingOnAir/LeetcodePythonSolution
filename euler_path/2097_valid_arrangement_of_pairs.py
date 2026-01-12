from typing import List
from collections import defaultdict


class Solution:
    # iterative
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        g = defaultdict(list)
        degree = defaultdict(int)
        for u, v in pairs:
            g[u].append(v)
            degree[u] += 1
            degree[v] -= 1

        start = pairs[0][0]
        for k, v in degree.items():
            if v == 1:
                start = k
                break

        res = list()
        stk = [start]
        while stk:
            while g[stk[-1]]:
                stk.append(g[stk[-1]].pop())
            res.append(stk.pop())
        res.reverse()
        return [[res[i], res[i + 1]] for i in range(len(res) - 1)]

    # recursive
    def validArrangement1(self, pairs: List[List[int]]) -> List[List[int]]:
        g = defaultdict(list)
        # net out degree
        degree = defaultdict(int)
        for u, v in pairs:
            g[u].append(v)
            degree[u] += 1
            degree[v] -= 1

        res = list()

        # post dfs
        def dfs(u):
            while g[u]:
                v = g[u].pop()
                dfs(v)
                res.append([u, v])

        for k, v in degree.items():
            # check whether Eulerian Circuit
            if v == 1:
                dfs(k)
                break
        if not res:
            dfs(pairs[0][0])
        return res[::-1]


def test_valid_arrangement():
    solution = Solution()
    assert solution.validArrangement([[17, 18], [18, 10], [10, 18]]) == [[17, 18], [18, 10], [10, 18]], 'wrong result'
    assert solution.validArrangement([[5, 1], [4, 5], [11, 9], [9, 4]]) == [[11, 9], [9, 4], [4, 5], [5, 1]], 'wrong result'
    assert solution.validArrangement([[1, 3], [3, 2], [2, 1]]) == [[1, 3], [3, 2], [2, 1]], 'wrong result'
    assert solution.validArrangement([[1, 2], [1, 3], [2, 1]]) == [[1, 2], [2, 1], [1, 3]], 'wrong result'


if __name__ == '__main__':
    test_valid_arrangement()
