from functools import lru_cache


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        @lru_cache(None)
        def helper(ss):
            stk = list()
            for c in ss:
                if c == '#':
                    if stk:
                        stk.pop()
                else:
                    stk.append(c)
            return ''.join(stk)

        return helper(s) == helper(t)


def test_backspace_compare():
    solution = Solution()
    assert solution.backspaceCompare("y#fo##f", "y#f#o##f"), 'wrong result'
    assert solution.backspaceCompare("ab#c", "ad#c"), 'wrong result'
    assert solution.backspaceCompare("ab##", "c#d#"), 'wrong result'
    assert not solution.backspaceCompare("a#c", "b"), 'wrong result'


if __name__ == '__main__':
    test_backspace_compare()
