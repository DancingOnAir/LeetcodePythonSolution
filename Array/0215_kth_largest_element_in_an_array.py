from typing import List
from random import choice


class Solution:
    # quick select
    # https://leetcode.com/problems/kth-largest-element-in-an-array/discuss/1019513/Python-QuickSelect-average-O(n)-explained
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivot = choice(nums)
        left = [x for x in nums if x > pivot]
        mid = [x for x in nums if x == pivot]
        right = [x for x in nums if x < pivot]

        if k <= len(left):
            return self.findKthLargest(left, k)
        elif k > len(left) + len(mid):
            return self.findKthLargest(right, k - len(left) - len(mid))
        else:
            return mid[0]

    def findKthLargest1(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]


def test_find_kth_largest():
    solution = Solution()
    assert solution.findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5, 'wrong result'
    assert solution.findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5, 'wrong result'


if __name__ == '__main__':
    test_find_kth_largest()
