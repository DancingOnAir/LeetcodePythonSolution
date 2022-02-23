class Solution:
    # Step1.
    # Initialize dp[n+1][n+1],
    # where dp[i][j] means the length of the longest common sequence between
    # i first letters in s1 and j first letters in s2.
    #
    # Step2.
    # Find the longest common sequence between s1 and s2,
    # where s1 = s and s2 = reversed(s)
    #
    # Step3.
    # return n - dp[n][n]
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(n):
                # s[n - j - 1] = s[-j - 1] = s[~j]
                dp[i + 1][j + 1] = dp[i][j] + 1 if s[i] == s[~j] else max(dp[i][j + 1], dp[i + 1][j])
        return n - dp[n][n]


    # initialize dp[n+1][n+1],
    # where dp[i][j] means the length of the longest palindrome sequence between
    # i start letter in s and j length of substring.
    def minInsertions1(self, s: str) -> int:
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
