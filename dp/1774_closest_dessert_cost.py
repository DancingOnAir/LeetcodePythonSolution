from typing import List


class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        def closest(x, y):
            if abs(x - target) == abs(y - target):
                return x if x < y else y
            return x if abs(x - target) < abs(y - target) else y

        def dfs(i, tot):
            if i >= len(toppingCosts):
                return tot

            a = dfs(i + 1, tot + toppingCosts[i])
            b = dfs(i + 1, tot + toppingCosts[i] * 2)
            c = dfs(i + 1, tot)

            tot = closest(a, closest(b, c))
            return tot

        res = 0
        for x in baseCosts:
            res = closest(res, dfs(0, x))
        return res


def test_closest_cost():
    solution = Solution()
    assert solution.closestCost([1, 7], [3, 4], 10) == 10, 'wrong result'
    assert solution.closestCost([2, 3], [4, 5, 100], 18) == 17, 'wrong result'
    assert solution.closestCost([3, 10], [2, 5], 9) == 8, 'wrong result'


if __name__ == '__main__':
    test_closest_cost()
