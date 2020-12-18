from typing import List
from collections import Counter


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        l1, l2 = len(s1), len(s2)

        dp = [[0] * (l1 + 1) for _ in range(l2 + 1)]

        common_str = ''
        for i in range(l1):
            for j in range(l2):
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
                if s1[i] == s2[j] and dp[i][j] + 1 >= dp[i + 1][j + 1]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                    if common_str and common_str[-1] < s1[i]:
                        common_str.
                        common_str[-1] = s1[i]
                    else:
                        common_str += s1[i]
        print(common_str)
        res = 0
        for i, val in enumerate(s1):
            if val not in common_str:
                res += ord(val)

        for i, val in enumerate(s2):
            if val not in common_str:
                res += ord(val)

        return res


def test_minimum_delete_sum():
    solution = Solution()

    assert solution.minimumDeleteSum(s1="sea", s2="eat") == 231, 'wrong result'
    assert solution.minimumDeleteSum(s1="delete", s2="leet") == 403, 'wrong result'


if __name__ == '__main__':
    test_minimum_delete_sum()
