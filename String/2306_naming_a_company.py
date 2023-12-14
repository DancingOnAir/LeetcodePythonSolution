from typing import List
from collections import defaultdict


class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        m = defaultdict(set)
        for w in ideas:
            m[w[0]].add(w[1:])

        res = 0
        for a, set_a in m.items():
            for b, set_b in m.items():
                if a >= b:
                    continue

                union = len(set_a & set_b)
                res += (len(set_a) - union) * (len(set_b) - union)
        return res * 2


def test_distinct_names():
    solution = Solution()
    assert solution.distinctNames(["bzklqtbdr","kaqvdlp","r","dk"]) == 12, 'wrong result'
    assert solution.distinctNames(["aaa","baa","caa","bbb","cbb","dbb"]) == 2, 'wrong result'
    assert solution.distinctNames(["coffee", "donuts", "time", "toffee"]) == 6, 'wrong result'
    assert solution.distinctNames(["lack", "back"]) == 0, 'wrong result'


if __name__ == '__main__':
    test_distinct_names()
