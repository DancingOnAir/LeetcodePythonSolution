class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        while i < len(s) / 2:
            if s[i] == s[-i - 1]:
                i += 1
        s = s[i: len(s) - i]
        return s[1:] == s[1:][::-1] or s[:-1] == s[:-1][::-1]

    def validPalindrome1(self, s: str) -> bool:
        def helper(x):
            return x == x[::-1]

        i, j = 0, len(s) - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                if helper(s[i: j]) or helper(s[i+1: j+1]):
                    return True
                return False
        return True


def test_valid_palindrome():
    solution = Solution()
    assert solution.validPalindrome("aba"), 'wrong result'
    assert solution.validPalindrome("abca"), 'wrong result'
    assert not solution.validPalindrome("abc"), 'wrong result'


if __name__ == '__main__':
    test_valid_palindrome()
