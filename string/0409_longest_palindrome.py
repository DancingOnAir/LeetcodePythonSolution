from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        odds = sum(1 for _, v in Counter(s).items() if v & 1)
        return len(s) - odds + (odds > 0)


def test_longest_palindrome():
    solution = Solution()

    assert solution.longestPalindrome("abccccdd") == 7, 'wrong result'
    assert solution.longestPalindrome("a") == 1, 'wrong result'
    assert solution.longestPalindrome("bb") == 2, 'wrong result'


if __name__ == '__main__':
    test_longest_palindrome()
