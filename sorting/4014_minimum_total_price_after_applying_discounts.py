from operator import mul


class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        prices.sort(reverse=True)
        discounts.sort(reverse=True)
        tot = sum(prices)
        saving = sum(map(mul, prices, discounts))
        return tot - saving / 100

    def minPrice1(self, prices: list[int], discounts: list[int]) -> float:
        prices.sort(reverse=True)
        discounts.sort(reverse=True)

        res = 0.0
        for i, p in enumerate(prices):
            if i < len(discounts):
                res += p * (100 - discounts[i]) / 100
            else:
                res += p
        return res


def test_min_price():
    solution = Solution()
    assert solution.minPrice([10,30,21], discounts = [50,60]) == 32.50000, 'wrong result'
    assert solution.minPrice([100,70], discounts = [10,40,50]) == 92.00000, 'wrong result'
    assert solution.minPrice([7,3,9], discounts = [100,100]) == 3.00000, 'wrong result'


if __name__ == '__main__':
    test_min_price()
