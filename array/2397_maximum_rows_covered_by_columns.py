from typing import List
from itertools import combinations


class Solution:
    # bit manipulation & state compression
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        # 保存每行压缩的状态
        mask = [0] * m
        for r in range(m):
            for c in range(n):
                mask[r] |= (matrix[r][c] << c)
        res = 0
        # 遍历从0到2^n - 1,列举选择各列的情况
        for i in range(1 << n):
            # 选取的列数等于numSelect
            if sum(map(int, bin(i)[2:])) == numSelect:
                cur = 0
                for r in range(m):
                    # 与操作，如果选取的列i包含了该行mask[r]所有的1
                    if mask[r] & i == mask[r]:
                        cur += 1
                res = max(res, cur)
        return res


    # brute force
    def maximumRows1(self, matrix: List[List[int]], numSelect: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        if numSelect == n:
            return m

        res = 0
        for comb in combinations(range(n), numSelect):
            cur = 0
            for r in range(m):
                valid = True
                for c in range(n):
                    if c not in comb and matrix[r][c] == 1:
                        valid = False
                        break
                cur += valid
            res = max(res, cur)
        return res


def test_maximum_rows():
    solution = Solution()
    assert solution.maximumRows([[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 0, 1]], 2) == 3, 'wrong result'
    assert solution.maximumRows([[1], [0]], 1) == 2, 'wrong result'


if __name__ == '__main__':
    test_maximum_rows()
