from typing import List


class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        A, B, C, D = [], [], [], []
        for i in range(len(arr1)):
            x, y = arr1[i], arr2[i]
            A.append(x + y + i)
            B.append(x + y - i)
            C.append(x - y + i)
            D.append(x - y - i)

        a = max(A) - min(A)
        b = max(B) - min(B)
        c = max(C) - min(C)
        d = max(D) - min(D)
        return max(a, b, c, d)


def test_max_abs_val_expr():
    solution = Solution()
    assert solution.maxAbsValExpr([1, 2, 3, 4], arr2=[-1, 4, 5, 6]) == 13, 'wrong result'
    assert solution.maxAbsValExpr([1, -2, -5, 0, 10], arr2=[0, -2, -1, -7, -4]) == 20, 'wrong result'


if __name__ == '__main__':
    test_max_abs_val_expr()
