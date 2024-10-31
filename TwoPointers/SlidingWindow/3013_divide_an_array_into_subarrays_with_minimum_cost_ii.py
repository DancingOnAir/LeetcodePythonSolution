from typing import List
from sortedcontainers import SortedList


class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        n = len(nums)
        k -= 1
        L, R = SortedList(nums[1: dist + 2]), SortedList()
        tot = sum(nums[:dist + 2])

        def add(val):
            if L and val < L[-1]:
                nonlocal tot
                tot += val
                L.add(val)
            else:
                R.add(val)

        def remove(val):
            if val in L:
                nonlocal tot
                tot -= val
                L.remove(val)
            else:
                R.remove(val)

        def l2r():
            nonlocal tot
            p = L.pop()
            tot -= p
            R.add(p)

        def r2l():
            nonlocal tot
            p = R.pop(0)
            tot += p
            L.add(p)

        while len(L) > k:
            l2r()

        res = tot
        for i in range(dist + 2, len(nums)):
            out = nums[i - dist - 1]
            remove(out)
            add(nums[i])

            if len(L) == k - 1:
                r2l()
            elif len(L) == k + 1:
                l2r()
            res = min(res, tot)
        return res

    # bisect & sorted list
    def minimumCost1(self, nums: List[int], k: int, dist: int) -> int:
        n = len(nums)
        sl = SortedList(nums[1: dist + 1])
        cur, res = sum(sl[:k-2]), float('inf')
        for i in range(dist + 1, n):
            if sl.bisect_right(nums[i]) < k - 1:
                cur += nums[i]
            else:
                cur += sl[k - 2]
            res = min(res, cur)
            sl.add(nums[i])

            if sl.bisect_right(nums[i - dist]) < k - 1:
                cur -= nums[i - dist]
            else:
                cur -= sl[k - 2]
            sl.remove(nums[i - dist])

        return res + nums[0]


def test_minimum_cost():
    solution = Solution()
    assert solution.minimumCost([1, 3, 2, 6, 4, 2], 3, 3) == 5, 'wrong result'
    assert solution.minimumCost([10, 1, 2, 2, 2, 1], 4, 3) == 15, 'wrong result'
    assert solution.minimumCost([10, 8, 18, 9], 3, 1) == 36, 'wrong result'


if __name__ == '__main__':
    test_minimum_cost()
