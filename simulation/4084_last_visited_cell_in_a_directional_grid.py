class Solution:
    def lastVisitedCell(self, grid: list[list[str]]) -> list[int]:
        m, n = len(grid), len(grid[0])
        r, c = 0, 0
        while True:
            nr, nc = r, c
            match grid[r][c]:
                case 'R':
                    nc += 1
                case 'L':
                    nc -= 1
                case 'U':
                    nr -= 1
                case _:
                    nr += 1
            if nc < 0 or nc == n or nr < 0 or nr == m or grid[nr][nc] is None:
                return [r, c]
            grid[r][c] = None
            r, c = nr, nc

def test_last_visited_cell():
    solution = Solution()
    assert solution.lastVisitedCell([["D","L"],["D","R"]]) == [1, 0], 'wrong result'
    assert solution.lastVisitedCell([["R", "D"], ["U", "L"]]) == [1, 0], 'wrong result'
    assert solution.lastVisitedCell([["R", "R", "R"]]) == [0, 2], 'wrong result'


if __name__ == '__main__':
    test_last_visited_cell()
