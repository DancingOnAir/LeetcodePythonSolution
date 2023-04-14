from typing import List


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        left, right = 0, nums[-1] - nums[0]
        while left <= right:
            mid = (left + right) // 2

            cnt = 0
            i = 1
            while i < len(nums):
                if nums[i] - nums[i - 1] <= mid:
                    cnt += 1
                    i += 1
                i += 1

            if cnt < p:
                left = mid + 1
            else:
                right = mid - 1
        return left


def test_minimize_max():
    solution = Solution()
    assert solution.minimizeMax([10, 1, 2, 7, 1, 3], 2) == 1, 'wrong result'
    assert solution.minimizeMax([4, 2, 1, 2], 1) == 0, 'wrong result'


if __name__ == '__main__':
    test_minimize_max()
