from typing import List
from itertools import product


class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        s = s[1: -1]
        n = len(s)
        res = []
        path = []

        def helper(ss):
            if not ss or (len(ss) > 1 and ss[0] == ss[-1] == '0'):
                return []
            if ss[-1] == '0':
                return [ss]
            if ss[0] == '0':
                return [ss[0] + "." + ss[1:]]

            return [ss] + [ss[:i] + '.' + ss[i:] for i in range(1, len(ss))]

        for i in range(n):
            for a, b in product(helper(s[:i]), helper(s[i:])):
                res.append("(%s, %s)" % (a, b))

        return res


def test_ambiguous_coordinates():
    solution = Solution()
    assert solution.ambiguousCoordinates("(123)") == ["(1, 2.3)", "(1, 23)", "(1.2, 3)", "(12, 3)"], 'wrong result'
    assert solution.ambiguousCoordinates("(0123)") == ["(0, 1.23)", "(0, 12.3)", "(0, 123)", "(0.1, 2.3)", "(0.1, 23)",
                                                       "(0.12, 3)"], 'wrong result'
    assert solution.ambiguousCoordinates("(00011)") == ["(0, 0.011)", "(0.001, 1)"], 'wrong result'


if __name__ == '__main__':
    test_ambiguous_coordinates()
