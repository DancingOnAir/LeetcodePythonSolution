from typing import List


class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        for i in range(m - 1):
            for j in range(n - 1):
                cur = grid[i][j] + grid[i][j + 1] + grid[i + 1][j] + grid[i + 1][j + 1]
                if cur.count('B') != 2:
                    return True
        return False


def test_can_make_square():
    solution = Solution()
    assert solution.canMakeSquare([["B", "W", "B"], ["B", "W", "W"], ["B", "W", "B"]]), 'wrong result'
    assert not solution.canMakeSquare([["B", "W", "B"], ["W", "B", "W"], ["B", "W", "B"]]), 'wrong result'
    assert solution.canMakeSquare([["B", "W", "B"], ["B", "W", "W"], ["B", "W", "W"]]), 'wrong result'


if __name__ == '__main__':
    test_can_make_square()
