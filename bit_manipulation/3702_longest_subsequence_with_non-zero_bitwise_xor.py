class Solution:
    def longestSubsequence(self, nums: list[int]) -> int:
        xor_sum = or_sum = 0
        for x in nums:
            xor_sum ^= x
            or_sum |= x

        if xor_sum != 0:
            return len(nums)
        elif or_sum != 0:
            return len(nums) - 1
        return 0


def test_longest_subsequence():
    solution = Solution()
    assert solution.longestSubsequence([1,2,3]) == 2, 'wrong result'
    assert solution.longestSubsequence([2,3,4]) == 3, 'wrong result'


if __name__ == '__main__':
    test_longest_subsequence()

