from typing import List
from functools import lru_cache


class Solution:
    # 错误的思路，比如[1, 2, 2, 3, 3], [1, 2]
    # horizontalCut.sort()
    # verticalCut.sort()
    # res, r, c = 0, 1, 1
    # while r < m or c < n:
    #     if r < m and c < n:
    #         if r * verticalCut[-1] > c * horizontalCut[-1]:
    #             res += verticalCut.pop() * r
    #             c += 1
    #         else:
    #             res += horizontalCut.pop() * c
    #             r += 1
    #     elif r < m:
    #         res += horizontalCut.pop() * c
    #         r += 1
    #     else:
    #         res += verticalCut.pop() * r
    #         c += 1
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

    def minimumCost1(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        @lru_cache(None)
        def dfs(r, c):
            if r < m and c < n:
                return min(dfs(r + 1, c) + horizontalCut[-r] * c, dfs(r, c + 1) + verticalCut[-c] * r)
            if r < m:
                return dfs(r + 1, c) + horizontalCut[-r] * c
            if c < n:
                return dfs(r, c + 1) + verticalCut[-c] * r
            return 0
        horizontalCut.sort()
        verticalCut.sort()

        return dfs(1, 1)


def test_minimum_cost():
    solution = Solution()
    assert solution.minimumCost(6, 3, [2, 3, 2, 3, 1], [1, 2]) == 28, 'wrong result'
    assert solution.minimumCost(3, 2, [1, 3], [5]) == 13, 'wrong result'
    assert solution.minimumCost(2, 2, [7], [4]) == 15, 'wrong result'


if __name__ == '__main__':
    test_minimum_cost()
