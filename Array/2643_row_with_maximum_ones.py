from typing import List


class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        return sorted([[i, sum(r)] for i, r in enumerate(mat)], key=lambda x: (-x[1], x[0]))[0]

    def rowAndMaximumOnes1(self, mat: List[List[int]]) -> List[int]:
        res = [-1, -1]
        for i, r in enumerate(mat):
            total = sum(r)
            if total > res[1]:
                res = [i, total]
        return res


def test_row_and_maximum_ones():
    solution = Solution()
    assert solution.rowAndMaximumOnes([[0, 1], [1, 0]]) == [0, 1], 'wrong result'
    assert solution.rowAndMaximumOnes([[0, 0, 0], [0, 1, 1]]) == [1, 2], 'wrong result'
    assert solution.rowAndMaximumOnes([[0, 0], [1, 1], [0, 0]]) == [1, 2], 'wrong result'


if __name__ == '__main__':
    test_row_and_maximum_ones()
