from typing import List
from itertools import groupby


class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        memo = [(k, len(list(g))) for k, g in groupby(s)]
        res = start = 0
        for i in range(len(memo)):
            l = memo[i][1]
            res += max(cost[start: start + l])
            start += l
        return sum(cost) - res


def test_min_cost():
    solution = Solution()
    assert solution.minCost('abaac', [1, 2, 3, 4, 5]) == 3, 'wrong result'
    assert solution.minCost('abc', [1, 2, 3]) == 0, 'wrong result'
    assert solution.minCost('aabaa', [1, 2, 3, 4, 1]) == 2, 'wrong result'


if __name__ == '__main__':
    test_min_cost()
