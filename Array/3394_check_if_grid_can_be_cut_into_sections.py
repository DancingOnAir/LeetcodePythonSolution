from typing import List


class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        def check(A):
            res = 0
            A.sort()
            pre = A[0][1]
            for a, b in A:
                res += pre <= a
                pre = max(pre, b)
            return res > 1

        x_axis = []
        y_axis = []
        for x1, y1, x2, y2 in rectangles:
            x_axis.append((x1, x2))
            y_axis.append((y1, y2))

        return check(x_axis) or check(y_axis)


def test_check_valid_cuts():
    solution = Solution()
    assert solution.checkValidCuts(5, [[1, 0, 5, 2], [0, 2, 2, 4], [3, 2, 5, 3], [0, 4, 4, 5]]), 'wrong result'
    assert solution.checkValidCuts(4, [[0, 0, 1, 1], [2, 0, 3, 4], [0, 2, 2, 3], [3, 0, 4, 3]]), 'wrong result'
    assert not solution.checkValidCuts(4, [[0, 2, 2, 4], [1, 0, 3, 2], [2, 2, 3, 4], [3, 0, 4, 2],
                                           [3, 2, 4, 4]]), 'wrong result'


if __name__ == '__main__':
    test_check_valid_cuts()
