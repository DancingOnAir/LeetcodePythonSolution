from typing import List


class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        m = dict(zip(chars, vals))
        res = cur = 0
        for ch in s:
            cur = max(cur + m.get(ch, ord(ch) - 96), 0)
            res = max(res, cur)
        return res

    def maximumCostSubstring1(self, s: str, chars: str, vals: List[int]) -> int:
        m = {chars[i]: vals[i] for i in range(len(chars))}
        res = cur = 0
        for i, ch in enumerate(s):
            if ch in m:
                cur += m[ch]
            else:
                cur += ord(ch) - 96
            if cur < 0:
                cur = 0
            res = max(res, cur)
        return res


def test_maximum_cost_substring():
    solution = Solution()
    assert solution.maximumCostSubstring("adaa", "d", [-1000]) == 2, 'wrong result'
    assert solution.maximumCostSubstring("abc", "abc", [-1, -1, -1]) == 0, 'wrong result'


if __name__ == '__main__':
    test_maximum_cost_substring()
