from typing import List
from collections import deque


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if not nums or k <= 0:
            return False
        m = dict()
        for i in range(len(nums)):
            if nums[i] in m and i - m[nums[i]] <= k:
                return True

            m[nums[i]] = i
        return False


def test_contains_nearby_duplicate():
    solution = Solution()
    assert solution.containsNearbyDuplicate([1, 2, 3, 1], 3), 'wrong result'
    assert solution.containsNearbyDuplicate([1, 0, 1, 1], 1), 'wrong result'
    assert not solution.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2), 'wrong result'


if __name__ == '__main__':
    test_contains_nearby_duplicate()
