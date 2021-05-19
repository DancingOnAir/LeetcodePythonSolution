class Solution:
    def longestPrefix(self, s: str) -> str:
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
