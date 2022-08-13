from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]


def test_find_kth_largest():
    solution = Solution()
    assert solution.findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5, 'wrong result'
    assert solution.findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5, 'wrong result'


if __name__ == '__main__':
    test_find_kth_largest()
