from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)

        n = len(nums)
        res = []

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                rest = target - nums[i] - nums[j]
                left, right = j + 1, n - 1

                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                while left < right:
                    if nums[left] + nums[right] < rest:
                        left += 1
                    elif nums[left] + nums[right] > rest:
                        right -= 1
                    else:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1

                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
        return res


def test_four_sum():
    solution = Solution()

    nums1 = [1, 0, -1, 0, -2, 2]
    target1 = 0
    print(solution.fourSum(nums1, target1))

    nums2 = [-3, -2, -1, 0, 0, 1, 2, 3]
    target2 = 0
    print(solution.fourSum(nums2, target2))

    nums3 = [-1, 0, 1, 2, -1, -4]
    target3 = -1
    print(solution.fourSum(nums3, target3))

    nums4 = [-1, 0, -5, -2, -2, -4, 0, 1, -2]
    target4 = -9
    print(solution.fourSum(nums4, target4))


if __name__ == '__main__':
    test_four_sum()
