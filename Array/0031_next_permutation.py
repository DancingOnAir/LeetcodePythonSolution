from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        i = j = n - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        if i == 0:
            nums.reverse()
            return

        k = i - 1
        while j > 0 and nums[j] <= nums[k]:
            j -= 1

        nums[j], nums[k] = nums[k], nums[j]
        left, right = k + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return


def test_next_permutation():
    solution = Solution()

    nums1 = [1, 2, 3]
    solution.nextPermutation(nums1)
    print(nums1)

    nums2 = [3, 2, 1]
    solution.nextPermutation(nums2)
    print(nums2)

    nums3 = [1, 1, 5]
    solution.nextPermutation(nums3)
    print(nums3)


if __name__ == '__main__':
    test_next_permutation()
