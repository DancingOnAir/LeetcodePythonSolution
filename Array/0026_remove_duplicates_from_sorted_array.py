class Solution:
    def removeDuplicates(self, nums: list) -> int:
        res = 1
        for i in range(len(nums) - 1):
            if nums[i] != nums[i + 1]:
                nums[res] = nums[i + 1]
                res += 1
        return res

    # only return the length of result, but array is incorrect
    def removeDuplicates1(self, nums: list) -> int:
        return len(set(nums))


def test_remove_duplicates():
    solution = Solution()

    nums1 = [1, 1, 2]
    print(solution.removeDuplicates(nums1))

    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(solution.removeDuplicates(nums2))


if __name__ == '__main__':
    test_remove_duplicates()