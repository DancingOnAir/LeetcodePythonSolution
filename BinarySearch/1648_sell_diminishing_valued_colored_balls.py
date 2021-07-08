from typing import List
from bisect import bisect_right


class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        def get_orders(x):
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
            if get_orders(mid) > orders:
                lo = mid + 1
            else:
                hi = mid

        res = calc_amount(lo) % MOD
        already_ordered = get_orders(lo)
        if already_ordered == orders:
            return res
        return (res + (orders - already_ordered) * lo) % MOD

        # def helper(x):
        #     return sum(inventory[x:]) - inventory[x] * (n - x)
        #
        # def calc(x, y):
        #     return (y + x + 1) * (y - x) // 2
        #
        # MOD = 10 ** 9 + 7
        # n = len(inventory)
        # inventory.sort()
        # left, right = 0, n - 1
        #
        # while left < right:
        #     mid = left + right >> 1
        #     if helper(mid) > orders:
        #         left = mid + 1
        #     else:
        #         right = mid
        #
        # res = calc(inventory[left], inventory[-1])
        # times = helper(left)
        # if times == orders:
        #     return res % MOD
        #
        # q, r = divmod(orders - times, n - left)
        # return res + (inventory[left] + inventory[left] - q + 1) * q * (n - left) // 2 + (inventory[left] - q + 1) * r


def test_max_profit():
    solution = Solution()

    assert solution.maxProfit([2, 5], 4) == 14, 'wrong result'
    assert solution.maxProfit([3, 5], 6) == 19, 'wrong result'
    assert solution.maxProfit([2, 8, 4, 10, 6], 20) == 110, 'wrong result'
    assert solution.maxProfit([1000000000], 1000000000) == 21, 'wrong result'


if __name__ == '__main__':
    test_max_profit()
