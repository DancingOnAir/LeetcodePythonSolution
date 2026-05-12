class Solution:
    def minCost(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        n = len(nums)
        ps_left = [0] * n
        ps_right = [0] * n
        for i in range(1, n):
            # i -> i - 1
            if i < n - 1 and abs(nums[i + 1] - nums[i]) < abs(nums[i] - nums[i - 1]):
                cost = abs(nums[i] - nums[i - 1])
            else:
                cost = 1
            ps_left[i] = ps_left[i - 1] + cost
            # i - 1 -> i
            if i > 1 and abs(nums[i - 2] - nums[i - 1]) <= abs(nums[i - 1] - nums[i]):
                cost = abs(nums[i - 1] - nums[i])
            else:
                cost = 1
            ps_right[i] = ps_right[i - 1] + cost

        res = [0] * len(queries)
        for i, (l, r) in enumerate(queries):
            if l < r:
                res[i] = ps_right[r] - ps_right[l]
            else:
                res[i] = ps_left[l] - ps_left[r]
        return res


def test_min_cost():
    solution = Solution()
    assert solution.minCost([-5, -2, 3], queries=[[0, 2], [2, 0], [1, 2]]) == [6, 2, 5], 'wrong result'
    assert solution.minCost([0, 2, 3, 9], queries=[[3, 0], [1, 2], [2, 0]]) == [4, 1, 3], 'wrong result'


if __name__ == '__main__':
    test_min_cost()
