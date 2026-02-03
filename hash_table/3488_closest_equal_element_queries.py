from typing import List
from collections import defaultdict
from bisect import bisect_left


class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        cnt = defaultdict(list)
        for i, x in enumerate(nums):
            cnt[x].append(i)

        n = len(nums)
        res = []
        for i in queries:
            x = nums[i]
            if len(cnt[x]) < 2:
                res.append(-1)
            else:
                j = bisect_left(cnt[x], i)
                if j == 0:
                    mi = min(cnt[x][j] + n - cnt[x][-1], cnt[x][j + 1] - cnt[x][j])
                elif j == len(cnt[x]) - 1:
                    mi = min(cnt[x][j] - cnt[x][j - 1], cnt[x][0] + n - cnt[x][j])
                else:
                    mi = min(cnt[x][j] - cnt[x][j - 1], cnt[x][j + 1] - cnt[x][j])
                res.append(mi)

        return res


def test_solve_queries():
    solution = Solution()
    assert solution.solveQueries([1, 3, 1, 4, 1, 3, 2], queries=[0, 3, 5]) == [2, -1, 3], 'wrong result'
    assert solution.solveQueries([1, 2, 3, 4], queries=[0, 1, 2, 3]) == [-1, -1, -1, -1], 'wrong result'


if __name__ == '__main__':
    test_solve_queries()
