from typing import List


class Solution:
    def minMoves(self, balance: List[int]) -> int:
        tot = 0
        p = -1
        for i, x in enumerate(balance):
            if x < 0:
                p = i
            tot += x
        if tot < 0:
            return -1
        if p < 0:
            return 0

        n = len(balance)
        res = 0
        dist = 0
        while balance[p] < 0:
            dist += 1
            storage = balance[(p + dist) % n] + balance[p - dist]
            res += min(-balance[p], storage) * dist
            balance[p] += storage
        return res


def test_min_moves():
    solution = Solution()
    # assert solution.minMoves([5,1,-4]) == 4, 'wrong result'
    assert solution.minMoves([1,2,-5,2]) == 6, 'wrong result'
    assert solution.minMoves([-3,2]) == -1, 'wrong result'


if __name__ == '__main__':
    test_min_moves()
