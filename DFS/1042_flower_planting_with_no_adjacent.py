from typing import List


class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        for u, v in paths:
            g[u - 1].append(v - 1)
            g[v - 1].append(u - 1)

        res = [-1] * n

        def dfs(u):
            res[u] = ({1, 2, 3, 4} - {res[v] for v in g[u]}).pop()
            for v in g[u]:
                if res[v] == -1:
                    dfs(v)

        for i in range(n):
            if res[i] == -1:
                dfs(i)
        return res


def test_garden_no_adj():
    solution = Solution()
    assert solution.gardenNoAdj(6, [[6, 4], [6, 1], [3, 1], [4, 5], [2, 1], [5, 6], [5, 2]]) == [1, 2, 3], 'wrong result'
    assert solution.gardenNoAdj(3, [[1, 2], [2, 3], [3, 1]]) == [1, 2, 3], 'wrong result'
    assert solution.gardenNoAdj(4, [[1, 2], [3, 4]]) == [1, 2, 1, 2], 'wrong result'
    assert solution.gardenNoAdj(4, [[1, 2], [2, 3], [3, 4], [4, 1], [1, 3], [2, 4]]) == [1, 2, 3, 4], 'wrong result'


if __name__ == '__main__':
    test_garden_no_adj()
