from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return n

        res = 2
        suf = [0] * n
        suf[-1] = 1
        for i in range(n - 2, 0, -1):
            if nums[i] <= nums[i + 1]:
                suf[i] += suf[i + 1] + 1
                res = max(res, suf[i] + 1)
            else:
                suf[i] = 1

        pre = 1
        for i in range(1, n - 1):
            if nums[i - 1] <= nums[i + 1]:
                res = max(res, pre + 1 + suf[i + 1])

            if nums[i - 1] <= nums[i]:
                pre += 1
                res = max(res, pre + 1)
            else:
                pre = 1
        return res


def test_longest_subarray():
    solution = Solution()
    assert solution.longestSubarray([1, 2, 3, 1, 2]) == 4, 'wrong result'
    assert solution.longestSubarray([2, 2, 2, 2, 2]) == 5, 'wrong result'


if __name__ == '__main__':
    test_longest_subarray()
