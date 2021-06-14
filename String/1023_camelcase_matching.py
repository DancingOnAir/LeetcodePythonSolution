from typing import List
from collections import Counter


class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        res = [-1] * len(queries)

        cnt = Counter(pattern)
        for i, q in enumerate(queries):
            cur = Counter(q)
            diff = [x for x in (cur - cnt) if x.isupper()]
            if len(diff) > 0:
                res[i] = False

        for p in pattern:
            for i, q in enumerate(queries):
                if type(res[i]) == int:
                    idx = q.find(p, 0 if res[i] == -1 else res[i]+1)
                    if idx == -1:
                        res[i] = False
                    else:
                        res[i] = idx
        return [type(x) == int for x in res]


def test_camel_match():
    solution = Solution()

    assert solution.camelMatch(["CompetitiveProgramming", "CounterPick", "ControlPanel"], "CooP") == [False, False, True]
    assert solution.camelMatch(["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"], "FB") \
           == [True, False, True, True, False], 'wrong result'
    assert solution.camelMatch(["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"], "FoBa") \
           == [True, False, True, False, False], 'wrong result'
    assert solution.camelMatch(["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"], "FoBaT") \
           == [False, True, False, False, False], 'wrong result'


if __name__ == '__main__':
    test_camel_match()
