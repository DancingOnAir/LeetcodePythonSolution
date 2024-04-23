from typing import List


class Solution:
    # O(mn)
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        res = [[0] * n for _ in range(m)]
        cnt = [[0] * n for _ in range(m)]

        for i in range(2, m):
            for j in range(2, n):
                in_region = True
                # 检查左右相邻的格子
                for r in image[i - 2: i + 1]:
                    if abs(r[j - 1] - r[j - 2]) > threshold or abs(r[j] - r[j - 1]) > threshold:
                        in_region = False
                        break
                if not in_region:
                    continue

                # 检查上下相邻的格子
                for y in range(j - 2, j + 1):
                    if abs(image[i - 2][y] - image[i - 1][y]) > threshold or abs(image[i - 1][y] - image[i][y]) > threshold:
                        in_region = False
                        break
                if not in_region:
                    continue

                avg = sum(image[x][y] for x in range(i - 2, i + 1) for y in range(j - 2, j + 1)) // 9
                for x in range(i - 2, i + 1):
                    for y in range(j - 2, j + 1):
                        res[x][y] += avg
                        cnt[x][y] += 1

        for i, r in enumerate(cnt):
            for j, c in enumerate(r):
                if c == 0:
                    res[i][j] = image[i][j]
                else:
                    res[i][j] //= c
        return res


def test_result_grid():
    solution = Solution()
    assert solution.resultGrid([[5, 6, 7, 10], [8, 9, 10, 10], [11, 12, 13, 10]], 3) == [[9, 9, 9, 9], [9, 9, 9, 9],
                                                                                         [9, 9, 9, 9]], 'wrong result'
    assert solution.resultGrid([[10, 20, 30], [15, 25, 35], [20, 30, 40], [25, 35, 45]], 12) == [[25, 25, 25],
                                                                                                 [27, 27, 27],
                                                                                                 [27, 27, 27], [30, 30,
                                                                                                                30]], 'wrong result'
    assert solution.resultGrid([[5, 6, 7], [8, 9, 10], [11, 12, 13]], 1) == [[5, 6, 7], [8, 9, 10],
                                                                             [11, 12, 13]], 'wrong result'


if __name__ == '__main__':
    test_result_grid()
