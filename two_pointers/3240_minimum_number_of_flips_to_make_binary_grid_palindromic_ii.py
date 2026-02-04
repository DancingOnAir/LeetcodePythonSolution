from typing import List


class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m // 2):
            row1, row2 = grid[i], grid[-i - 1]
            for j in range(n // 2):
                cnt1 = row1[j] + row2[-1 - j] + row2[j] + row1[-1 - j]
                res += min(cnt1, 4 - cnt1)
        # m，n为奇数的矩阵中心必须为0
        if m % 2 and n % 2:
            res += grid[m//2][n//2]

        diff = cnt2 = 0
        if m % 2:
            row = grid[m // 2]
            for j in range(n // 2):
                if row[j] != row[-1 - j]:
                    diff += 1
                else:
                    cnt2 += row[j] * 2
        if n % 2:
            for i in range(m // 2):
                if grid[i][n // 2] != grid[-1 - i][n // 2]:
                    diff += 1
                else:
                    cnt2 += grid[i][n // 2] * 2

        return res + (diff if diff else cnt2 % 4)


def test_min_flips():
    solution = Solution()
    assert solution.minFlips([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == 3, 'wrong result'
    assert solution.minFlips([[0, 1], [0, 1], [0, 0]]) == 2, 'wrong result'
    assert solution.minFlips([[1], [1]]) == 2, 'wrong result'


if __name__ == '__main__':
    test_min_flips()
