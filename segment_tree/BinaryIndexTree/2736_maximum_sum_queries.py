from typing import List


class BinaryIndexTree:
    def __init__(self, n):
        self.tree = [-1] * (n + 1)

    def add(self, i, v):
        while i < len(self.tree):
            self.tree[i] = max(self.tree[i], v)
            i += i & -i

    def query(self, i):
        res = -1
        while i > 0:
            res = max(res, self.tree[i])
            i -= i & -i
        return res


class Solution:
    def maximumSumQueries(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        n, m = len(nums1), len(queries)
        nums = list(zip(nums1, nums2))
        nq = [(x, y, i) for i, (x, y) in enumerate(queries)]

        # 离散化
        unique_set = set()
        for x in nums:
            unique_set.add(x[1])
        for q in queries:
            unique_set.add(q[1])
        unique_list = list(unique_set)
        unique_list.sort()
        sz = len(unique_list)
        mapping = {v: i for i, v in enumerate(unique_list)}

        # 排序，解决1维限制
        nums.sort(key=lambda x: x[0], reverse=True)
        nq.sort(key=lambda x: x[0], reverse=True)
        pass

        t = BinaryIndexTree(sz + 1)
        res = [0] * m
        j = 0
        for x, y, i in nq:
            while j < n and nums[j][0] >= x:
                t.add(sz - mapping[nums[j][1]], nums[j][0] + nums[j][1])
                j += 1
            # 查询树状数组里的最值，比sz - mapping[y]小，也就是比y大的数对应的最值
            res[i] = t.query(sz - mapping[y])
        return res


def test_maximum_sum_queries():
    solution = Solution()
    assert solution.maximumSumQueries([4, 3, 1, 2], [2, 4, 9, 5], [[4, 1], [1, 3], [2, 5]]) == [6, 10,
                                                                                                7], 'wrong result'
    assert solution.maximumSumQueries([3, 2, 5], [2, 3, 4], [[4, 4], [3, 2], [1, 1]]) == [9, 9, 9], 'wrong result'


if __name__ == '__main__':
    test_maximum_sum_queries()
