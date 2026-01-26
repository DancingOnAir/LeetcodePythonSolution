import heapq
from typing import List
from collections import defaultdict
from heapq import heappop, heappush


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        mods = [[] for _ in range(3)]
        for x in nums:
            mods[x % 3].append(x)

        if [] in mods:
            res = 0
        else:
            res = max(mods[0]) + max(mods[1]) + max(mods[2])

        for m in mods:
            if len(m) < 3:
                continue
            res = max(res, sum(heapq.nlargest(3, m)))
        return res

    def maximumSum1(self, nums: List[int]) -> int:
        cnt = defaultdict(list)
        for x in nums:
            heappush(cnt[x % 3], -x)

        def helper(r):
            top3 = []
            i = 0
            while len(cnt[r]) > 0 and i < 3:
                top3.append(-heappop(cnt[r]))
                i += 1
            return top3

        res = 0
        zeros = helper(0)
        if len(zeros) == 3:
            res = sum(zeros)

        ones = helper(1)
        if len(ones) == 3:
            res = max(res, sum(ones))

        twos = helper(2)
        if len(twos) == 3:
            res = max(res, sum(twos))

        if zeros and ones and twos:
            res = max(res, zeros[0] + ones[0] + twos[0])
        return res


def test_maximum_sum():
    solution = Solution()
    assert solution.maximumSum([4, 2, 3, 1]) == 9, 'wrong result'
    assert solution.maximumSum([2, 1, 5]) == 0, 'wrong result'


if __name__ == '__main__':
    test_maximum_sum()
