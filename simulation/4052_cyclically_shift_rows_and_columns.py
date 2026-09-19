class Solution:
    def cyclicShift(self, n: int, grid: list[list[int]], rowShift: list[int], colShift: list[int]) -> list[list[int]]:
        for i, r in enumerate(grid):
            k = rowShift[i]
            grid[i] = r[k:] + r[:k]

        for j, c in enumerate(zip(*grid)):
            k = colShift[j]
            new_col = c[k:] + c[:k]
            for r, x in zip(grid, new_col):
                r[j] = x
        return grid


def test_cyclic_shift():
    solution = Solution()
    assert solution.cyclicShift(2, grid = [[1,2],[3,4]], rowShift = [1,0], colShift = [0,1]) == [[2,4],[3,1]], 'wrong result'
    assert solution.cyclicShift(3, grid = [[1,2,3],[4,5,6],[7,8,9]], rowShift = [1,2,0], colShift = [2,2,1]) == [[7,8,5],[2,3,9],[6,4,1]], 'wrong result'


if __name__ == '__main__':
    test_cyclic_shift()
