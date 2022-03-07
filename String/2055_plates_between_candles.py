from typing import List
from bisect import bisect_left, bisect_right


class Solution:
    # Find out indices of candies and add them to a list A
    # For each query [a,b],
    # find out the candies after a and the candies before b.
    #
    # A[i] - A[j] + 1 is the length between two candies,
    # i - j + 1is the number of candies.
    # (A[j] - A[i]) - (j - i) is the number of plates between two candies.
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        A = [i for i, ch in enumerate(s) if ch == '|']

        res = list()
        for a, b in queries:
            i = bisect_left(A, a)
            j = bisect_right(A, b) - 1
            res.append(A[j] - A[i] - (j - i) if j > i else 0)
        return res

    # find the nearest candle index on the left and on the right
    def platesBetweenCandles1(self, s: str, queries: List[List[int]]) -> List[int]:
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
            p2 = bisect(candle, q[1])
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
