from typing import List


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        pass


def test_shortest_path_length():
    solution = Solution()

    assert solution.shortestPathLength([[1, 2, 3], [0], [0], [0]]) == 4, 'wrong result'
    assert solution.shortestPathLength([[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]]) == 4, 'wrong result'


if __name__ == '__main__':
    test_shortest_path_length()
