from typing import List
from collections import Counter, defaultdict


class Solution:
    # dfs + Counter without seen array
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        def dfs(node, parent):
            cnt = Counter(labels[node])
            for child in graph[node]:
                if child != parent:
                    cnt += dfs(child, node)
            res[node] = cnt[labels[node]]
            return cnt

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        res = [0] * n
        dfs(0, None)
        return res

    # postorder + Counter
    def countSubTrees1(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        res = [0] * n
        seen = [False] * n

        def postorder(node):
            if seen[node]:
                return Counter()

            seen[node] = True
            c = Counter()
            for child in graph[node]:
                if not seen[child]:
                    c += postorder(child)

            c += Counter(labels[node])
            res[node] = c[labels[node]]
            return c

        postorder(0)
        return res


def test_count_sub_trees():
    solution = Solution()
    assert solution.countSubTrees(7, [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]], "abaedcd") == [2, 1, 1, 1, 1, 1, 1], 'wrong result'
    assert solution.countSubTrees(4, [[0, 1], [1, 2], [0, 3]], "bbbb") == [4, 2, 1, 1], 'wrong result'
    assert solution.countSubTrees(5, [[0, 1], [0, 2], [1, 3], [0, 4]], "aabab") == [3, 2, 1, 1, 1], 'wrong result'


if __name__ == '__main__':
    test_count_sub_trees()
