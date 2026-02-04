from typing import List
from collections import defaultdict


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        m = len(set(nums))
        res, left = 0, 0
        for right, x in enumerate(nums):
            freq[x] += 1
            while left <= right and len(freq) == m:
                res += len(nums) - right
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1
        return res


def test_count_complete_subarrays():
    solution = Solution()
    # assert solution.countCompleteSubarrays([1, 3, 1, 2, 2]) == 4, 'wrong result'
    assert solution.countCompleteSubarrays([5, 5, 5, 5]) == 10, 'wrong result'


if __name__ == '__main__':
    test_count_complete_subarrays()
