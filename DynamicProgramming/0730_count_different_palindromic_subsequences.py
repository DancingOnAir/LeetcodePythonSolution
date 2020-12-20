class Solution:
    def countPalindromicSubsequences(self, S: str) -> int:
        n = len(S)
        if n < 2:
            return n

        def getPalindromicSubsequences(s: str):
            pass

        dp = [0] * (n + 1)
        memo = list()
        for i in range(n):
            for j in range(i+1)[::-1]:
                if S[j] == S[i] and getPalindromicSubsequences(S[j:i+1]) not in memo:
                    dp[i + 1] += dp[j] + 1
                    memo.append()
                else:
                    dp[i + 1]
            #     for k in range():
            #         dp[i+1] =
        return


def test_count_palindromic_subsequences():
    solution = Solution()

    assert solution.countPalindromicSubsequences('bccb') == 6, 'wrong result'
    assert solution.countPalindromicSubsequences('abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba') \
           == 104860361, 'wrong result'


if __name__ == '__main__':
    test_count_palindromic_subsequences()

