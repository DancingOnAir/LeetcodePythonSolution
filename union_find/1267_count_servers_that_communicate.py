class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        row_cnt = [0] * len(grid)
        col_cnt = [0] * len(grid[0])
        for i, r in enumerate(grid):
            for j, c in enumerate(r):
                if c > 0:
                    row_cnt[i] += 1
                    col_cnt[j] += 1
        res = 0
        for i, r in enumerate(grid):
            for j, c in enumerate(r):
                if c > 0 and (row_cnt[i] > 1 or col_cnt[j] > 1):
                    res += 1
        return res


def test_count_servers():
    solution = Solution()
    assert solution.countServers([[1, 0], [0, 1]]) == 0, 'wrong result'
    assert solution.countServers([[1, 0], [1, 1]]) == 3, 'wrong result'
    assert solution.countServers([[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]) == 4, 'wrong result'


if __name__ == '__main__':
    test_count_servers()
