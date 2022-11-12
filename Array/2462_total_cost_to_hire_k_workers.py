from typing import List
from heapq import heapify, heappop, heappush


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n, res = len(costs), 0
        pairs = [(v, i) for i, v in enumerate(costs)]
        l, r = min(candidates, n // 2), max(n - candidates, n // 2)
        pq = pairs[:l] + pairs[r:]

        heapify(pq)
        for _ in range(k):
            cost, i = heappop(pq)
            if i < l:
                i, l = l, l + 1
            if i >= r:
                i, r = r - 1, r - 1
            if l <= r:
                heappush(pq, pairs[i])
            res += cost
        return res

    def totalCost1(self, costs: List[int], k: int, candidates: int) -> int:
        res = 0
        n = len(costs)
        i, j = 0, n - 1
        h, t = list(), list()
        while k:
            while len(h) < candidates and i < j:
                heappush(h, costs[i])
                i += 1

            while len(t) < candidates and j >= i:
                heappush(t, costs[j])
                j -= 1

            if not t:
                res += heappop(h)
            elif not h:
                res += heappop(t)
            elif h[0] <= t[0]:
                res += heappop(h)
            else:
                res += heappop(t)
            k -= 1

        return res


def test_total_cost():
    solution = Solution()
    assert solution.totalCost([17, 12, 10, 2, 7, 2, 11, 20, 8], 3, 4) == 11, 'wrong result'
    assert solution.totalCost([1, 2, 4, 1], 3, 3) == 4, 'wrong result'


if __name__ == '__main__':
    test_total_cost()
