class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        seen = set()
        res = float('inf')

        def dfs(i: int, j: int, xor: int) -> None:
            nonlocal res
            if res == 0 or i < 0 or j < 0 or (i, j, xor) in seen:
                return

            seen.add((i, j, xor))
            xor ^= grid[i][j]
            if i == 0 and j == 0:
                res = min(res, xor)
                return

            dfs(i - 1, j, xor)
            dfs(i, j - 1, xor)

        dfs(len(grid) - 1, len(grid[0]) - 1, 0)
        return res


def test_min_cost():
    solution = Solution()
    assert solution.minCost([[1, 2], [3, 4]]) == 6, 'wrong result'
    assert solution.minCost([[6, 7], [5, 8]]) == 9, 'wrong result'
    assert solution.minCost([[2, 7, 5]]) == 0, 'wrong result'


if __name__ == '__main__':
    test_min_cost()
