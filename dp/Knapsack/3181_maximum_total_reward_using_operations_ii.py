from typing import List
from functools import lru_cache
from bisect import bisect_left


class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        rewardValues = sorted(set(rewardValues))
        # 这里x表示0，比特位从0开始算起，比如：这里x可以表示为二进制0001，最低位的1表示0，如果表示1，可以写为0010
        x = 1
        for i in rewardValues:
            valid_x = x & ((1 << i) - 1)
            # for each value in valid_x, we add num to it
            # for example, if we have x = 5 (binary 100000) and num = 6
            # then we will have new x = 11, whose binary = 10000000000
            # == (100000) << 6
            x |= valid_x << i
        return x.bit_length() - 1

    # TLE
    def maxTotalReward1(self, rewardValues: List[int]) -> int:
        @lru_cache(None)
        def dfs(i, x):
            if i >= len(rewardValues):
                return x

            return max(dfs(i + 1, x), dfs(i + 1, x + rewardValues[i]) if rewardValues[i] > x else 0)

        rewardValues = sorted(set(rewardValues))
        return dfs(0, 0)


def test_max_total_reward():
    solution = Solution()
    # assert solution.maxTotalReward([6, 13, 9, 19]) == 34, 'wrong result'
    # assert solution.maxTotalReward([2, 15, 14, 18]) == 35, 'wrong result'
    # assert solution.maxTotalReward([1, 1, 3, 3]) == 4, 'wrong result'
    assert solution.maxTotalReward([1, 6, 4, 3, 2]) == 11, 'wrong result'


if __name__ == '__main__':
    test_max_total_reward()
