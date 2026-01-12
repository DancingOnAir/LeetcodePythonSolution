class Solution:
    def repeatedCharacter(self, s: str) -> str:
        m = set()
        for c in s:
            if c in m:
                return c
            m.add(c)
        return ''

    def repeatedCharacter1(self, s: str) -> str:
        m = [0] * 26
        for i, c in enumerate(s):
            if m[ord(c) - 97] == 1:
                return c
            m[ord(c) - 97] = 1
        return ''


def test_repeated_character():
    solution = Solution()
    assert solution.repeatedCharacter("abccbaacz") == "c", 'wrong result'
    assert solution.repeatedCharacter("abcdd") == "d", 'wrong result'


if __name__ == '__main__':
    test_repeated_character()
