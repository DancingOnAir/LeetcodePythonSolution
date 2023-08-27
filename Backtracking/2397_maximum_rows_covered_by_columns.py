from typing import List


class Solution:
    # bitmask: Gosper's Hack: https://www.bilibili.com/video/BV1na41137jv/?vd_source=e6f3bca3cb4f75b9e8b036e0e78f1541
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
        res = 0
        x = (1 << numSelect) - 1
        mask = [sum(c << j for j, c in enumerate(r)) for i, r in enumerate(matrix)]
        while x < (1 << len(matrix[0])):
            res = max(res, sum(x & r == r for r in mask))
            lowbit = x & -x
            left = x + lowbit
            right = (x ^ left) // lowbit >> 2
            x = left | right
        return res

    # bit mask
    def maximumRows2(self, matrix: List[List[int]], numSelect: int) -> int:
        res = 0
        mask = [sum(c << j for j, c in enumerate(r)) for i, r in enumerate(matrix)]
        for x in range(1 << len(matrix[0])):
            if bin(x)[2:].count('1') == numSelect:
                # x & r == r 表示r是x的子集，所有1都被覆盖
                res = max(res, sum(x & r == r for r in mask))
        return res

    # backtracking recursive
    def maximumRows1(self, matrix: List[List[int]], numSelect: int) -> int:
        def dfs(i):
            nonlocal cnt
            if cnt == numSelect:
                cur = 0
                for r in matrix:
                    if all(select[j] == 1 for j, c in enumerate(r) if c == 1):
                        cur += 1

                nonlocal res
                res = max(res, cur)

            if i >= n:
                return

            dfs(i + 1)

            select[i] += 1
            cnt += 1
            dfs(i + 1)

            select[i] -= 1
            cnt -= 1

        m, n = len(matrix), len(matrix[0])
        res = cnt = 0
        select = [0] * n
        dfs(0)
        return res


def test_maximum_rows():
    solution = Solution()
    assert solution.maximumRows([[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 0, 1]], 2) == 3, 'wrong result'
    assert solution.maximumRows([[1], [0]], 1) == 2, 'wrong result'


if __name__ == '__main__':
    test_maximum_rows()
