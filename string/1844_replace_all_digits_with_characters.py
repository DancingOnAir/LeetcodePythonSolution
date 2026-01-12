class Solution:
    def replaceDigits(self, s: str) -> str:
        return ''.join([chr(ord(s[i - 1]) + int(c)) if i & 1 else c for i, c in enumerate(s)])


def test_replace_digits():
    solution = Solution()
    assert solution.replaceDigits('a1c1e1') == 'abcdef', 'wrong result'
    assert solution.replaceDigits('a1b2c3d4e') == 'abbdcfdhe', 'wrong result'
    assert solution.replaceDigits('a1c1e') == 'abcde', 'wrong result'


if __name__ == '__main__':
    test_replace_digits()
