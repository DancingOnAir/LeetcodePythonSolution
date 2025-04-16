class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        return False


def test_is_strictly_palindromic():
    solution = Solution()
    assert not solution.isStrictlyPalindromic(9), 'wrong result'
    assert not solution.isStrictlyPalindromic(4), 'wrong result'


if __name__ == '__main__':
    test_is_strictly_palindromic()
