from typing import List
from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        in_degrees = [0] * numCourses
        for u, v in prerequisites:
            graph[u].append(v)
            in_degrees[v] += 1

        dq = deque(i for i, val in enumerate(in_degrees) if val == 0)
        res = 0
        while dq:
            u = dq.popleft()
            res += 1
            for v in graph[u]:
                in_degrees[v] -= 1
                if in_degrees[v] == 0:
                    dq.append(v)
        return res == numCourses


def test_can_finish():
    solution = Solution()
    assert solution.canFinish(2, [[1, 0]]), 'wrong result'
    assert not solution.canFinish(2, [[1, 0], [0, 1]]), 'wrong result'


if __name__ == '__main__':
    test_can_finish()
