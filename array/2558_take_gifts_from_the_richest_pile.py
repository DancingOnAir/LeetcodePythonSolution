from typing import List
from heapq import heapify, heappop, heappush


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-x for x in gifts]
        heapify(gifts)
        while k > 0:
            heappush(gifts, -int((-heappop(gifts)) ** 0.5))
            k -= 1
        return -sum(gifts)


def test_pick_gifts():
    solution = Solution()
    assert solution.pickGifts([25, 64, 9, 4, 100], 4) == 29, 'wrong result'
    assert solution.pickGifts([1, 1, 1, 1], 4) == 4, 'wrong result'


if __name__ == '__main__':
    test_pick_gifts()
