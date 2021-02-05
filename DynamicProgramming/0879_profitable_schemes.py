from typing import List


class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        pass


def test_profitable_schemes():
    solution = Solution()
    assert solution.profitableSchemes(5, 3, [2, 2], [2, 3]) == 2, 'wrong result'
    assert solution.profitableSchemes(10, 5, [2, 3, 5], [6, 7, 8]) == 7, 'wrong result'


if __name__ == '__main__':
    test_profitable_schemes()
