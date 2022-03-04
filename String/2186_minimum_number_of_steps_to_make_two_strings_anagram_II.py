from collections import Counter, defaultdict


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        m = defaultdict(int)
        for ch in s:
            m[ch] += 1
        for ch in t:
            m[ch] -= 1
        return sum(abs(x) for x in m.values())

    # collections.counter
    def minSteps1(self, s: str, t: str) -> int:
        return sum((Counter(s) - Counter(t)).values()) + sum((Counter(t) - Counter(s)).values())


def test_min_steps():
    solution = Solution()
    assert solution.minSteps('leetcode', 'coats') == 7, 'wrong result'
    assert solution.minSteps('night', 'thing') == 0, 'wrong result'


if __name__ == '__main__':
    test_min_steps()
