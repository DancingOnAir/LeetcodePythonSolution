from collections import Counter


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        res = l = 0
        cnt = Counter()
        for r, c in enumerate(s):
            cnt[c] += 1
            while cnt[c] > 2:
                cnt[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res


def test_maximum_length_substring():
    solution = Solution()
    assert solution.maximumLengthSubstring("bcbbbcba") == 4, 'wrong result'
    assert solution.maximumLengthSubstring("aaaa") == 2, 'wrong result'


if __name__ == '__main__':
    test_maximum_length_substring()
