from typing import List
from heapq import heappush, heappop


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        hp = []
        for i, x in enumerate(nums):
            heappush(hp, (x, i))

        while k:
            x, i = heappop(hp)
            heappush(hp, (x * multiplier, i))
            k -= 1
        return [x for x, _ in sorted(hp, key=lambda x: x[1])]


def test_get_final_state():
    solution = Solution()
    assert solution.getFinalState([2, 1, 3, 5, 6], 5, 2) == [8, 4, 6, 5, 6], 'wrong result'
    assert solution.getFinalState([1, 2], 3, 4) == [16, 8], 'wrong result'


if __name__ == '__main__':
    test_get_final_state()
