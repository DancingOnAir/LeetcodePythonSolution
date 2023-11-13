class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        res = 1
        left = 0
        for right in range(1, len(s)):
            if ord(s[right]) != ord(s[right - 1]) + 1:
                left = right
            else:
                res = max(res, right - left + 1)
        return res


def test_longest_continuous_substring():
    solution = Solution()
    # assert solution.longestContinuousSubstring("abacaba") == 2, 'wrong result'
    assert solution.longestContinuousSubstring("abcde") == 5, 'wrong result'


if __name__ == '__main__':
    test_longest_continuous_substring()
