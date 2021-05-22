from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        return sum(dict(Counter(s) - Counter(t)).values())


def test_min_steps():
    solution = Solution()
    assert solution.minSteps('bab', 'aba') == 1, 'wrong result'
    assert solution.minSteps('leetcode', 'practice') == 5, 'wrong result'
    assert solution.minSteps('anagram', 'mangaar') == 0, 'wrong result'
    assert solution.minSteps('xxyyzz', 'xxyyzz') == 0, 'wrong result'
    assert solution.minSteps('friend', 'family') == 4, 'wrong result'


if __name__ == '__main__':
    test_min_steps()
