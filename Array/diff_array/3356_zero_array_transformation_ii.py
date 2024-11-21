from typing import List


class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        diff = [0] * (len(nums) + 1)
        sum_d = k = 0
        for i, (x, d) in enumerate(zip(nums, diff)):
            sum_d += d
            while k < len(queries) and sum_d < x:
                l, r, v = queries[k]
                diff[l] += v
                diff[r + 1] -= v
                if l <= i <= r:
                    sum_d += v
                k += 1

            if sum_d < x:
                return -1
        return k


def test_is_zero_array():
    solution = Solution()
    assert solution.minZeroArray([2, 0, 2], [[0, 2, 1], [0, 2, 1], [1, 1, 3]]) == 2, 'wrong result'
    assert solution.minZeroArray([4, 3, 2, 1], [[1, 3, 2], [0, 2, 1]]) == -1, 'wrong result'


if __name__ == '__main__':
    test_is_zero_array()
