class Solution:
    # equivalent to get max length of the palindrome subsequence
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[0] * (n + 1) for _ in range(n)]

        for l in range(1, n+1):
            for i in range(n - l + 1):
                if l == 1:
                    dp[i][l] = 1
                else:
                    p = s.find(s[i + l - 1], i, i + l - 1)
                    if p == -1:
                        dp[i][l] = dp[i][l - 1]
                    else:
                        dp[i][l] = max(dp[i][l - 1], dp[p + 1][l + i - p - 2] + 2)
        return n - dp[0][n]


def test_min_insertions():
    solution = Solution()
    assert solution.minInsertions('zzazz') == 0, 'wrong result'
    assert solution.minInsertions('mbadm') == 2, 'wrong result'
    assert solution.minInsertions('leetcode') == 5, 'wrong result'


if __name__ == '__main__':
    test_min_insertions()
