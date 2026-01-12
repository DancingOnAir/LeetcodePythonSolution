class Solution:
    def checkString(self, s: str) -> bool:
        for i, ch in enumerate(s):
            if i > 0 and s[i - 1] == 'b' and ch == 'a':
                return False
        return True

    def checkString1(self, s: str) -> bool:
        return 'ba' not in s


def test_check_string():
    solution = Solution()
    assert solution.checkString('aaabbb'), 'wrong result'
    assert not solution.checkString('abab'), 'wrong result'
    assert solution.checkString('bbb'), 'wrong result'


if __name__ == '__main__':
    test_check_string()
