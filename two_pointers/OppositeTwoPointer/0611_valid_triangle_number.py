from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        res = 0
        for i in range(2, n):
            x = nums[i]

            left, right = 0, i - 1
            while left < right:
                if nums[left] + nums[right] <= x:
                    left += 1
                else:
                    res += right - left
                    right -= 1
        return res

    def triangleNumber1(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        res = 0
        for i in range(n - 1, 1, -1):
            x = nums[i]

            left, right = 0, i - 1
            while left < right:
                if nums[left] + nums[right] <= x:
                    left += 1
                else:
                    res += right - left
                    right -= 1
        return res


def test_triangle_number():
    solution = Solution()
    assert solution.triangleNumber([2, 2, 3, 4]) == 3, 'wrong result'
    assert solution.triangleNumber([4, 2, 3, 4]) == 4, 'wrong result'


if __name__ == '__main__':
    test_triangle_number()
