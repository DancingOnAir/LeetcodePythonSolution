class Solution:
    def minCost(self, nums: list[int]) -> int:
        n = len(nums)
        res = float('inf')
        start = 0
        for i, x in enumerate(nums):
            if i == n - 1 or x != nums[i + 1]:
                if i > 0 and start < n - 1:
                    res = min(res, (start + n - i - 1) * x)
                start = i + 1
        return res


def test_min_cost():
    solution = Solution()
    assert solution.minCost([1,2,3]) == 4, 'wrong result'
    assert solution.minCost([3,3,3,6,3,3]) == 9, 'wrong result'
    assert solution.minCost([3,4,4,5,4,4,3]) == 20, 'wrong result'


if __name__ == '__main__':
    test_min_cost()
