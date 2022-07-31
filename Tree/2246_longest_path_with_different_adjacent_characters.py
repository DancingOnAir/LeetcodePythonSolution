from typing import List
from heapq import nlargest
from collections import deque
from bisect import insort_right


class Solution:
    # bfs
    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(parent)
        child_num = [0] * n
        for p in parent[1:]:
            child_num[p] += 1
        # the longest chain with node i as parent
        longest = [[0] for _ in range(n)]
        # add all the leaf nodes into deque: [current node, the maximum length end by this node]
        dq = deque()
        for i in range(n):
            if not child_num[i]:
                dq.append((i, 1))

        res = 1
        while dq:
            cur_node, cur_len = dq.popleft()
            cur_parent = parent[cur_node]

            child_num[cur_parent] -= 1
            if s[cur_node] != s[cur_parent]:
                insort_right(longest[cur_parent], cur_len)
                if len(longest[cur_parent]) > 2:
                    longest[cur_parent].pop(0)

            if child_num[cur_parent] == 0:
                res = max(res, 1 + sum(longest[cur_parent][-2:]))
                dq.append([cur_parent, 1 + longest[cur_parent][-1]])

        return res

    # improved dfs
    def longestPath2(self, parent: List[int], s: str) -> int:
        n = len(parent)
        tree = [[] for _ in range(n)]
        for i, p in enumerate(parent):
            if p != -1:
                tree[p].append(i)

        def dfs(i):
            nonlocal res
            candidates = [0]
            for child in tree[i]:
                # 必须先计算子节点，再判断父节点和子节点字符是否一样，因为子树里也可能有最长的chain
                cur = dfs(child)
                if s[i] != s[child]:
                    candidates.append(cur)

            candidates = nlargest(2, candidates)
            res = max(res, sum(candidates) + 1)
            return max(candidates) + 1

        res = 0
        dfs(0)
        return res

    # dfs
    def longestPath1(self, parent: List[int], s: str) -> int:
        n = len(parent)
        tree = [[] for _ in range(n)]
        for i in range(1, n):
            tree[parent[i]].append(i)

        def dfs(i: int) -> int:
            nonlocal res
            max_len = 0
            for j in tree[i]:
                # 获取子树的最长边，此外还要加上i到j的边
                cur_len = dfs(j) + 1
                if s[i] != s[j]:
                    res = max(res, max_len + cur_len)
                    max_len = max(max_len, cur_len)
            return max_len

        res = 0
        dfs(0)
        # 计算的是节点，dfs计算的是边
        return res + 1


def test_longest_path():
    solution = Solution()
    assert solution.longestPath([-1, 0, 0, 1, 1, 2], "abacbe") == 3, 'wrong result'
    assert solution.longestPath([-1, 0, 0, 0], "aabc") == 3, 'wrong result'


if __name__ == '__main__':
    test_longest_path()
