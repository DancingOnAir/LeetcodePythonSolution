from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1

            if nums[left] > -nums[i]:
                break

            while left < right:
                if nums[left] + nums[right] > -nums[i]:
                    right -= 1
                elif nums[left] + nums[right] < -nums[i]:
                    left += 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return res


def test_three_sum() -> None:
    solution = Solution()
    nums1 = [-1, 0, 1, 2, -1, -4]
    print(solution.threeSum(nums1))

    nums2 = [0, 0, 0, 0]
    print(solution.threeSum(nums2))

    nums3 = [-2, 0, 0, 2, 2]
    print(solution.threeSum(nums3))


if __name__ == '__main__':
    test_three_sum()
