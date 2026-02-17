from typing import List
from bisect import bisect_left


class Solution:


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
