class Solution:
    def minimumCost(self, cost: list[int]) -> int:
        return sum(x for i, x in enumerate(sorted(cost, reverse=True)) if i % 3 != 2)


def test_minimum_cost():
    solution = Solution()
    assert solution.minimumCost([1, 2, 3]) == 5, 'wrong result'
    assert solution.minimumCost([6, 5, 7, 9, 2, 2]) == 23, 'wrong result'
    assert solution.minimumCost([5, 5]) == 10, 'wrong result'


if __name__ == '__main__':
    test_minimum_cost()
