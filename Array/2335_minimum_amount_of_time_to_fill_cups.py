from typing import List


class Solution:
    def fillCups(self, amount: List[int]) -> int:
        amount.sort()
        res = 0
        while amount[2] != 0:
            res += 1
            amount[2] -= 1
            amount[1] -= 1
            amount.sort()
        return res


def test_fill_cups():
    solution = Solution()
    assert solution.fillCups([1, 4, 2]) == 4, 'wrong result'
    assert solution.fillCups([5, 4, 4]) == 7, 'wrong result'
    assert solution.fillCups([5, 0, 0]) == 5, 'wrong result'


if __name__ == '__main__':
    test_fill_cups()
