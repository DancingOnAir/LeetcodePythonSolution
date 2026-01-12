from typing import List


class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        n = len(word)
        forbidden = set(forbidden)
        res = left = 0

        for right in range(n):
            for i in range(right, max(right - 10, left - 1), -1):
                if word[i: right + 1] in forbidden:
                    left = i + 1
                    break
            res = max(res, right - left + 1)
        return res

    # TLE
    def longestValidSubstring1(self, word: str, forbidden: List[str]) -> int:
        n = len(word)
        for l in range(n, 0, -1):
            for i in range(n - l + 1):
                if all(w not in word[i: i + l] for w in forbidden):
                    return l
        return 0


def test_longest_valid_substring():
    solution = Solution()
    assert solution.longestValidSubstring("cbaaaabc", ["aaa", "cb"]) == 4, 'wrong result'
    assert solution.longestValidSubstring("leetcode", ["de", "le", "e"]) == 4, 'wrong result'


if __name__ == '__main__':
    test_longest_valid_substring()
