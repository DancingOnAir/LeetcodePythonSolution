from typing import List


class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        coins.sort()
        res, mx, i = 0, 0, 0
        while mx < target:
            if i < len(coins) and coins[i] <= mx + 1:
                mx += coins[i]
                i += 1
            else:
                mx += mx + 1
                res += 1
        return res


def test_minimum_added_coins():
    solution = Solution()
    assert solution.minimumAddedCoins([1, 4, 10], 19) == 2, 'wrong result'
    assert solution.minimumAddedCoins([1, 4, 10, 5, 7, 19], 19) == 1, 'wrong result'
    assert solution.minimumAddedCoins([1, 1, 1], 20) == 3, 'wrong result'


if __name__ == '__main__':
    test_minimum_added_coins()
