from typing import List
from functools import lru_cache, cache


class Solution:
    # https://leetcode.cn/problems/minimum-time-to-break-locks-i/
    def findMinimumTime(self, strength: List[int], K: int) -> int:
        n = len(strength)
        done = [False] * n
        res = float('inf')

        def dfs(i, time):
            nonlocal res
            if time >= res:
                return
            if i == n:
                res = time
                return

            x = 1 + i * K
            for j, s in enumerate(strength):
                if not done[j]:
                    done[j] = True
                    dfs(i + 1, time + (s - 1) // x + 1)
                    done[j] = False

        dfs(0, 0)
        return res


def test_find_minimum_time():
    solution = Solution()
    assert solution.findMinimumTime([3, 4, 1], 1) == 4, 'wrong result'
    assert solution.findMinimumTime([2, 5, 4], 2) == 5, 'wrong result'


if __name__ == '__main__':
    test_find_minimum_time()
