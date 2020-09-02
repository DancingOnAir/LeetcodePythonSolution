from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for n in nums:
            if i < 2 or n > nums[i - 2]:
                nums[i] = n
                i += 1
        return i

    def removeDuplicates1(self, nums: List[int]) -> int:
        count = 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] == nums[i + 1]:
                count += 1
            else:
                count = 1

            if count > 2:
                nums.pop(i)
                count -= 1

        return len(nums)


def test_remove_duplicates():
    solution = Solution()

    nums1 = [1, 1, 1, 2, 2, 3]
    print(solution.removeDuplicates(nums1))
    print(nums1)

    nums2 = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    print(solution.removeDuplicates(nums2))
    print(nums2)


if __name__ == '__main__':
    test_remove_duplicates()
