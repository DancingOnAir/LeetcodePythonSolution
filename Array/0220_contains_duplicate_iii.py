from typing import List
from collections import OrderedDict


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        def binary_search(arr, target, start, end):
            if start > end:
                return False
            mid = start + (end - start) // 2
            if target - t <= arr[mid] <= target + t:
                return True
            return binary_search(arr, target, start, mid - 1) or binary_search(arr, target, mid + 1, end)

        m = OrderedDict()
        for i, val in enumerate(nums):
            if binary_search(list(m.keys()), val, 0, len(m) - 1):
                return True
            m[val] = i
            if len(m) > k:
                m.pop(nums[i - k])

        return False


def test_contains_nearby_almost_duplicate():
    solution = Solution()
    assert solution.containsNearbyAlmostDuplicate([-3, 3, -6], 2, 3), 'wrong result'
    assert solution.containsNearbyAlmostDuplicate([1, 2, 3, 1], 3, 0), 'wrong result'
    assert solution.containsNearbyAlmostDuplicate([1, 0, 1, 1], 1, 2), 'wrong result'
    assert not solution.containsNearbyAlmostDuplicate([1, 5, 9, 1, 5, 9], 2, 3), 'wrong result'


if __name__ == '__main__':
    test_contains_nearby_almost_duplicate()

