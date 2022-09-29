from typing import List


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        in_degree = [0] * n
        for u, v, t in roads:
            graph[u].append(v)
            graph[v].append(u)
        pass


def test_count_paths():
    solution = Solution()
    assert solution.countPaths(7, [[0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3], [3, 5, 1], [6, 5, 1], [2, 5, 1], [0, 4, 5], [4, 6, 2]]) == 4, 'wrong result'
    assert solution.countPaths(2, [[1, 0, 10]]) == 1, 'wrong result'


if __name__ == '__main__':
    test_count_paths()

