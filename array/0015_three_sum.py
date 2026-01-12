from typing import List
import bisect


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
        nums = sorted(d)

        res = []
        for i, v in enumerate(nums):
            if not v:
                if d[v] > 2:
                    res.append([0, 0, 0])
            elif d[v] > 1 and -2 * v in d:
                res.append([v, v, -2 * v])

            if v < 0:
                rest = -v
                left = bisect.bisect_left(nums, rest - nums[-1], i + 1)
                right = bisect.bisect_right(nums, rest // 2, left)
                for j in nums[left: right]:
                    k = rest - j
                    if k in d and k != j:
                        res.append([v, k, j])
        return res

    def threeSum1(self, nums: List[int]) -> List[List[int]]:
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
