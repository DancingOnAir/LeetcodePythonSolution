from typing import List


class Solution:
    #
    def smallestMissingValueSubtree(self, parents: List[int], nums: List[int]) -> List[int]:
        n = len(parents)
        seen = [0] * 100010
        res = [1] * n
        if 1 not in nums:
            return res

        tree = [[] for _ in range(n)]
        for i in range(1, n):
            tree[parents[i]].append(i)

        def dfs(node):
            if seen[nums[node]] == 0:
                for j in tree[node]:
                    dfs(j)
                seen[nums[node]] = 1

        i = nums.index(1)
        miss = 1
        while i >= 0:
            dfs(i)
            while seen[miss]:
                miss += 1
            res[i] = miss
            i = parents[i]
        return res

    # TLE
    def smallestMissingValueSubtree1(self, parents: List[int], nums: List[int]) -> List[int]:
        n = len(parents)
        tree = [[] for _ in range(n)]
        for i, p in enumerate(parents):
            if p != -1:
                tree[p].append(i)

        res = [1] * n

        def dfs(node):
            if not tree[node]:
                if nums[node] == 1:
                    res[node] = 2
                return {nums[node]}, res[node]

            s = {nums[node]}
            pre = 1
            for child in tree[node]:
                a, b = dfs(child)
                s |= a
                pre = max(pre, b)
            while pre in s:
                pre += 1
            res[node] = pre
            return s, pre

        dfs(0)
        return res


def test_smallest_missing_value_subtree():
    solution = Solution()
    assert solution.smallestMissingValueSubtree([-1, 0, 0, 2], [1, 2, 3, 4]) == [5, 1, 1, 1], 'wrong result'
    assert solution.smallestMissingValueSubtree([-1, 0, 1, 0, 3, 3], [5, 4, 6, 2, 1, 3]) == [7, 1, 1, 4, 2, 1], 'wrong result'
    assert solution.smallestMissingValueSubtree([-1, 2, 3, 0, 2, 4, 1], [2, 3, 4, 5, 6, 7, 8]) == [1, 1, 1, 1, 1, 1, 1], 'wrong result'


if __name__ == '__main__':
    test_smallest_missing_value_subtree()
