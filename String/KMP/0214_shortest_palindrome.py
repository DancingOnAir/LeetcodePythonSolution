class Solution:
    # acab  abaa    aaacecaa
    # baca  aaba    aacecaaa
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        nxt = [0] * n
        j = 0
        for i in range(1, n):
            while j > 0 and s[i] != s[j]:
                j = nxt[j - 1]
            if s[i] == s[j]:
                j += 1
            nxt[i] = j

        j = 0
        for i in range(n - 1, -1, -1):
            while j > 0 and s[i] != s[j]:
                j = nxt[j - 1]
            if s[i] == s[j]:
                j += 1

        res = s[j:]
        if len(res) == n:
            return ''
        return res[::-1] + s


def test_shortest_palindrome():
    solution = Solution()
    assert solution.shortestPalindrome("aacecaaa") == "aaacecaaa", 'wrong result'
    assert solution.shortestPalindrome("abcd") == "dcbabcd", 'wrong result'


if __name__ == '__main__':
    test_shortest_palindrome()
