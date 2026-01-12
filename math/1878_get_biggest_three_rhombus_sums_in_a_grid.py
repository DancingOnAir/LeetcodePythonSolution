from typing import List


class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        ps1, ps2 = [[0] * (n + 2) for _ in range(m + 1)], [[0] * (n + 2) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                ps1[i][j] = ps1[i - 1][j - 1] + grid[i - 1][j - 1]
                ps2[i][j] = ps2[i - 1][j + 1] + grid[i - 1][j - 1]

        res = []
        for i in range(m):
            for j in range(n):
                res.append(grid[i][j])
                for k in range(i + 2, m, 2):
                    ux, uy = i, j
                    dx, dy = k, j
                    lx, ly = (i + k) // 2, j - (k - i) // 2
                    rx, ry = (i + k) // 2, j + (k - i) // 2
                    if ly < 0 or ry >= n:
                        break

                    res.append((ps2[lx + 1][ly + 1] - ps2[ux][uy + 2]) +
                               (ps1[rx + 1][ry + 1] - ps1[ux][uy]) +
                               (ps1[dx + 1][dy + 1] - ps1[lx][ly]) +
                               (ps2[dx + 1][dy + 1] - ps2[rx][ry + 2]) -
                               (grid[ux][uy] + grid[dx][dy] + grid[lx][ly] + grid[rx][ry]))
        return sorted(set(res), reverse=True)[:3]


def test_get_biggest_three():
    solution = Solution()
    assert solution.getBiggestThree(
        [[3, 4, 5, 1, 3], [3, 3, 4, 2, 3], [20, 30, 200, 40, 10], [1, 5, 5, 4, 1], [4, 3, 2, 2, 5]]) == [228, 216,
                                                                                                         211], 'wrong result'
    assert solution.getBiggestThree([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [20, 9, 8], 'wrong result'
    assert solution.getBiggestThree([[7, 7, 7]]) == [7], 'wrong result'


if __name__ == '__main__':
    test_get_biggest_three()
