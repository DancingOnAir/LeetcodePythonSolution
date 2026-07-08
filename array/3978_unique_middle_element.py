class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        return nums.count(nums[len(nums) // 2]) == 1

    def isMiddleElementUnique1(self, nums: list[int]) -> bool:
        mid = len(nums) // 2
        for i, x in enumerate(nums):
            if i != mid and x == nums[mid]:
                return False
        return True


def test_is_middle_element_unique():
    solution = Solution()
    assert solution.isMiddleElementUnique([1,2,3]) == True, 'wrong result'
    assert solution.isMiddleElementUnique([1,2,2]) == False, 'wrong result'


if __name__ == '__main__':
    test_is_middle_element_unique()
