class Solution:
    # https://leetcode.com/problems/longest-happy-prefix/discuss/547187/Python-Deterministic-Finite-Automaton-inspired-by-KMP
    # kmp
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return ''
        cnt = [0] * n
        d = 0
        for i in range(1, n):
            while d and s[d] != s[i]:
                d = cnt[d - 1]
            d += (s[d] == s[i])
            cnt[i] = d
        return s[:cnt[n - 1]]

    # incremental hash
    def longestPrefix2(self, s: str) -> str:
        res, l, r, mod = 0, 0, 0, 10 ** 9 + 7
        for i in range(len(s) - 1):
            l = (l * 128 + ord(s[i])) % mod
            # Specifically, we get the ith letter from the end using s[~i], note ~i is -i-1
            r = (r + pow(128, i, mod) * ord(s[~i])) % mod
            #  for the collisions, we can easily check if prefix is equal to the suffix.
            if l == r:
                res = i + 1
        return s[: res]

    # brute force
    def longestPrefix1(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return ""

        pos = 1
        while pos >= 0:
            if s.startswith(s[pos:]):
                return s[pos:]
            pos += 1

        return ""


def test_longest_prefix():
    solution = Solution()
    assert solution.longestPrefix('level') == 'l', 'wrong result'
    assert solution.longestPrefix('ababab') == 'abab', 'wrong result'
    assert solution.longestPrefix('leetcodeleet') == 'leet', 'wrong result'
    assert solution.longestPrefix('a') == '', 'wrong result'


if __name__ == '__main__':
    test_longest_prefix()
