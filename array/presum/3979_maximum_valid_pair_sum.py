class Solution:
    def maxValidPairSum(self, nums: list[int], k: int) -> int:
        n = len(nums)
        res = mx = 0
        suffix_max = [0] * n
        for i in range(n - 1, -1, -1):
            mx = max(mx, nums[i])
            suffix_max[i] = mx

        for i in range(n - k):
            res = max(res, nums[i] + suffix_max[i + k])
        return res


def test_max_valid_pair_sum():
    solution = Solution()
    assert solution.maxValidPairSum([1,3,5,2,8], 2) == 13, 'wrong result'
    assert solution.maxValidPairSum([5,1,9], 1) == 14, 'wrong result'


if __name__ == '__main__':
    test_max_valid_pair_sum()
