from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        return sorted(nums, key=lambda x: x == 0)


def test_apply_operations():
    solution = Solution()
    assert solution.applyOperations([1,2,2,1,1,0]) == [1,4,2,0,0,0], 'wrong result'
    assert solution.applyOperations([0,1]) == [1,0], 'wrong result'


if __name__ == '__main__':
    test_apply_operations()
