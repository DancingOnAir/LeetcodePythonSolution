class Solution:
    def longestPrefix(self, s: str) -> str:
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
