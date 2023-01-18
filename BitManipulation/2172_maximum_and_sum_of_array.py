from typing import List
from functools import lru_cache


class Solution:
    # bit mask base 3
    # https://leetcode.com/problems/maximum-and-sum-of-array/solutions/1766824/java-c-python-dp-solution/
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        # dp方法表示当为mask的时候如何分配nums[i]，达到最优解
        @lru_cache(None)
        def dp(i, mask):
            res = 0
            if i == len(nums):
                return 0
            for slot in range(1, numSlots + 1):
                # 每个slot对应的基数, 比如10进制下120百分位的基数就是10 ** (2 - 1) = 100
                b = 3 ** (slot - 1)
                if mask // b % 3 > 0:
                    res = max(res, (slot & nums[i]) + dp(i + 1, mask - b))
            return res

        return dp(0, 3 ** numSlots - 1)

    # bit mask base 2
    def maximumANDSum1(self, nums: List[int], numSlots: int) -> int:
        f = [0] * (1 << (numSlots * 2))
        for i, fi in enumerate(f):
            c = bin(i).count('1')
            # 如果已经满足或超出了总的位置，无法放置，要跳过。
            if c >= len(nums):
                continue
            for j in range(numSlots * 2):
                # 找到空的栏位
                if (i & (1 << j)) == 0:
                    cur = i | (1 << j)
                    f[cur] = max(f[cur], ((j // 2 + 1) & nums[c]) + fi)
        # 优化，如果放在上面for里每次做比较，比较的次数远远大于从f里直接找出最大值的次数。
        return max(f)


def test_maximum_and_sum():
    solution = Solution()
    assert solution.maximumANDSum([1, 2, 3, 4, 5, 6], 3) == 9, 'wrong result'
    assert solution.maximumANDSum([1, 3, 10, 4, 7, 1], 9) == 24, 'wrong result'


if __name__ == '__main__':
    test_maximum_and_sum()
