from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stk = list()
        res = prices[:]
        for i in range(len(prices)):
            while stk and prices[stk[-1]] >= prices[i]:
                res[stk.pop()] -= prices[i]
            stk.append(i)
        return res


def test_final_prices():
    solution = Solution()
    assert solution.finalPrices([8, 4, 6, 2, 3]) == [4, 2, 4, 2, 3], 'wrong result'
    assert solution.finalPrices([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5], 'wrong result'


if __name__ == '__main__':
    test_final_prices()

