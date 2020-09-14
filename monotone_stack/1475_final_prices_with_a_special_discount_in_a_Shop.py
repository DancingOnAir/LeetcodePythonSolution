from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res, stk = prices[:], []

        for i in range(len(prices)):
            while stk and prices[stk[-1]] >= prices[i]:
                cur = stk.pop()
                res[cur] = prices[cur] - prices[i]
            stk.append(i)
        return res


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
