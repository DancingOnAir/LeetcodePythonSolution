class Solution:
    # nxt前缀表不减1的实现
    def longestPrefix(self, s: str) -> str:
        j = 0
        nxt = [0] * len(s)

        for i in range(1, len(s)):
            while j > 0 and s[i] != s[j]:
                j = nxt[j - 1]
            if s[i] == s[j]:
                j += 1
            nxt[i] = j
        return s[:nxt[-1]]

    def longestPrefix1(self, s: str) -> str:
        s += ' '
        n = len(s)
        nxt = [-1] * n
        i, j = 0, -1
        while i < n - 1:
            if j == -1 or s[i] == s[j]:
                i += 1
                j += 1
                if s[i] == s[j]:
                    nxt[i] = nxt[j]
                else:
                    nxt[i] = j
            else:
                j = nxt[j]

        return s[:nxt[-1]]


def test_longest_prefix():
    solution = Solution()
    assert solution.longestPrefix("abc") == "", 'wrong result'
    assert solution.longestPrefix("level") == "l", 'wrong result'
    assert solution.longestPrefix("ababab") == "abab", 'wrong result'


if __name__ == '__main__':
    test_longest_prefix()
