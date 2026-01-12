from typing import List
from itertools import accumulate
from bisect import bisect_right


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        pre = list(accumulate(sorted(nums)))
        return [bisect_right(pre, x) for x in queries]

    def answerQueries1(self, nums: List[int], queries: List[int]) -> List[int]:
        res = list()
        pre_sum = list(accumulate(sorted(nums)))
        for x in queries:
            res.append(bisect_right(pre_sum, x))
        return res


def test_answer_queries():
    solution = Solution()
    assert solution.answerQueries([4, 5, 2, 1], [3, 10, 21]) == [2, 3, 4], 'wrong result'
    assert solution.answerQueries([2, 3, 4, 5], [1]) == [0], 'wrong result'


if __name__ == '__main__':
    test_answer_queries()
