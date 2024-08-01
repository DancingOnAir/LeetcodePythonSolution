from typing import List


class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        for i, r in enumerate(grid):
            if sum(r) == len(grid) - 1:
                return i
        return -1


def test_find_champion():
    solution = Solution()
    assert solution.findChampion([[0, 1], [0, 0]]) == 0, 'wrong result'
    assert solution.findChampion([[0, 0, 1], [1, 0, 1], [0, 0, 0]]) == 1, 'wrong result'


if __name__ == '__main__':
    test_find_champion()
