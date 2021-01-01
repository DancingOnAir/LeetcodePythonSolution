from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        dp = [-1] * K
        memo = list()
        for f in flights:
            if src == f[0] and dst == f[1]:
                dp[0] = f[2]
                memo.append([f[0], f[1]])
        if not K:
            return dp[0]

        for k in range(1, K+1):
            for i in range(n):
                if i not in memo[-1]


def test_find_cheapest_price():
    solution = Solution()

    n1 = 3
    edges1 = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src1 = 0
    dst1 = 2
    k1 = 1
    assert solution.findCheapestPrice(n1, edges1, src1, dst1, k1) == 200, 'wrong result'

    n2 = 3
    edges2 = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src2 = 0
    dst2 = 2
    k2 = 0
    assert solution.findCheapestPrice(n2, edges2, src2, dst2, k2) == 500, 'wrong result'


if __name__ == '__main__':
    test_find_cheapest_price()
