from typing import List
from sortedcontainers import SortedList
from collections import Counter


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        L, R = SortedList(), SortedList()
        cnt = Counter()
        tot = 0

        def add(val):
            if cnt[val] == 0:
                return
            p = (cnt[val], val)
            if L and p > L[0]:
                nonlocal tot
                tot += p[0] * p[1]
                L.add(p)
            else:
                R.add(p)

        def remove(val):
            if cnt[val] == 0:
                return
            p = (cnt[val], val)
            if p in L:
                nonlocal tot
                tot -= p[0] * p[1]
                L.remove(p)
            else:
                R.remove(p)

        def l2r():
            p = L[0]
            nonlocal tot
            tot -= p[0] * p[1]
            L.remove(p)
            R.add(p)

        def r2l():
            p = R[-1]
            nonlocal tot
            tot += p[0] * p[1]
            L.add(p)
            R.remove(p)

        res = [0] * (len(nums) - k + 1)
        for r, num in enumerate(nums):
            cnt[num] += 1
            add(num)

            l = r - k + 1
            if l < 0:
                continue

            while R and len(L) < x:
                r2l()
            while len(L) > x:
                l2r()
            res[l] = tot

            out = nums[l]
            remove(out)
            cnt[out] -= 1
            add(out)
        return res


def test_find_x_sum():
    solution = Solution()
    assert solution.findXSum([1, 1, 2, 2, 3, 4, 2, 3], 6, 2) == [6, 10, 12], 'wrong result'
    assert solution.findXSum([3, 8, 7, 8, 7, 5], 2, 2) == [11, 15, 15, 15, 12], 'wrong result'


if __name__ == '__main__':
    test_find_x_sum()