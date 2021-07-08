from typing import List


class Solution:
    # pattern 4
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        fn = lambda x: sum(max(0, x - xx) for xx in inventory)

        lo, hi, mod = 0, max(inventory), 10 ** 9 + 7
        while lo < hi:
            mid = lo + hi + 1 >> 1
            if fn(mid) >= orders:
                lo = mid
            else:
                hi = mid - 1
        res = sum((x + lo + 1) * (x - lo) // 2 for x in inventory if x > lo)
        return (res - (fn(lo) - orders) * (lo + 1)) % mod

    # https://leetcode.com/problems/sell-diminishing-valued-colored-balls/discuss/927560/C%2B%2B-Binary-Answer-or-Sort%2BGreedy
    # pattern 3
    def maxProfit1(self, inventory: List[int], orders: int) -> int:
        def have_enough_balls(x):
            res = 0
            for i in range(n - 1, -1, -1):
                if inventory[i] <= x:
                    break
                res += inventory[i] - x
            return res

        def calc_amount(x):
            res = 0
            for i in range(n - 1, - 1, -1):
                if inventory[i] <= x:
                    break
                res += (inventory[i] + x + 1) * (inventory[i] - x) // 2
            return res

        MOD = 10 ** 9 + 7
        inventory.sort()
        lo, hi = 0, inventory[-1]
        n = len(inventory)
        while lo < hi:
            mid = lo + hi >> 1
            if have_enough_balls(mid) > orders:
                lo = mid + 1
            else:
                hi = mid

        res = calc_amount(lo) % MOD
        already_ordered = have_enough_balls(lo)
        if already_ordered == orders:
            return res
        return (res + (orders - already_ordered) * lo) % MOD


def test_max_profit():
    solution = Solution()

    assert solution.maxProfit([2, 5], 4) == 14, 'wrong result'
    assert solution.maxProfit([3, 5], 6) == 19, 'wrong result'
    assert solution.maxProfit([2, 8, 4, 10, 6], 20) == 110, 'wrong result'
    assert solution.maxProfit([1000000000], 1000000000) == 21, 'wrong result'


if __name__ == '__main__':
    test_max_profit()
