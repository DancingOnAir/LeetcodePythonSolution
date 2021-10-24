from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def find(idx):
            if idx != parents[idx]:
                idx = find(parents[idx])
            return idx

        def union(idx1, idx2):
            p1 = find(idx1)
            p2 = find(idx2)
            if p1 == p2:
                return
            parents[p1] = p2

            nonlocal res
            res -= 1

        row = len(grid)
        col = len(grid[0])
        res = sum(grid[i][j] == '1' for i in range(row) for j in range(col))
        parents = [i for i in range(row * col)]
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '0':
                    continue
                cur = i * col + j
                if j + 1 < col and grid[i][j + 1] == '1':
                    union(cur, cur + 1)
                if i + 1 < row and grid[i + 1][j] == '1':
                    union(cur, cur + col)

        return res


def test_num_is_lands():
    solution = Solution()

    assert solution.numIslands([
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]) == 1, 'wrong result'

    assert solution.numIslands([
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]) == 3, 'wrong result'


if __name__ == '__main__':
    test_num_is_lands()
