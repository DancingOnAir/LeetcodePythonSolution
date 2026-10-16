class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        vals = sorted((x * x for x in nums), reverse=True)
        p = (len(vals) + 1) // 2
        return sum(vals[:p]) - sum(vals[p:])

    def maxAlternatingSum1(self, nums: list[int]) -> int:
        res = 0
        for i, x in enumerate(sorted(nums, key=lambda x: abs(x))):
            if len(nums) >= (i + 1) * 2:
                res -= x * x
            else:
                res += x * x
        return res


def test_max_alternating_sum():
    solution = Solution()
    assert solution.maxAlternatingSum([1,2,3]) == 12, 'wrong result'
    assert solution.maxAlternatingSum([1,-1,2,-2,3,-3]) == 16, 'wrong result'


if __name__ == '__main__':
    test_max_alternating_sum()
