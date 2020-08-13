from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 1

        for i in range(len(nums)):
            while 1 <= nums[i] <= len(nums) and nums[nums[i] - 1] != nums[i]:
                tmp = nums[i] - 1
                nums[i], nums[tmp] = nums[tmp], nums[i]

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1

    def firstMissingPositive1(self, nums: List[int]) -> int:
        if not nums:
            return 1

        # O(n)
        max_val = max(nums)
        # O(n)
        for i in range(1, max_val):
            # O(n)
            if i not in nums:
                return i
        return max_val + 1 if max_val >= 0 else 1


def test_first_missing_positive():
    solution = Solution()

    nums1 = [1, 2, 0]
    print(solution.firstMissingPositive(nums1))

    nums2 = [3, 4, 0, 2]
    print(solution.firstMissingPositive(nums2))

    nums3 = [7, 8, 9, 11, 12]
    print(solution.firstMissingPositive(nums3))

    nums4 = [2]
    print(solution.firstMissingPositive(nums4))


if __name__ == '__main__':
    test_first_missing_positive()
