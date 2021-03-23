class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        n = len(a)
        if n == 1:
            return True

        for i in range(n + 1):
            s1 = a[:i] + b[i:]
            s2 = b[:i] + a[i:]

            if s1 == s1[::-1] or s2 == s2[::-1]:
                return True

        return False


def test_check_palindrome_formation():
    solution = Solution()
    assert solution.checkPalindromeFormation('x', 'y'), 'wrong result'
    assert solution.checkPalindromeFormation('abdef', 'fecab'), 'wrong result'
    assert solution.checkPalindromeFormation('ulacfd', 'jizalu'), 'wrong result'
    assert not solution.checkPalindromeFormation('xbdef', 'xecab'), 'wrong result'


if __name__ == '__main__':
    test_check_palindrome_formation()
