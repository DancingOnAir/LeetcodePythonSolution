from typing import List


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        return sum(sorted(piles, reverse=True)[1: len(piles) * 2 // 3: 2])


def test_max_coins():
    solution = Solution()
    assert solution.maxCoins([2, 4, 1, 2, 7, 8]) == 9, 'wrong result'
    assert solution.maxCoins([2, 4, 5]) == 4, 'wrong result'
    assert solution.maxCoins([9, 8, 7, 6, 5, 1, 2, 3, 4]) == 18, 'wrong result'


if __name__ == '__main__':
    test_max_coins()
