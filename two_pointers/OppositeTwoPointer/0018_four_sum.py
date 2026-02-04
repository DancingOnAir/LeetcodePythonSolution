from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = list()
        for i in range(n - 3):
            x = nums[i]
            if i > 0 and nums[i - 1] == x:
                continue
            if x + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            if x + nums[-3] + nums[-2] + nums[-1] < target:
                continue

            for j in range(i + 1, n - 2):
                y = nums[j]
                if j > i + 1 and nums[j - 1] == y:
                    continue
                if x + y + nums[j + 1] + nums[j + 2] > target:
                    break
                if x + y + nums[-2] + nums[-1] < target:
                    continue

                left = j + 1
                right = n - 1
                while left < right:
                    s = x + y + nums[left] + nums[right]
                    if s < target:
                        left += 1
                    elif s > target:
                        right -= 1
                    else:
                        res.append([x, y, nums[left], nums[right]])
                        left += 1
                        while left < right and nums[left - 1] == nums[left]:
                            left += 1

                        right -= 1
                        while left < right and nums[right + 1] == nums[right]:
                            right -= 1
        return res


def test_four_sum():
    solution = Solution()
    assert solution.fourSum([-3, -1, 0, 4], 0) == [[-3, -1, 0, 4]], 'wrong result'
    assert solution.fourSum([1, 0, -1, 0, -2, 2], 0) == [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]], 'wrong result'
    assert solution.fourSum([2, 2, 2, 2, 2], 8) == [[2, 2, 2, 2]], 'wrong result'


if __name__ == '__main__':
    test_four_sum()
