class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        left, right = 0, len(s) - 1
        s = list(s)
        while left < right:
            if s[left] != s[right]:
                if s[left] < s[right]:
                    s[right] = s[left]
                else:
                    s[left] = s[right]

            left += 1
            right -=1

        return ''.join(s)


def test_make_smallest_palindrome():
    solution = Solution()
    assert solution.makeSmallestPalindrome("egcfe") == "efcfe", 'wrong result'
    assert solution.makeSmallestPalindrome("abcd") == "abba", 'wrong result'
    assert solution.makeSmallestPalindrome("seven") == "neven", 'wrong result'


if __name__ == '__main__':
    test_make_smallest_palindrome()
