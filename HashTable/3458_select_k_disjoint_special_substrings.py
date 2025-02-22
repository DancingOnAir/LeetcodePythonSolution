from collections import defaultdict
from bisect import bisect_left


class Solution:
    def maxSubstringLength(self, s: str, k: int) -> bool:
        if k == 0:
            return True

        pos = defaultdict(list)
        for i, c in enumerate(s):
            pos[c].append(i)

        g = defaultdict(list)
        for i, p in pos.items():
            l, r = p[0], p[-1]
            for j, q in pos.items():
                if j == i:
                    continue
                qi = bisect_left(q, l)
                if qi < len(q) and q[qi] <= r:
                    g[i].append(j)

        def dfs(u):
            nonlocal l, r
            seen.add(u)
            p = pos[u]
            l = min(l, p[0])
            r = max(r, p[-1])
            for v in g[u]:
                if v not in seen:
                    dfs(v)

        def maxNonOverlapIntervals(intervals):
            intervals.sort(key=lambda x: x[1])
            res = 0
            pre_r = -1
            for l, r in intervals:
                if l > pre_r:
                    res += 1
                    pre_r = r
            return res

        intervals = []
        for i, p in pos.items():
            seen = set()
            l, r = float('inf'), 0
            dfs(i)
            if l > 0 or r < len(s) - 1:
                intervals.append((l, r))

        return maxNonOverlapIntervals(intervals) >= k


def test_max_substring_length():
    solution = Solution()
    assert solution.maxSubstringLength("abcdbaefab", k=2), 'wrong result'
    assert not solution.maxSubstringLength("cdefdc", 3), 'wrong result'
    assert solution.maxSubstringLength("abeabe", k=0), 'wrong result'


if __name__ == '__main__':
    test_max_substring_length()
