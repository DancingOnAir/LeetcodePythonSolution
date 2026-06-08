from collections import defaultdict


class Solution:
    def maximumSaleItems(self, items: list[list[int]], budget: int) -> int:
        n = len(items)
        cnt_factor = [0] * (n + 1)
        min_price = float('inf')
        for factor, price in items:
            cnt_factor[factor] += 1
            min_price = min(min_price, price)

        cnt_multi = [0] * (n + 1)
        sum_cnt = defaultdict(int)

        for factor, price in items:
            if price >= min_price * 2:
                continue
            if cnt_multi[factor] == 0:
                for i in range(factor, n + 1, factor):
                    cnt_multi[factor] += cnt_factor[i]
            cnt = cnt_multi[factor] - 1
            if cnt > 0:
                sum_cnt[price] = cnt

        res = 0
        for price in sorted(sum_cnt):
            if budget < price:
                break
            cnt = min(sum_cnt[price], budget // price)
            budget -= cnt * price
            res += cnt * 2
        return res + budget // min_price


def test_maximum_sale_items():
    solution = Solution()
    assert solution.maximumSaleItems([[1, 6], [2, 4], [3, 5]], budget=19) == 5, 'wrong result'
    assert solution.maximumSaleItems([[2, 8], [1, 10], [6, 6], [4, 12], [5, 20], [5, 17]],
                                     budget=35) == 7, 'wrong result'


if __name__ == '__main__':
    test_maximum_sale_items()
