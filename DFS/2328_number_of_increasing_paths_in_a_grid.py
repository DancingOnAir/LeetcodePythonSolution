from typing import List


class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        pass


def test_count_paths():
    solution = Solution()
    assert solution.countPaths([[1, 1], [3, 4]]) == 8, 'wrong result'
    assert solution.countPaths([[1], [2]]) == 3, 'wrong result'


if __name__ == '__main__':
    test_count_paths()
