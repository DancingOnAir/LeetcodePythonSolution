from typing import List


class Solution:
    def triangleType(self, nums: List[int]) -> str:
        if nums[0] + nums[1] > nums[2] and nums[1] + nums[2] > nums[0] and nums[0] + nums[2] > nums[1]:
            if nums[0] == nums[1] == nums[2]:
                return "equilateral"
            elif nums[0] != nums[1] and nums[1] != nums[2] and nums[0] != nums[2]:
                return "scalene"
            else:
                return "isosceles"
        return "none"

    # sort O(n):nlog(n)
    def triangleType1(self, nums: List[int]) -> str:
        nums.sort()
        if nums[0] + nums[1] <= nums[2]:
            return "none"
        elif nums[0] == nums[2]:
            return "equilateral"
        elif nums[0] == nums[1] or nums[1] == nums[2]:
            return "isosceles"

        return "scalene"


def test_triangle_type():
    solution = Solution()
    assert solution.triangleType([3, 3, 3]) == "equilateral", 'wrong result'
    assert solution.triangleType([3, 4, 5]) == "scalene", 'wrong result'


if __name__ == '__main__':
    test_triangle_type()
