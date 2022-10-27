from typing import List
from heapq import heapify, heappop, heappush


class Solution:
    def fillCups(self, amount: List[int]) -> int:
        return max(max(amount), (sum(amount) + 1) // 2)

    # heap
    def fillCups2(self, amount: List[int]) -> int:
        heap = [-x for x in amount]
        heapify(heap)
        res = 0
        while heap[0] != 0:
            mx1 = heappop(heap)
            mx2 = heappop(heap)
            res += 1

            heappush(heap, mx1 + 1)
            heappush(heap, mx2 + 1)

        return res

    # greedy
    def fillCups1(self, amount: List[int]) -> int:
        amount.sort()
        res = 0
        while amount[2] != 0:
            res += 1
            amount[2] -= 1
            amount[1] -= 1
            amount.sort()
        return res


def test_fill_cups():
    solution = Solution()
    assert solution.fillCups([1, 4, 2]) == 4, 'wrong result'
    assert solution.fillCups([5, 4, 4]) == 7, 'wrong result'
    assert solution.fillCups([5, 0, 0]) == 5, 'wrong result'


if __name__ == '__main__':
    test_fill_cups()
