from typing import List
from heapq import heappush, heappop, heapreplace
from math import pow


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        if multiplier == 1:
            return nums

        mx = max(nums)
        n, MOD = len(nums), 10 ** 9 + 7
        hp = []
        for i, x in enumerate(nums):
            heappush(hp, (x, i))

        while k and hp[0][0] < mx:
            x, i = hp[0]
            heapreplace(hp, (x * multiplier, i))
            k -= 1

        hp.sort()
        for i, (x, j) in enumerate(hp):
            q, r = divmod(k, n)
            nums[j] = x * pow(multiplier, q + (i < r)) % MOD

        return nums


def test_get_final_state():
    solution = Solution()
    assert solution.getFinalState([1], 3, 10) == [1000], 'wrong result'
    assert solution.getFinalState([2, 1, 3, 5, 6], 5, 2) == [8, 4, 6, 5, 6], 'wrong result'
    assert solution.getFinalState([100000,2000], 2, 1000000) == [999999307,999999993], 'wrong result'


if __name__ == '__main__':
    test_get_final_state()
