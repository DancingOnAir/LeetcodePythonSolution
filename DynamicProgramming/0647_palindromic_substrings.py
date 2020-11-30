from typing import List


class Solution:

    # Let N = len(S). There are 2N-1 possible centers for the palindrome:
    # we could have a center at S[0], between S[0] and S[1], at S[1], between S[1] and S[2], at S[2], etc.
    def countSubstrings(self, s: str) -> int:
        res, n = 0, len(s)
        for center in range(2 * n - 1):
            left = center // 2
            right = left + center % 2
            while left >= 0 and right < n and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1

        return res

    def countSubstrings1(self, s: str) -> int:
        res, n = 0, len(s)
        dp = [[0] * n for _ in range(n)]

        for i in range(n)[::-1]:
            for j in range(i, n):
                dp[i][j] = (s[i] == s[j]) and ((j - i + 1) < 3 or dp[i + 1][j - 1])
                res += dp[i][j]
        return res


def test_count_substrings():
    solution = Solution()

    assert solution.countSubstrings('abc') == 3, 'wrong result'
    assert solution.countSubstrings('aaa') == 6, 'wrong result'


if __name__ == '__main__':
    test_count_substrings()
