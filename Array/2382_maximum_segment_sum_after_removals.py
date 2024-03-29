from typing import List
from itertools import accumulate


class UF:
    def __init__(self, nums):
        self.parent = list(range(len(nums)))
        self.sum = [x for x in nums]

    def find(self, p):
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    def unite(self, p, q):
        self.sum[self.find(q)] += self.sum[self.find(p)]
        self.parent[self.find(p)] = self.find(q)


class Solution:
    # pre sum
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        n = len(nums)
        left = list(range(n))
        right = list(range(n))
        seen = [False] * n

        pre_sum = [0] + list(accumulate(nums))
        res = list()
        mx = 0
        for x in removeQueries[::-1]:
            res.append(mx)
            seen[x] = True
            l, r = x, x
            if x - 1 >= 0 and seen[x - 1]:
                l = left[x - 1]
            if x + 1 < n and seen[x + 1]:
                r = right[x + 1]
            left[r] = l
            right[l] = r
            mx = max(mx, pre_sum[r + 1] - pre_sum[l])
        return res[::-1]

    # union find
    def maximumSegmentSum2(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        n = len(nums)
        uf = UF(nums)
        seen = [False] * n
        res = [0] * n
        cur = 0
        for i in range(n - 1, 0, -1):
            x = removeQueries[i]
            seen[x] = True

            if x > 0 and seen[x - 1]:
                uf.unite(x - 1, x)
            if x < n - 1 and seen[x + 1]:
                uf.unite(x, x + 1)
            cur = max(cur, uf.sum[uf.find(x)])
            res[i - 1] = cur
        return res

    # union find, only union 1 time
    def maximumSegmentSum1(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        def find(x):
            if x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]

        n = len(nums)
        parents = list(range(n + 1))
        total = [0] * (n + 1)
        res = [0] * n
        for i in range(n - 1, 0, -1):
            x = removeQueries[i]
            pa = find(x + 1)
            # 将x和x+1合并
            parents[x] = pa

            total[pa] += total[x] + nums[x]
            res[i - 1] = max(res[i], total[pa])
        return res


def test_maximum_segment_sum():
    solution = Solution()
    assert solution.maximumSegmentSum([1, 2, 5, 6, 1], [0, 3, 2, 4, 1]) == [14, 7, 2, 2, 0], 'wrong result'
    assert solution.maximumSegmentSum([3, 2, 11, 1], [3, 2, 1, 0]) == [16, 5, 3, 0], 'wrong result'


if __name__ == '__main__':
    test_maximum_segment_sum()

