class Solution:
    def minIncrease(self, nums: list[int]) -> int:
        n = len(nums)
        suf = [0] * (n + 1)
        for i in range(n - 2, 0, -2):
            suf[i] = suf[i + 2] + max(0, max(nums[i - 1], nums[i + 1]) - nums[i] + 1)

        if n % 2 == 1:
            return suf[1]

        res = suf[2]
        pre = 0
        for i in range(1, n - 1, 2):
            pre += max(max(nums[i - 1], nums[i + 1]) - nums[i] + 1, 0)
            res = min(res, pre + suf[i + 3])

        return res


def test_min_increase():
    solution = Solution()
    assert solution.minIncrease([1, 2, 2]) == 1, 'wrong result'
    assert solution.minIncrease([2, 1, 1, 3]) == 2, 'wrong result'
    assert solution.minIncrease([5, 2, 1, 4, 3]) == 4, 'wrong result'


if __name__ == '__main__':
    test_min_increase()
