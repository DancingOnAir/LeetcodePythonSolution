from typing import List
from collections import Counter


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        res = 0
        memo = set()
        freq = Counter(words)
        flag = 0
        for w in freq:
            if w[0] == w[1]:
                if freq[w] & 1:
                    flag = 1
                res += freq[w] // 2 * 4
                continue

            if w in memo:
                res += min(freq[w], freq[w[::-1]]) * 4
            else:
                memo.add(w[::-1])

        return res + flag * 2


def test_longest_palindrome():
    solution = Solution()
    assert solution.longestPalindrome(["lc", "cl", "gg"]) == 6, 'wrong result'
    assert solution.longestPalindrome(["ab", "ty", "yt", "lc", "cl", "ab"]) == 8, 'wrong result'
    assert solution.longestPalindrome(["cc", "ll", "xx"]) == 2, 'wrong result'


if __name__ == '__main__':
    test_longest_palindrome()

