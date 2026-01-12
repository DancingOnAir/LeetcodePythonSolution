from typing import List
from collections import defaultdict


class Solution:
    def maxAmount(self, initialCurrency: str, pairs1: List[List[str]], rates1: List[float], pairs2: List[List[str]],
                  rates2: List[float]) -> float:
        def calc_amount(pairs, rates, initialCurrency):
            g = defaultdict(list)
            for (x, y), r in zip(pairs, rates):
                g[x].append((y, r))
                g[y].append((x, 1.0 / r))

            amount = {}

            def dfs(x, cur):
                amount[x] = cur
                for to, rate in g[x]:
                    if to not in amount:
                        dfs(to, cur * rate)
            dfs(initialCurrency, 1.0)
            return amount

        day1_amount = calc_amount(pairs1, rates1, initialCurrency)
        day2_amount = calc_amount(pairs2, rates2, initialCurrency)
        return max(day1_amount.get(x, 0.0) / a2 for x, a2 in day2_amount.items())


def test_max_amount():
    solution = Solution()
    assert solution.maxAmount("EUR", [["EUR", "USD"], ["USD", "JPY"]], [2.0, 3.0],
                              [["JPY", "USD"], ["USD", "CHF"], ["CHF", "EUR"]],
                              [4.0, 5.0, 6.0]) == 720.00000, 'wrong result'
    assert solution.maxAmount("NGN", [["NGN", "EUR"]], [9.0], [["NGN", "EUR"]], [6.0]) == 1.50000, 'wrong result'


if __name__ == '__main__':
    test_max_amount()
