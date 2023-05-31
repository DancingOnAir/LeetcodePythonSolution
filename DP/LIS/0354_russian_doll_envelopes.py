from typing import List
from bisect import bisect_left


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        def LIS(arr):
            g = list()
            for x in arr:
                j = bisect_left(g, x)
                if j == len(g):
                    g.append(x)
                else:
                    g[j] = x
            return len(g)
        # 注意这里排序，优先比较w，当w1==w2时，h较大的排前面，这样的话h1, h2自然就是反序的，在对h求LIS时只能取其一
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        return LIS([h for _, h in envelopes])


def test_max_envelopes():
    solution = Solution()
    assert solution.maxEnvelopes([[5, 4], [6, 4], [6, 7], [2, 3]]) == 3, 'wrong result'
    assert solution.maxEnvelopes([[1, 1], [1, 1], [1, 1]]) == 1, 'wrong result'


if __name__ == '__main__':
    test_max_envelopes()
