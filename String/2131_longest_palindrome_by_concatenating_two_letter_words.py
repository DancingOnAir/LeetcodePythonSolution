from typing import List
from collections import Counter


class Solution:
    def longestPalindrome1(self, words: List[str]) -> int:
        freq = Counter()
        pairs = 0
        pass

    # set
    def longestPalindrome(self, words: List[str]) -> int:
        center = aa = abba = 0
        freq = Counter(words)

        for w, c in freq.items():
            if w[0] == w[1]:
                aa += c // 2 * 2
                if c % 2 == 1:
                    center = 2
            else:
                abba += min(freq[w], freq[w[::-1]])

        return center + aa * 2 + abba * 2


def test_longest_palindrome():
    solution = Solution()
    assert solution.longestPalindrome(["lc", "cl", "gg"]) == 6, 'wrong result'
    assert solution.longestPalindrome(["ab", "ty", "yt", "lc", "cl", "ab"]) == 8, 'wrong result'
    assert solution.longestPalindrome(["cc", "ll", "xx"]) == 2, 'wrong result'


if __name__ == '__main__':
    test_longest_palindrome()

