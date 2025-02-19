from collections import Counter


class Solution:
    def maxDifference(self, s: str) -> int:
        mx, mi = 0, len(s)
        for val in Counter(s).values():
            if val & 1:
                mx = max(mx, val)
            else:
                mi = min(mi, val)
        return mx - mi


def test_max_difference():
    solution = Solution()
    assert solution.maxDifference("aaaaabbc") == 3, 'wrong result'
    assert solution.maxDifference("abcabcab") == 1, 'wrong result'


if __name__ == '__main__':
    test_max_difference()
