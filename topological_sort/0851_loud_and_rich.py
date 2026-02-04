from typing import List
from collections import deque


class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        in_degrees = [0] * n
        graph = [[] for _ in range(n)]
        for u, v in richer:
            graph[u].append(v)
            in_degrees[v] += 1

        res = list(range(n))
        dq = deque(i for i, val in enumerate(in_degrees) if val == 0)
        while dq:
            u = dq.popleft()
            for v in graph[u]:
                if quiet[res[v]] > quiet[res[u]]:
                    res[v] = res[u]
                in_degrees[v] -= 1
                if in_degrees[v] == 0:
                    dq.append(v)
        return res


def test_loud_and_rich():
    solution = Solution()
    assert solution.loudAndRich([[1, 0], [2, 1], [3, 1], [3, 7], [4, 3], [5, 3], [6, 3]], [3, 2, 5, 4, 6, 1, 7, 0]) == [5, 5, 2, 5, 4, 5, 6, 7], 'wrong result'
    assert solution.loudAndRich([], [0]) == [0], 'wrong result'


if __name__ == '__main__':
    test_loud_and_rich()
