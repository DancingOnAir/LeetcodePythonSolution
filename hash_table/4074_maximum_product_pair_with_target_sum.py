from collections import defaultdict


class Solution:
    def maxProductPair(self, nums: list[int], target: int) -> list[int]:
        res = [-1, -1]
        m = defaultdict(int)
        for i, x in enumerate(nums):
            if x in m:
                if res == [-1, -1] or nums[res[0]] * nums[res[1]] < x * nums[m[x]]:
                    if 2 * x > target:
                        res = [i, m[x]]
                    elif 2 * x < target:
                        res = [m[x], i]
            else:
                m[target - x] = i
        return res


def test_max_product_pair():
    solution = Solution()
    # assert solution.maxProductPair([1, 2, 3, 4], target=5) == [2, 1], 'wrong result'
    # assert solution.maxProductPair([-3, -1, 4, 2], target=1) == [3, 1], 'wrong result'
    assert solution.maxProductPair([3, 3, 5], target=6) == [-1, -1], 'wrong result'


if __name__ == '__main__':
    test_max_product_pair()
