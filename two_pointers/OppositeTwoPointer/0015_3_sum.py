from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = list()

        for i in range(n - 2):
            x = nums[i]
            if i > 0 and nums[i - 1] == x:
                continue
            if x + nums[i + 1] + nums[i + 2] > 0:
                break
            if x + nums[-2] + nums[-1] < 0:
                continue

            j, k = i + 1, n - 1
            while j < k:
                s = x + nums[j] + nums[k]
                if s < 0:
                    j += 1
                elif s > 0:
                    k -= 1
                else:
                    res.append([x, nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j - 1] == nums[j]:
                        j += 1
                    k -= 1
                    while j < k and nums[k + 1] == nums[k]:
                        k -= 1
        return res


def test_three_sum():
    solution = Solution()
    assert solution.threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]], 'wrong result'
    assert solution.threeSum([0, 1, 1]) == [], 'wrong result'
    assert solution.threeSum([0, 0, 0]) == [[0, 0, 0]], 'wrong result'


if __name__ == '__main__':
    test_three_sum()
