from typing import List
from bisect import bisect_left


class Solution:
    # z function
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        def cal_z(p):
            ss = p + '#' + s
            n, m = len(ss), len(p)
            z = [0] * n
            l, r = 0, 0
            res = []

            for i in range(1, n):
                if i <= r:
                    z[i] = min(z[i - l], r - i + 1)

                while z[i] + i < n and ss[z[i]] == ss[z[i] + i]:
                    l, r = i, z[i] + i
                    z[i] += 1

                if z[i] == m:
                    res.append(i - m - 1)
            return res

        pa, pb = cal_z(a), cal_z(b)
        ans = []
        for x in pa:
            i = bisect_left(pb, x)
            if (i < len(pb) and pb[i] - x <= k) or (i > 0 and x - pb[i - 1] <= k):
                ans.append(x)
        return ans


def test_beautiful_indices():
    solution = Solution()
    assert solution.beautifulIndices("xxtxxuftxt", "tx", "x", 2) == [2, 7], 'wrong result'
    assert solution.beautifulIndices("isawsquirrelnearmysquirrelhouseohmy", "my", "squirrel", 15) == [16, 33], 'wrong result'
    assert solution.beautifulIndices("abcd", "a", "a", 4) == [0], 'wrong result'


if __name__ == '__main__':
    test_beautiful_indices()
