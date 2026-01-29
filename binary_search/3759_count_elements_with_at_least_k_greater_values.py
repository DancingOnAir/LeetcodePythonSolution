from typing import List
from bisect import bisect_left


class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = bisect_left(nums, nums[-k])
        return i


def test_count_elements():
    solution = Solution()
    assert solution.countElements([3, 1, 2], 1) == 2, 'wrong result'
    assert solution.countElements([5, 5, 5], 2) == 0, 'wrong result'


if __name__ == '__main__':
    test_count_elements()
