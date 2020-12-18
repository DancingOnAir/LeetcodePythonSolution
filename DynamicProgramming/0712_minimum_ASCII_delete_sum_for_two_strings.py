from typing import List
from collections import Counter


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        l1, l2 = len(s1), len(s2)
        dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]

        for i in range(l1):
            for j in range(l2):
                if s1[i] == s2[j]:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
                else:
                    dp[i + 1][j + 1] = dp[i][j] + ord(s1[i])

        res = sum(map(ord, s1 + s2)) - dp[l1][l2] * 2
        return res


def test_minimum_delete_sum():
    solution = Solution()

    assert solution.minimumDeleteSum(s1="sea", s2="eat") == 231, 'wrong result'
    assert solution.minimumDeleteSum(s1="delete", s2="leet") == 403, 'wrong result'


if __name__ == '__main__':
    test_minimum_delete_sum()
