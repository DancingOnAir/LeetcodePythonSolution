from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return list()

        res = list()
        for i in range(0, len(original), n):
            res.append(original[i: i + n])
        return res




def test_construct_2d_array():
    solution = Solution()

    assert solution.construct2DArray([1, 2, 3, 4], 2, 2) == [[1, 2], [3, 4]], 'wrong result'
    assert solution.construct2DArray([1, 2, 3], 1, 3) == [[1, 2, 3]], 'wrong result'
    assert solution.construct2DArray([1, 2], 1, 1) == [], 'wrong result'


if __name__ == '__main__':
    test_construct_2d_array()
