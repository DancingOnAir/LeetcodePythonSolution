from collections import Counter


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = left = 0
        c = Counter()
        for right, ch in enumerate(s):
            while c[ch] > 0:
                c[s[left]] -= 1
                left += 1

            c[ch] += 1
            res = max(res, right - left + 1)
        return res


def test_length_of_longest_substring():
    solution = Solution()
    assert solution.lengthOfLongestSubstring("abcabcbb") == 3, 'wrong result'
    assert solution.lengthOfLongestSubstring("bbbbb") == 1, 'wrong result'
    assert solution.lengthOfLongestSubstring("pwwkew") == 3, 'wrong result'


if __name__ == '__main__':
    test_length_of_longest_substring()
