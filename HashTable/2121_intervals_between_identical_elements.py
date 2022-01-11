from typing import List
from itertools import accumulate


class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        res = [0] * len(arr)
        pre, suf = [0] * len(arr), [0] * len(arr)

        freq = dict()
        for i, val in enumerate(arr):
            freq.setdefault(val, []).append(i)

        for vs in freq.values():
            for i in range(1, len(vs)):
                pre[vs[i]] = pre[vs[i - 1]] + i * (vs[i] - vs[i - 1])
        for vs in freq.values():
            for i in range(len(vs) - 2, -1, -1):
                suf[vs[i]] = suf[vs[i + 1]] + (len(vs) - i - 1) * (vs[i + 1] - vs[i])

        for i in range(len(arr)):
            res[i] = pre[i] + suf[i]
        return res


    # for given list 1, 3, 5, 7, 9:
    # For example, we choose i = 3 or the number l[i] = 7.
    # To find abs difference for numbers smaller than equal to 7:
    # 7 - 1 + 7 - 3 + 7 - 5 + 7 - 7 => 7 * 4 - (1 + 3 + 5 + 7) => 7 * (i + 1) - pre[i + 1]
    # Similarly
    # ((pre[len(l)] - pre[i]) - v * (len(l) - (i))) calculates abs difference between l[i] and numbers greater than l[i]
    def getDistances2(self, arr: List[int]) -> List[int]:
        res = [0] * len(arr)
        freq = dict()

        for i, val in enumerate(arr):
            freq.setdefault(val, []).append(i)

        for vs in freq.values():
            pre_sum = [0]
            pre_sum += list(accumulate(vs))
            for i, v in enumerate(vs):
                res[v] = (v * i - pre_sum[i + 1]) + (pre_sum[-1] - pre_sum[i] - v * (len(vs) - i - 1))
        return res

    # brute force, TLE
    def getDistances1(self, arr: List[int]) -> List[int]:
        res = [0] * len(arr)

        freq = dict()
        for i, val in enumerate(arr):
            freq.setdefault(val, []).append(i)

        for k, vs in freq.items():
            for v in vs:
                res[v] = sum(abs(v - x) for x in vs if x != v)
        return res


def test_get_distances():
    solution = Solution()
    assert solution.getDistances([2, 1, 3, 1, 2, 3, 3]) == [4, 2, 7, 2, 4, 4, 5], 'wrong result'
    assert solution.getDistances([10, 5, 10, 10]) == [5, 0, 3, 4], 'wrong result'


if __name__ == '__main__':
    test_get_distances()
