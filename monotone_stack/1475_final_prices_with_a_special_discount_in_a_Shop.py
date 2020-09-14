from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stk = []

        for i, num in enumerate(prices):
            while stk and prices[stk[-1]] >= num:
                prices[stk.pop()] -= num
            stk.append(i)
        return prices


def test_final_prices():
    solution = Solution()

    prices1 = [8, 4, 6, 2, 3]
    print(solution.finalPrices(prices1))

    prices2 = [1, 2, 3, 4, 5]
    print(solution.finalPrices(prices2))

    prices3 = [10, 1, 1, 6]
    print(solution.finalPrices(prices3))


if __name__ == '__main__':
    test_final_prices()
