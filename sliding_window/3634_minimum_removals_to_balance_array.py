from typing import List


class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        if len(nums) < 2:
            return 0

        nums.sort()
        left = res = 0
        for right, x in enumerate(nums):
            while nums[right] > nums[left] * k:
                left += 1
            res = max(res, right - left + 1)
        return len(nums) - res


def test_min_removal():
    solution = Solution()
    assert solution.minRemoval([20,5,11], k=2) == 1, 'wrong result'
    assert solution.minRemoval([2, 1, 5], k=2) == 1, 'wrong result'
    assert solution.minRemoval([1, 6, 2, 9], k=3) == 2, 'wrong result'
    assert solution.minRemoval([4, 6], k=2) == 0, 'wrong result'


if __name__ == '__main__':
    test_min_removal()
