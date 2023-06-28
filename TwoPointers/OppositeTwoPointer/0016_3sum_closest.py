from typing import List
from math import inf


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        n = len(nums)
        diff = inf
        res = 0
        for i in range(n - 2):
            x = nums[i]
            j, k = i + 1, n - 1
            while j < k:
                s = x + nums[j] + nums[k]
                if diff > abs(s - target):
                    diff = abs(s - target)
                    res = s
                if s < target:
                    j += 1
                    while j < k and nums[j - 1] == nums[j]:
                        j += 1
                elif s > target:
                    k -= 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                else:
                    break
        return res


def test_three_sum_closest():
    solution = Solution()
    assert solution.threeSumClosest([-1, 2, 1, -4], 1) == 2, 'wrong result'
    assert solution.threeSumClosest([0, 0, 0], 1) == 0, 'wrong result'


if __name__ == '__main__':
    test_three_sum_closest()
