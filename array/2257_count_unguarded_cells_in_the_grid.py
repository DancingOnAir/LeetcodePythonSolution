from typing import List


class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]
        for x, y in walls + guards:
            grid[x][y] = 1

        for r, c in guards:
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                x, y = r, c
                while 0 <= x + dx < m and 0 <= y + dy < n and grid[x + dx][y + dy] != 1:
                    x += dx
                    y += dy
                    grid[x][y] = 2

        return sum(x == 0 for r in grid for x in r)


def test_count_unguarded():
    solution = Solution()
    assert solution.countUnguarded(4, 6, [[0,0],[1,1],[2,3]], [[0,1],[2,2],[1,4]]) == 7, 'wrong result'
    assert solution.countUnguarded(3, 3, [[1,1]], [[0,1],[1,0],[2,1],[1,2]]) == 4, 'wrong result'


if __name__ == '__main__':
    test_count_unguarded()
