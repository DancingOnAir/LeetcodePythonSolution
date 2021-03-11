class Solution:
    # recursive
    def checkPartitioning(self, s: str) -> bool:
        def helper(sub_s, k):
            if k == 1:
                return sub_s == sub_s[::-1]

            for i in range(1, len(s) - 1):
                if sub_s[:i] == sub_s[:i][::-1] and helper(sub_s[i:], k - 1):
                    return True

        return helper(s, 3)

    # dp
    def checkPartitioning2(self, s: str) -> bool:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                l = j - i + 1
                if l == 1:
                    dp[i][j] = True
                elif l == 2:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (s[i] == s[j]) and dp[i + 1][j - 1]

        for i in range(n):
            for j in range(i + 2, n):
                left, mid, right = dp[0][i], dp[i + 1][j - 1], dp[j][n - 1]
                if left and mid and right:
                    return True
        return False

    # brute force solution
    def checkPartitioning1(self, s: str) -> bool:
        n = len(s)
        # split string s into 3 parts: s[:left], s[left, right], s[:right]
        for i in range(1, n - 1):
            if s[:i] == s[:i][::-1]:
                for j in range(i + 1, n):
                    if s[i:j] == s[i:j][::-1] and s[j:] == s[j:][::-1]:
                        return True
        return False


def test_check_partitioning():
    solution = Solution()
    assert solution.checkPartitioning('abcbdd'), 'wrong result'
    assert not solution.checkPartitioning('bcbddxy'), 'wrong result'
    assert solution.checkPartitioning('bbab'), 'wrong result'


if __name__ == '__main__':
    test_check_partitioning()
