from typing import List
from functools import reduce
from itertools import accumulate, product


class Solution:
    # 模运算在四则运算里不支持除法分配律，需要转换为乘法
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        prefix = list(accumulate([c for r in grid for c in r], lambda x, y: (x * y) % 12345, initial=1))
        suffix = list(accumulate([c for r in reversed(grid) for c in reversed(r)], lambda x, y: (x * y) % 12345, initial=1))
        m, n = len(grid), len(grid[0])
        for i, j in product(range(m), range(n)):
            k = i * n + j
            grid[i][j] = (prefix[k] * suffix[-k - 2]) % 12345
        return grid

    # TLE
    def constructProductMatrix1(self, grid: List[List[int]]) -> List[List[int]]:
        total = reduce(lambda x, y: x * y, [c for r in grid for c in r])
        res = []
        for r in grid:
            row = []
            for c in r:
                row.append((total // c) % 12345)
            res.append(row)
        return res


def test_construct_product_matrix():
    solution = Solution()
    assert solution.constructProductMatrix([[1, 2], [3, 4]]) == [[24, 12], [8, 6]], 'wrong result'
    assert solution.constructProductMatrix([[12345], [2], [1]]) == [[2], [0], [0]], 'wrong result'


if __name__ == '__main__':
    test_construct_product_matrix()
