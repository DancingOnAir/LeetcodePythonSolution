from typing import List


class Solution:
    # 0-1背包问题
    # dp[i] 表示target为i时有多少种组合
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        dp = [1] + [0] * target
        for cnt, mark in types:
            for i in range(target, -1, -1):
                for j in range(1, min(cnt, i // mark) + 1):
                    dp[i] = (dp[i] + dp[i - j * mark]) % mod
        return dp[-1]


def test_ways_to_reach_target():
    solution = Solution()
    assert solution.waysToReachTarget(6, [[6, 1], [3, 2], [2, 3]]) == 7, 'wrong result'
    assert solution.waysToReachTarget(5, [[50, 1], [50, 2], [50, 5]]) == 4, 'wrong result'
    assert solution.waysToReachTarget(18, [[6, 1], [3, 2], [2, 3]]) == 1, 'wrong result'


if __name__ == '__main__':
    test_ways_to_reach_target()
