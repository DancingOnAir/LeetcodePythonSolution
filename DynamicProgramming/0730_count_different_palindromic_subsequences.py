class Solution:
    # https://leetcode.com/problems/count-different-palindromic-subsequences/discuss/109507/Java-96ms-DP-Solution-with-Detailed-Explanation
    def countPalindromicSubsequences(self, S: str) -> int:
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

