class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        x, y = set(s[i] + s[i+1] for i in range(len(s) - 1)), set(s[i] + s[i-1] for i in range(len(s) - 1, 0, -1))
        return x & y

    def isSubstringPresent1(self, s: str) -> bool:
        m = set()
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                return True

            if s[i] + s[i + 1] in m:
                return True
            m.add(s[i + 1] + s[i])
        return False


def test_is_substring_present():
    solution = Solution()
    assert solution.isSubstringPresent("leetcode"), 'wrong result'
    assert solution.isSubstringPresent("abcba"), 'wrong result'
    assert not solution.isSubstringPresent("abcd"), 'wrong result'


if __name__ == '__main__':
    test_is_substring_present()
