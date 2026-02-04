class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        j = cnt = 0
        for i in range(1, len(s)):
            cnt += (s[i] == s[i - 1])

            if cnt > 1:
                j += 1
                cnt -= (s[j] == s[j - 1])
        return len(s) - j

    def longestSemiRepetitiveSubstring1(self, s: str) -> int:
        res = 0
        cnt = 0
        pre = ''
        left, pos = 0, 0

        for right in range(len(s)):
            if s[right] == pre:
                if cnt == 0:
                    pos = right - 1
                cnt += 1

            if cnt > 1:
                left = pos + 1
                pos = right - 1
                cnt -= 1

            res = max(res, right - left + 1)
            pre = s[right]
        return res


def test_longest_semi_repetitive_substring():
    solution = Solution()
    assert solution.longestSemiRepetitiveSubstring("52233") == 4, 'wrong result'
    assert solution.longestSemiRepetitiveSubstring("5494") == 4, 'wrong result'
    assert solution.longestSemiRepetitiveSubstring("1111111") == 2, 'wrong result'


if __name__ == '__main__':
    test_longest_semi_repetitive_substring()
