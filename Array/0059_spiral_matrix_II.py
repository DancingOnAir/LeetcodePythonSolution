from typing import List


class Solution:
    # walk the spiral
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        i, j, di, dj = 0, 0, 0, 1
        for k in range(n * n):
            res[i][j] = k + 1
            if res[(i + di) % n][(j + dj) % n]:
                di, dj = dj, -di
            i += di
            j += dj

        return res

    def generateMatrix1(self, n: int) -> List[List[int]]:
        res = [[0 for i in range(n)] for j in range(n)]
        top, bottom, left, right = 0, n - 1, 0, n - 1
        k = 1
        while k <= n * n:
            for i in range(left, right + 1):
                res[top][i] = k
                k += 1
            top += 1

            for i in range(top, bottom + 1):
                res[i][right] = k
                k += 1
            right -= 1

            for i in range(right, left - 1, -1):
                res[bottom][i] = k
                k += 1
            bottom -= 1

            for i in range(bottom, top - 1, -1):
                res[i][left] = k
                k += 1
            left += 1
        return res


def test_generate_matrix():
    solution = Solution()

    print(solution.generateMatrix(3))
    print(solution.generateMatrix(4))

if __name__ == '__main__':
    test_generate_matrix()
