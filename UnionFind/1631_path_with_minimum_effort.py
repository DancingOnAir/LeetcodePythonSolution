from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        pass


def test_minimum_effort_path():
    solution = Solution()

    assert solution.minimumEffortPath([[1, 2, 2], [3, 8, 2], [5, 3, 5]]) == 2, 'wrong result'
    assert solution.minimumEffortPath([[1, 2, 3], [3, 8, 4], [5, 3, 5]]) == 1, 'wrong result'
    assert solution.minimumEffortPath([[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]]) == 0, 'wrong result'


if __name__ == '__main__':
    test_minimum_effort_path()
