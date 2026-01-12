from typing import List
from collections import Counter


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_to_col = Counter()
        col_to_ball = Counter()
        res = []
        for ball, col in queries:
            if ball in ball_to_col:
                temp = ball_to_col[ball]
                if col_to_ball[temp] == 1:
                    col_to_ball.pop(temp)
                else:
                    col_to_ball[temp] -= 1

            col_to_ball[col] += 1
            ball_to_col[ball] = col
            res.append(len(col_to_ball.keys()))

        return res


def test_query_results():
    solution = Solution()
    assert solution.queryResults(4, [[1, 4], [2, 5], [1, 3], [3, 4]]) == [1, 2, 2, 3], 'wrong result'
    assert solution.queryResults(4, [[0, 1], [1, 2], [2, 2], [3, 4], [4, 5]]) == [1, 2, 2, 3, 4], 'wrong result'


if __name__ == '__main__':
    test_query_results()
