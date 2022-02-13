class Solution:
    def checkString(self, s: str) -> bool:
        return 'ba' not in s


def test_check_string():
    solution = Solution()
    assert solution.checkString('aaabbb'), 'wrong result'
    assert not solution.checkString('abab'), 'wrong result'
    assert solution.checkString('bbb'), 'wrong result'


if __name__ == '__main__':
    test_check_string()
