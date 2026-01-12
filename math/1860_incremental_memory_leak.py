from typing import List
from heapq import heappush, heappop, heapify, heapreplace


class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        crash = 1
        hp = [[-memory1, 1], [-memory2, 2]]
        heapify(hp)
        while -hp[0][0] >= crash:
            heapreplace(hp, [hp[0][0] + crash, hp[0][1]])
            crash += 1

        res = [crash, 0, 0]
        while hp:
            tmp = heappop(hp)
            res[tmp[1]] = -tmp[0]
        return res


def test_mem_leak():
    solution = Solution()
    assert solution.memLeak(2, 2) == [3, 1, 0], 'wrong result'
    assert solution.memLeak(8, 11) == [6, 0, 4], 'wrong result'


if __name__ == '__main__':
    test_mem_leak()

