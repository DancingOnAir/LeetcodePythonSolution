class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        if costBoth > cost1 + cost2:
            return cost1 * need1 + cost2 * need2

        if need1 > need2:
            need1, need2 = need2, need1
            cost1, cost2 = cost2, cost1

        return costBoth * need1 + min(cost2, costBoth) * (need2 - need1)


def test_minimum_cost():
    solution = Solution()
    assert solution.minimumCost(3, cost2 = 2, costBoth = 1, need1 = 3, need2 = 2) == 3, 'wrong result'
    assert solution.minimumCost(5, cost2 = 4, costBoth = 15, need1 = 2, need2 = 3) == 22, 'wrong result'
    assert solution.minimumCost(5, cost2 = 4, costBoth = 15, need1 = 0, need2 = 0) == 0, 'wrong result'


if __name__ == '__main__':
    test_minimum_cost()
