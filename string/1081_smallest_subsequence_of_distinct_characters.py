class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last = {c: i for i, c in enumerate(s)}
        stk = list()
        for i, c in enumerate(s):
            if c in stk:
                continue
            while stk and stk[-1] > c and last[stk[-1]] > i:
                stk.pop()
            stk.append(c)

        return ''.join(stk)
        # dp思路不对，很可能新添加的字符会对前面不止一个字符造成影响。
        # n = len(s)
        # if n < 2:
        #     return n
        #
        # dp = [''] * (n + 1)
        # for i in range(1, n+1):
        #     c = s[i - 1]
        #     if c in dp[i - 1]:
        #         j = dp[i - 1].index(c)
        #         if dp[i - 1][j:] > dp[i - 1][j+1:] + c:
        #             dp[i] = dp[i - 1][: j] + dp[i - 1][j + 1:] + c
        #         else:
        #             dp[i] = dp[i - 1]
        #     else:
        #         dp[i] = dp[i - 1] + c
        # return dp[n]


def test_smallest_subsequence():
    solution = Solution()
    assert solution.smallestSubsequence('bcabc') == 'abc', 'wrong result'
    assert solution.smallestSubsequence('cbacdcbc') == 'acdb', 'wrong result'


if __name__ == '__main__':
    test_smallest_subsequence()

