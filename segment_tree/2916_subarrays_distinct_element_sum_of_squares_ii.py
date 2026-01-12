from typing import List
from collections import Counter


class Solution:
    # https://leetcode.cn/problems/subarrays-distinct-element-sum-of-squares-ii/solutions/2502897/yi-bu-bu-ti-shi-ni-si-kao-ben-ti-pythonj-zhhs/
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        tot = [0] * (n * 4)
        todo = [0] * (n * 4)

        def do(idx, l, r, add):
            tot[idx] += add * (r - l + 1)
            todo[idx] += add

        def query_and_add_one(idx, l, r, L, R):
            if L <= l and r <= R:
                res = tot[idx]
                do(idx, l, r, 1)
                return res

            m = (l + r) // 2
            add = todo[idx]
            if add:
                do(idx * 2, l, m, add)
                do(idx * 2 + 1, m + 1, r, add)
                todo[idx] = 0

            res = 0
            if L <= m:
                res += query_and_add_one(idx * 2, l, m, L, R)
            if m < R:
                res += query_and_add_one(idx * 2 + 1, m + 1, r, L, R)
            tot[idx] = tot[idx * 2] + tot[idx * 2 + 1]
            return res

        ans = s = 0
        last = {}
        for i, x in enumerate(nums, 1):
            j = last.get(x, 0)
            s += query_and_add_one(1, 1, n, j + 1, i) * 2 + i - j
            ans += s
            last[x] = i
        return ans % (10 ** 9 + 7)


def test_sum_counts():
    solution = Solution()
    assert solution.sumCounts([1, 2, 1]) == 15, 'wrong result'
    assert solution.sumCounts([1, 1]) == 3, 'wrong result'


if __name__ == '__main__':
    test_sum_counts()
