from typing import List
from bisect import bisect_left


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        num_plate = 0
        memo = dict()
        for i, ch in enumerate(s):
            if ch == '*':
                num_plate += 1
            else:
                memo[i] = num_plate

        candle = list(memo.keys())
        res = list()
        for q in queries:
            p1 = bisect_left(candle, q[0])
            p2 = bisect_left(candle, q[1])
            if p1 == p2:
                res.append(0)
                continue

            if p2 == len(candle) or (candle[p2] > q[1] and p2 > p1):
                p2 -= 1
            res.append(memo[candle[p2]] - memo[candle[p1]])
        return res


def test_plates_between_candles():
    solution = Solution()
    assert solution.platesBetweenCandles("**|**|***|", [[2, 5], [5, 9]]) == [2, 3], 'wrong result'
    assert solution.platesBetweenCandles("***|**|*****|**||**|*", [[1, 17], [4, 5], [14, 17], [5, 11], [15, 16]]) \
           == [9, 0, 0, 0, 0], 'wrong result'


if __name__ == '__main__':
    test_plates_between_candles()
