from typing import List
from itertools import accumulate
from bisect import bisect_left


class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        pre_sum = [0] + list(accumulate(nums))

        res = list()
        for q in queries:
            i = bisect_left(nums, q)
            res.append(i * q - pre_sum[i] + pre_sum[-1] - pre_sum[i] - (len(nums) - i) * q)
        return res

    # brute force but TLE
    def minOperations1(self, nums: List[int], queries: List[int]) -> List[int]:
        return list(sum(abs(x - q) for x in nums) for q in queries)


def test_min_operations():
    solution = Solution()
    assert solution.minOperations([3, 1, 6, 8], [1, 5]) == [14, 10], 'wrong result'
    assert solution.minOperations([2, 9, 6, 3], [10]) == [20], 'wrong result'


if __name__ == '__main__':
    test_min_operations()
