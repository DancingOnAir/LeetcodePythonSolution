class Solution:
    def longestSubarraysDivByK(self, nums: list[int], k: int) -> int:
        first_pos = {0: -1}
        ps = res = 0
        for r, x in enumerate(nums):
            ps = (ps + x) % k
            if ps in first_pos:
                res = max(res, r - first_pos[ps])
            else:
                first_pos[ps] = r
        return res

    def longestSubarray(self, nums: list[int], k: int) -> int:
        res = self.longestSubarraysDivByK(nums, k)

        for i in range(len(nums)):
            nums[i] *= -1
            res = max(res, self.longestSubarraysDivByK(nums, k))
            nums[i] *= -1
        return res


def test_longest_subarray():
    solution = Solution()
    assert solution.longestSubarray([4,1,2], k = 3) == 3, 'wrong result'
    assert solution.longestSubarray([5,3,4], k = 7) == 2, 'wrong result'
    assert solution.longestSubarray([2,2,5], k = 6) == 2, 'wrong result'


if __name__ == '__main__':
    test_longest_subarray()
