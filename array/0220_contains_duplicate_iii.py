from typing import List
from collections import OrderedDict
from bisect import bisect_left, bisect_right
from sortedcontainers import SortedList


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t < 0:
            return False
        n = len(nums)
        w = t + 1
        bucket = dict()

        for i, val in enumerate(nums):
            j = val // w
            if j in bucket:
                return True
            elif j - 1 in bucket and abs(nums[i] - bucket[j - 1]) < w:
                return True
            elif j + 1 in bucket and abs(nums[i] - bucket[j + 1]) < w:
                return True
            bucket[j] = nums[i]
            if i >= k:
                del bucket[nums[i - k] // w]
        return False

    def containsNearbyAlmostDuplicate2(self, nums: List[int], k: int, t: int) -> bool:
        m = SortedList()
        for i, val in enumerate(nums):
            pos1 = bisect_left(m, val - t)
            pos2 = bisect_right(m, val + t)
            if pos1 != pos2 and pos1 != len(m):
                return True

            m.add(nums[i])
            if i >= k:
                m.remove(nums[i - k])
        return False

    # TLE
    def containsNearbyAlmostDuplicate1(self, nums: List[int], k: int, t: int) -> bool:
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
    assert solution.containsNearbyAlmostDuplicate([7, 2, 8], 2, 1), 'wrong result'
    assert solution.containsNearbyAlmostDuplicate([-3, 3, -6], 2, 3), 'wrong result'
    assert solution.containsNearbyAlmostDuplicate([1, 2, 3, 1], 3, 0), 'wrong result'
    assert solution.containsNearbyAlmostDuplicate([1, 0, 1, 1], 1, 2), 'wrong result'
    assert not solution.containsNearbyAlmostDuplicate([1, 5, 9, 1, 5, 9], 2, 3), 'wrong result'


if __name__ == '__main__':
    test_contains_nearby_almost_duplicate()

