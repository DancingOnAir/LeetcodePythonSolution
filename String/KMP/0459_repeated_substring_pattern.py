class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        j = 0
        nxt = [0] * len(s)
        for i in range(1, len(s)):
            while j > 0 and s[i] != s[j]:
                j = nxt[j - 1]
            if s[i] == s[j]:
                j += 1
            nxt[i] = j

        return nxt[-1] > 0 and (len(s) % (len(s) - nxt[-1])) == 0


def test_repeated_substring_pattern():
    solution = Solution()
    assert not solution.repeatedSubstringPattern("abac"), 'wrong result'
    assert solution.repeatedSubstringPattern("abab"), 'wrong result'
    assert not solution.repeatedSubstringPattern("aba"), 'wrong result'
    assert solution.repeatedSubstringPattern("abcabcabcabc"), 'wrong result'


if __name__ == '__main__':
    test_repeated_substring_pattern()
