from typing import List


class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        left, right = min(nums), max(nums)
        while left <= right:
            mid = left + (right - left) // 2
            last = take = 0
            for x in nums:
                if last != 0:
                    last = 0
                    continue

                if mid >= x:
                    take += 1
                    last = 1

            if take >= k:
                right = mid - 1
            else:
                left = mid + 1

        return left


def test_min_capability():
    solution = Solution()
    assert solution.minCapability([7, 3, 9, 5], 2) == 5, 'wrong result'
    assert solution.minCapability([2, 3, 5, 9], 2) == 5, 'wrong result'
    assert solution.minCapability([2, 7, 9, 3, 1], 2) == 2, 'wrong result'


if __name__ == '__main__':
    test_min_capability()
