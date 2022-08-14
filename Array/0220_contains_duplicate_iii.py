from typing import List
from collections import OrderedDict


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        # m = set()
        m = OrderedDict()
        for x in nums:
            if x in m:

            m.add(x)
        pass


def test_contains_nearby_almost_duplicate():
    solution = Solution()
    assert solution.containsNearbyAlmostDuplicate([1, 2, 3, 1], 3, 0), 'wrong result'
    assert solution.containsNearbyAlmostDuplicate([1, 0, 1, 1], 1, 2), 'wrong result'
    assert not solution.containsNearbyAlmostDuplicate([1, 5, 9, 1, 5, 9], 2, 3), 'wrong result'


if __name__ == '__main__':
    test_contains_nearby_almost_duplicate()

