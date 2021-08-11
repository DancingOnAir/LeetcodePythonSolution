from typing import List
from collections import Counter


class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        mod = 10 ** 9 + 7
        n, l1, l2 = len(words), len(target), len(words[0])
        if l1 > l2:
            return 0

        cnt = list(Counter(w[i] for w in words) for i in range(l2))
        dp = [[0] * (l1 + 1) for _ in range(l2 + 1)]
        for i in range(l2):
            dp[i][0] = 1
            for j in range(min(i + 1, l1)):
                dp[i+1][j+1] = (dp[i][j+1] + (dp[i][j] * cnt[i][target[j]]) % mod) % mod

        return dp[l2][l1]


def test_num_ways():
    solution = Solution()

    assert solution.numWays(["acca", "bbbb", "caca"], "aba") == 6, 'wrong result'
    assert solution.numWays(["abba", "baab"], "bab") == 4, "wrong result"
    assert solution.numWays(["abcd"], "abcd") == 1, "wrong result"
    assert solution.numWays(["abab", "baba", "abba", "baab"], "abba") == 16, "wrong result"


if __name__ == '__main__':
    test_num_ways()
