from typing import List


class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        res = list()
        m, n = len(land), len(land[0])

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or land[r][c] == 0:
                return 0, 0

            land[r][c] = 0
            r1, c1 = dfs(r + 1, c)
            r2, c2 = dfs(r, c + 1)

            return max(r1, r2, r), max(c1, c2, c)

        for i in range(m):
            for j in range(n):
                if land[i][j] == 1:
                    x, y = dfs(i, j)
                    res.append([i, j, x, y])
        return res


def test_find_farmland():
    solution = Solution()
    assert solution.findFarmland([[1, 0, 0], [0, 1, 1], [0, 1, 1]]) == [[0, 0, 0, 0], [1, 1, 2, 2]], 'wrong result'
    assert solution.findFarmland([[1, 1], [1, 1]]) == [[0, 0, 1, 1]], 'wrong result'
    assert solution.findFarmland([[0]]) == [], 'wrong result'


if __name__ == '__main__':
    test_find_farmland()

