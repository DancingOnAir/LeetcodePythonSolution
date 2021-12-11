from typing import List
from collections import defaultdict


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        res = cur = i = 0
        s = set()
        for j, val in enumerate(nums):
            while val in s:
                s.remove(nums[i])
                cur -= nums[i]
                i += 1
            s.add(val)
            cur += val
            res = max(res, cur)
        return res


def test_maximum_unique_subarray():
    solution = Solution()
    assert solution.maximumUniqueSubarray([4, 2, 4, 5, 6]) == 17, 'wrong result'
    assert solution.maximumUniqueSubarray([5, 2, 1, 2, 5, 2, 1, 2, 5]) == 8, 'wrong result'


if __name__ == '__main__':
    test_maximum_unique_subarray()
