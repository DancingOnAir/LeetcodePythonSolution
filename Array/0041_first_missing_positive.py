from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 1

        max_val = max(nums)
        for i in range(1, max_val):
            if i not in nums:
                return i
        return max_val + 1 if max_val >= 0 else 1


def test_first_missing_positive():
    solution = Solution()

    nums1 = [1, 2, 0]
    print(solution.firstMissingPositive(nums1))

    nums2 = [3, 4, -1, 1]
    print(solution.firstMissingPositive(nums2))

    nums3 = [7, 8, 9, 11, 12]
    print(solution.firstMissingPositive(nums3))

    nums3 = [-5]
    print(solution.firstMissingPositive(nums3))


if __name__ == '__main__':
    test_first_missing_positive()
