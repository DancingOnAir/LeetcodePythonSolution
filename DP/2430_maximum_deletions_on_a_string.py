class Solution:
    # dp[i] mean the maximum number of operations to delete, the substring starting at s[i].
    def deleteString(self, s: str) -> int:
        n = len(s)
        if len(set(s)) == 1:
            return n

        lcs = [[0] * (n + 1) for _ in range(n + 1)]
        dp = [1] * n
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    lcs[i][j] = lcs[i + 1][j + 1] + 1
                if lcs[i][j] >= j - i:
                    dp[i] = max(dp[i], dp[j] + 1)
        return dp[0]


def test_delete_string():
    solution = Solution()
    assert solution.deleteString("abcabcdabc") == 2, 'wrong result'
    assert solution.deleteString("aaabaab") == 4, 'wrong result'
    assert solution.deleteString("aaaaa") == 5, 'wrong result'


if __name__ == '__main__':
    test_delete_string()
