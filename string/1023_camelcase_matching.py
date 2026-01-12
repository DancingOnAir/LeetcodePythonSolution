from typing import List
from collections import Counter


class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def u(s):
            return [c for c in s if c.isupper()]

        def issup(s, t):
            it = iter(t)
            return all(c in it for c in s)
            # for c in s:
            #     if c in t:
            #         t = t[t.index(c)+1:]
            #     else:
            #         return False
            # return True

        return [u(pattern) == u(q) and issup(pattern, q) for q in queries]

    def camelMatch1(self, queries: List[str], pattern: str) -> List[bool]:
        res = [-1] * len(queries)

        def u(s):
            return [c for c in s if c.isupper()]
        cnt = u(pattern)
        for i, q in enumerate(queries):
            if cnt != u(q):
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
