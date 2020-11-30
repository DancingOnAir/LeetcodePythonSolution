from typing import List


class Solution:
    # def isPalindrom(self, left, right, s):
    #     while left < right:
    #         if s[left] != s[right]:
    #             return False
    #         left += 1
    #         right -= 1
    #
    #     return True

    def countSubstrings(self, s: str) -> int:
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
