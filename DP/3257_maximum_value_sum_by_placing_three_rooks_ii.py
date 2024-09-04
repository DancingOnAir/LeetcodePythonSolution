from typing import List


class Solution:
    def maximumValueSum(self, board: List[List[int]]) -> int:
        def helper(row):
            for j, x in enumerate(row):
                for k in range(3):
                    if p[k][0] < x and all(j != j2 for _, j2 in p[:k]):
                        p[k], (x, j) = (x, j), p[k]

        p = [(float('-inf'), -1)] * 3
        m = len(board)
        suf = [None] * m
        # 给后缀数组赋值
        for i in range(m - 1, -1, -1):
            helper(board[i])
            suf[i] = p[:]

        res = float('-inf')
        p = [(float('-inf'), -1)] * 3
        for i, row in enumerate(board[:-2]):
            helper(row)
            for j2, y in enumerate(board[i + 1]):
                for x, j1 in p:
                    for z, j3 in suf[i + 2]:
                        if j1 != j2 and j2 != j3 and j1 != j3:
                            res = max(res, x + y + z)
        return res


def test_maximum_value_sum():
    solution = Solution()
    assert solution.maximumValueSum([[-3, 1, 1, 1], [-3, 1, -3, 1], [-3, 2, 1, 1]]) == 4, 'wrong result'
    assert solution.maximumValueSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 15, 'wrong result'
    assert solution.maximumValueSum([[1, 1, 1], [1, 1, 1], [1, 1, 1]]) == 3, 'wrong result'


if __name__ == '__main__':
    test_maximum_value_sum()