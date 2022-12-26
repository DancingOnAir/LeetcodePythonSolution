from typing import List
from collections import defaultdict


class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        g = defaultdict(list)
        # net out degree
        degree = defaultdict(int)
        for u, v in pairs:
            g[u].append(v)
            degree[u] += 1
            degree[v] -= 1

        for k, v in degree.items():
            # check whether Eulerian Circuit
            if v == 1:
                u = k
                break

        res = list()

        # post dfs
        def dfs(u):
            while g[u]:
                v = g[u].pop()
                dfs(v)
                res.append([u, v])

        dfs(u)
        return res[::-1]


def test_valid_arrangement():
    solution = Solution()
    # assert solution.validArrangement([[17, 18], [18, 10], [10, 18]]) == [[17, 18], [18, 10], [10, 18]], 'wrong result'
    # assert solution.validArrangement([[5, 1], [4, 5], [11, 9], [9, 4]]) == [[11, 9], [9, 4], [4, 5], [5, 1]], 'wrong result'
    assert solution.validArrangement([[1, 3], [3, 2], [2, 1]]) == [[1, 3], [3, 2], [2, 1]], 'wrong result'
    assert solution.validArrangement([[1, 2], [1, 3], [2, 1]]) == [[1, 2], [2, 1], [1, 3]], 'wrong result'


if __name__ == '__main__':
    test_valid_arrangement()
