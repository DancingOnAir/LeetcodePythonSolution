class Solution:
    def maximumSaleItems(self, items: list[list[int]], budget: int) -> int:
        max_factor = max(item[0] for item in items)
        cnt_factor = [0] * (max_factor + 1)
        for factor, _ in items:
            cnt_factor[factor] += 1

        cnt_multi = [0] * (max_factor + 1)
        dp = [0] * (budget + 1)
        min_price = float('inf')
        sum_price = 0

        for factor, price in items:
            min_price = min(min_price, price)
            if cnt_multi[factor] == 0:
                for i in range(factor, max_factor + 1, factor):
                    cnt_multi[factor] += cnt_factor[i]
            cnt = cnt_multi[factor]

            sum_price = min(sum_price + price, budget)
            for i in range(sum_price, price - 1, -1):
                v = dp[i - price] + cnt
                if v > dp[i]:
                    dp[i] = v
        return max(x + (budget - i) // min_price for i, x in enumerate(dp))


def test_maximum_sale_items():
    solution = Solution()
    assert solution.maximumSaleItems([[6, 2], [2, 6], [3, 4]], budget=9) == 4, 'wrong result'
    assert solution.maximumSaleItems([[2, 4], [3, 2], [4, 1], [6, 4], [12, 4]], budget=8) == 10, 'wrong result'


if __name__ == '__main__':
    test_maximum_sale_items()
