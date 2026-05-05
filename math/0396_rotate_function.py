class Solution:
    def maxRotateFunction(self, nums: list[int]) -> int:
        pre_sum = sum(nums)
        n = len(nums)
        res = tot = sum(i * x for i, x in enumerate(nums))
        for i in range(1, n):
            tot += pre_sum - n * nums[n - i]
            res = max(res, tot)
        return res


def test_max_rotate_function():
    solution = Solution()
    assert solution.maxRotateFunction([4, 3, 2, 6]) == 26, 'wrong result'
    assert solution.maxRotateFunction([100]) == 0, 'wrong result'


if __name__ == '__main__':
    test_max_rotate_function()
