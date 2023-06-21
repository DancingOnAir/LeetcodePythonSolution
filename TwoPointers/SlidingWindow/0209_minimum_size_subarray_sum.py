from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)

        res = n + 1
        total = i = 0
        for j, x in enumerate(nums):
            total += x
            while total >= target:
                res = min(res, j + 1 - i)
                total -= nums[i]
                i += 1
        return res if res <= n else 0


def test_min_sub_array_len():
    solution = Solution()
    assert solution.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]) == 2, 'wrong result'
    assert solution.minSubArrayLen(4, [1, 4, 4]) == 1, 'wrong result'
    assert solution.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]) == 0, 'wrong result'


if __name__ == '__main__':
    test_min_sub_array_len()
