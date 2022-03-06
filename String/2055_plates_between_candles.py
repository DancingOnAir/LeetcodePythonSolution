from typing import List


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        num_asterisk = 0
        memo = dict()
        for i, ch in enumerate(s):
            if ch == '*':
                num_asterisk += 1
            else:
                memo[i] = num_asterisk

        pass


def test_plates_between_candles():
    solution = Solution()
    assert solution.platesBetweenCandles("**|**|***|", [[2, 5], [5, 9]]) == [2, 3], 'wrong result'
    assert solution.platesBetweenCandles("***|**|*****|**||**|*", [[1, 17], [4, 5], [14, 17], [5, 11], [15, 16]]) \
           == [9, 0, 0, 0, 0], 'wrong result'


if __name__ == '__main__':
    test_plates_between_candles()
