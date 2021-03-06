class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ''
        res = ''
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if all(k.swapcase() in s[i:j] for k in s[i:j]):
                    res = max(res, s[i:j], key=len)
        return res

    # brute force
    def longestNiceSubstring1(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return ''

        res = ''
        flag = False
        for j in range(1, n+1):
            for i in range(j):
                for c in s[i:j]:
                    if (c.islower() and c.upper() not in s[i:j]) or (c.isupper() and c.lower() not in s[i:j]):
                        flag = False
                        break
                    flag = True

                if flag and len(s[i:j]) > len(res):
                    res = s[i:j]
        return res


def test_longest_nice_substring():
    solution = Solution()
    assert solution.longestNiceSubstring('YazaAay') == 'aAa', 'wrong result'
    assert solution.longestNiceSubstring('Bb') == 'Bb', 'wrong result'
    assert solution.longestNiceSubstring('c') == '', 'wrong result'
    assert solution.longestNiceSubstring('dDzeE') == 'dD', 'wrong result'


if __name__ == '__main__':
    test_longest_nice_substring()
