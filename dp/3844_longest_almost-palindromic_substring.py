from collections import defaultdict


class Solution:
    def almostPalindromic(self, s: str) -> int:
        n = len(s)
        res = 0

        def helper(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            nonlocal res
            # s[l + 1: r - 1]是回文
            res = max(res, r - l - 1)

        for i in range(2 * n - 1):
            l, r = i // 2, (i + 1) // 2
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            helper(l - 1, r)
            helper(l, r + 1)
            if res >= n:
                return res
        return res


def test_almost_palindromic():
    solution = Solution()
    assert solution.almostPalindromic("abca") == 4, 'wrong result'
    assert solution.almostPalindromic("abba") == 4, 'wrong result'
    assert solution.almostPalindromic("zzabba") == 5, 'wrong result'


if __name__ == '__main__':
    test_almost_palindromic()
