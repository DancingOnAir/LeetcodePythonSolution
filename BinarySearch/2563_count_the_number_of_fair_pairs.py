from typing import List


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        if n < 2:
            return 0
        nums.sort()
        res = 0
        for i in range(n):
            left = i + 1
            right = n - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[i] + nums[mid] <= upper:
                    left = mid + 1
                else:
                    right = mid - 1
            right_bound = left - 1

            left = i + 1
            right = n - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[i] + nums[mid] >= lower:
                    right = mid - 1
                else:
                    left = mid + 1
            left_bound = left
            res += right_bound + 1 - left_bound if right_bound >= left_bound else 0

        return res


def test_count_fair_pairs():
    solution = Solution()
    assert solution.countFairPairs([-5, -7, -5, -7, -5], -12, -12) == 6, 'wrong result'
    assert solution.countFairPairs([0, 1, 7, 4, 4, 5], 3, 6) == 6, 'wrong result'
    assert solution.countFairPairs([1, 7, 9, 2, 5], 11, 11) == 1, 'wrong result'


if __name__ == '__main__':
    test_count_fair_pairs()
