from typing import List
from collections import Counter


class Solution:
    # straight forward with HashMap
    def longestPalindrome(self, words: List[str]) -> int:
        freq = Counter()
        center = res = 0

        for w in words:
            if w[0] == w[1]:
                if freq[w] > 0:
                    center -= 1
                    freq[w] -= 1
                    res += 4
                else:
                    center += 1
                    freq[w] += 1
            else:
                if freq[w[::-1]] > 0:
                    res += 4
                    freq[w[::-1]] -= 1
                else:
                    freq[w] += 1

        if center > 0:
            res += 2
        return res

    # Counter, remove set
    def longestPalindrome1(self, words: List[str]) -> int:
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

