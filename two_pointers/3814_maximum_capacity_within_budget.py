from typing import List
from bisect import bisect_left


class Solution:
    # monostack
    def maxCapacity(self, costs: List[int], capacity: List[int], budget: int) -> int:
        a = [(cost, cap) for cost, cap in zip(costs, capacity) if cost < budget]
        a.sort(key=lambda x: x[0])

        stk = [(0, 0)]
        res = 0
        for cost, cap in a:
            while cost + stk[-1][0] >= budget:
                stk.pop()
            res = max(res, stk[-1][1] + cap)
            if cap > stk[-1][1]:
                stk.append((cost, cap))
        return res

    # two points
    def maxCapacity2(self, costs: List[int], capacity: List[int], budget: int) -> int:
        a = [(cost, cap) for cost, cap in zip(costs, capacity) if cost < budget]
        a.sort(key=lambda x: x[0])

        pre_max = [0] * (len(a) + 1)
        l = res = 0
        for r in range(len(a) - 1, -1, -1):
            while l < r and a[l][0] + a[r][0] < budget:
                pre_max[l + 1] = max(pre_max[l], a[l][1])
                l += 1
            res = max(res, pre_max[min(l, r)] + a[r][1])
        return res

    # binary search
    def maxCapacity1(self, costs: List[int], capacity: List[int], budget: int) -> int:
        a = []
        for cost, cap in zip(costs, capacity):
            if cost < budget:
                a.append((cost, cap))
        a.sort(key=lambda x: x[0])

        premax = [0] * (len(a) + 1)
        res = 0
        for i, (cost, cap) in enumerate(a):
            # param: 1. 数组, 2. 上限，找到就停止的值 3. key是排序方式
            j = bisect_left(range(i), budget - cost, key=lambda x: a[x][0])
            res = max(res, cap + premax[j])
            premax[i + 1] = max(premax[i], cap)
        return res


def test_max_capacity():
    solution = Solution()
    assert solution.maxCapacity([4, 8, 5, 3], capacity=[1, 5, 2, 7], budget=8) == 8, 'wrong result'
    assert solution.maxCapacity([3, 5, 7, 4], capacity=[2, 4, 3, 6], budget=7) == 6, 'wrong result'
    assert solution.maxCapacity([2, 2, 2], capacity=[3, 5, 4], budget=5) == 9, 'wrong result'


if __name__ == '__main__':
    test_max_capacity()
