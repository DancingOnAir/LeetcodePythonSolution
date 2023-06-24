from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = left = zeros = 0

        for right, x in enumerate(nums):
            if x == 0:
                zeros += 1
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            res = max(res, right - left + 1)
        return res


def test_longest_ones():
    solution = Solution()
    assert solution.longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2) == 6, 'wrong result'
    assert solution.longestOnes([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3) == 10, 'wrong result'


if __name__ == '__main__':
    test_longest_ones()
