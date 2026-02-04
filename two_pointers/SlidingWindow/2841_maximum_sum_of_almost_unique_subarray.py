from typing import List
from collections import Counter


class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        res = left = tot = 0
        cnt = Counter()
        for right, x in enumerate(nums):
            cnt[x] += 1
            tot += x
            if right - left + 1 == k:
                if len(cnt) >= m:
                    res = max(res, tot)

                cnt[nums[left]] -= 1
                if cnt[nums[left]] == 0:
                    del cnt[nums[left]]
                tot -= nums[left]
                left += 1
        return res


def test_max_sum():
    solution = Solution()
    assert solution.maxSum([2, 6, 7, 3, 1, 7], m=3, k=4) == 18, 'wrong result'
    assert solution.maxSum([5, 9, 9, 2, 4, 5, 4], m=1, k=3) == 23, 'wrong result'
    assert solution.maxSum([1, 2, 1, 2, 1, 2, 1], m=3, k=3) == 0, 'wrong result'


if __name__ == '__main__':
    test_max_sum()
