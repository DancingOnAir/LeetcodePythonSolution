class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        def helper(s1, s2):
            n = len(s1)
            flag = True
            for i in range(n // 2):
                if flag:
                    if s1[i] != s2[n - 1 - i]:
                        flag = False
                if not flag:
                    if s1[i] != s1[n - 1 - i]:
                        return False
            return True

        if helper(a, b) or helper(b, a):
            return True

        ra, rb = a[::-1], b[::-1]
        if helper(ra, rb) or helper(rb, ra):
            return True

        return False

    # 相遇问题
    def checkPalindromeFormation1(self, a: str, b: str) -> bool:
        n = len(a)
        if n == 1:
            return True

        i, j = 0, n - 1
        while i < j and a[i] == b[j]:
            i += 1
            j -= 1
        s1, s2 = a[i: j + 1], b[i: j + 1]

        i, j = 0, n - 1
        while i < j and b[i] == a[j]:
            i += 1
            j -= 1
        s3, s4 = b[i: j + 1], a[i : j + 1]

        return any(s == s[::-1] for s in (s1, s2, s3, s4))


def test_check_palindrome_formation():
    solution = Solution()
    assert solution.checkPalindromeFormation('x', 'y'), 'wrong result'
    assert solution.checkPalindromeFormation('abdef', 'fecab'), 'wrong result'
    assert solution.checkPalindromeFormation('ulacfd', 'jizalu'), 'wrong result'
    assert not solution.checkPalindromeFormation('xbdef', 'xecab'), 'wrong result'


if __name__ == '__main__':
    test_check_palindrome_formation()
