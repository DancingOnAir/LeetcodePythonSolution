from typing import List
from collections import defaultdict


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        for i, p in enumerate(manager):
            graph[p].append(i)

        def dfs(u):
            res = 0
            for v in graph[u]:
                res = max(res, dfs(v) + informTime[u])
            return res
        return dfs(headID)


def test_num_of_minutes():
    solution = Solution()
    assert solution.numOfMinutes(1, 0, [-1], [0]) == 0, 'wrong result'
    assert solution.numOfMinutes(6, 2, [2, 2, -1, 2, 2, 2], [0, 0, 1, 0, 0, 0]) == 1, 'wrong result'


if __name__ == '__main__':
    test_num_of_minutes()
