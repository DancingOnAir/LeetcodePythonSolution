from typing import List


class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        horizontalCut.sort()
        verticalCut.sort()
        sum_h = sum(horizontalCut)
        sum_v = sum(verticalCut)
        res = 0

        while horizontalCut and verticalCut:
            if horizontalCut[-1] > verticalCut[-1]:
                res += horizontalCut[-1] + sum_v
                sum_h -= horizontalCut.pop()
            else:
                res += verticalCut[-1] + sum_h
                sum_v -= verticalCut.pop()
        return sum_h + sum_v + res


def test_minimum_cost():
    solution = Solution()
    assert solution.minimumCost(6, 3, [2, 3, 2, 3, 1], [1, 2]) == 28, 'wrong result'
    assert solution.minimumCost(3, 2, [1, 3], [5]) == 13, 'wrong result'
    assert solution.minimumCost(2, 2, [7], [4]) == 15, 'wrong result'


if __name__ == '__main__':
    test_minimum_cost()