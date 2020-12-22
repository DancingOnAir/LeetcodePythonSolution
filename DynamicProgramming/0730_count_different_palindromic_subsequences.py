class Solution:
    def countPalindromicSubsequences(self, S: str) -> int:
        n = len(S)
        MOD = 10 ** 9 + 7
        dp = [[[0] * n for _ in range(n)] for _ in range(4)]

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                for k in range(4):
                    c = chr(ord('a') + k)
                    if i == j:
                        if S[i] == c:
                            dp[k][i][j] = 1
                        else:
                            dp[k][i][j] = 0
                    else:
                        if S[i] != c:
                            dp[k][i][j] = dp[k][i+1][j]
                        elif S[j] != c:
                            dp[k][i][j] = dp[k][i][j-1]
                        else:
                            if j == i + 1:
                                dp[k][i][j] = 2
                            else:
                                dp[k][i][j] = 2
                                for m in range(4):
                                    dp[k][i][j] += dp[m][i+1][j-1]
                                    dp[k][i][j] %= MOD
        res = 0
        for k in range(4):
            res += dp[k][0][n-1]
            res %= MOD
        return res

    # https://leetcode.com/problems/count-different-palindromic-subsequences/discuss/109507/Java-96ms-DP-Solution-with-Detailed-Explanation
    def countPalindromicSubsequences1(self, S: str) -> int:
        n = len(S)
        if n < 2:
            return n

        dp = [[1 if i == j else 0 for i in range(n)] for j in range(n)]

        for distance in range(1, n):
            for i in range(n - distance):
                j = i + distance

                if S[i] != S[j]:
                    dp[i][j] = dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]
                else:
                    left, right = i + 1, j - 1
                    while left <= right and S[left] != S[i]:
                        left += 1
                    while left <= right and S[right] != S[j]:
                        right -= 1

                    dp[i][j] = 2 * dp[i + 1][j - 1]
                    if left == right:
                        dp[i][j] += 1
                    elif left > right:
                        dp[i][j] += 2
                    else:
                        dp[i][j] -= dp[left + 1][right - 1]

        return dp[0][n - 1] % (10 ** 9 + 7)


def test_count_palindromic_subsequences():
    solution = Solution()

    assert solution.countPalindromicSubsequences('bccb') == 6, 'wrong result'
    assert solution.countPalindromicSubsequences('abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba') \
           == 104860361, 'wrong result'


if __name__ == '__main__':
    test_count_palindromic_subsequences()

