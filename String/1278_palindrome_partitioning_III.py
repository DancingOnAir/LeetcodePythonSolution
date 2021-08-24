class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        def changes_make_palindrome(ss):
            changes = 0
            i, j = 0, len(ss) - 1
            while i < j:
                if ss[i] != ss[j]:
                    changes += 1
                i += 1
                j -= 1
            return changes

        n = len(s)
        if n == k:
            return 0

        memo = dict()
        for i in range(n):
            for j in range(i+1, n+1):
                ss = s[i: j]

                if ss not in memo:
                    memo[ss] = changes_make_palindrome(ss)
        print(memo)

        # dp[pos][k]
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(1, min(k, n - i) + 1):
                if j == 1:
                    continue

                dp[i][j] = min(dp[i])
        return dp[0][k]


def test_palindrome_partition():
    solution = Solution()
    assert solution.palindromePartition("abc", 2) == 1, 'wrong result'
    assert solution.palindromePartition("aabbc", 3) == 0, 'wrong result'
    assert solution.palindromePartition("leetcode", 8) == 0, 'wrong result'


if __name__ == '__main__':
    test_palindrome_partition()
