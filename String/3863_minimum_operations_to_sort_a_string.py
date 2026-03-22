from itertools import pairwise


class Solution:
    def minOperations(self, s: str) -> int:
        if all(a <= b for a, b in pairwise(s)):
            return 0

        if len(s) == 2:
            return -1

        mx = max(s)
        mn = min(s)

        if mn == s[0] or mx == s[-1]:
            return 1

        if any(c == mn or c == mx for c in s[1: -1]):
            return 2

        return 3


def test_min_operations():
    solution = Solution()
    assert solution.minOperations("dog") == 1, 'wrong result'
    assert solution.minOperations("card") == 2, 'wrong result'
    assert solution.minOperations("gf") == -1, 'wrong result'


if __name__ == '__main__':
    test_min_operations()
