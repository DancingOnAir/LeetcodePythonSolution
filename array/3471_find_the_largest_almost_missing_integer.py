from typing import List
from collections import Counter


class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        def helper(x, arr):
            return -1 if x in arr else x

        if k == len(nums):
            return max(nums)

        if k == 1:
            cnt = Counter(nums)
            return max([x for x in cnt if cnt[x] == 1], default=-1)

        return max(helper(nums[0], nums[1:]), helper(nums[-1], nums[:-1]))


def test_count_arrays():
    solution = Solution()
    assert solution.largestInteger([3, 9, 2, 1, 7], k=3) == 7, 'wrong result'
    assert solution.largestInteger([3, 9, 7, 2, 1, 7], k=4) == 3, 'wrong result'
    assert solution.largestInteger([0, 0], k=1) == -1, 'wrong result'


if __name__ == '__main__':
    test_count_arrays()
