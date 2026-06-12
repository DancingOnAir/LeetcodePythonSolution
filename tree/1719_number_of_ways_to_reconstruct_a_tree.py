from typing import List
from collections import defaultdict


class Solution:
    # https://leetcode.cn/problems/number-of-ways-to-reconstruct-a-tree/solution/zhong-gou-yi-ke-shu-de-fang-an-shu-by-le-36e1/
    def checkWays(self, pairs: List[List[int]]) -> int:
        # 所有的节点的集合
        nodes = set()
        # degree[i]表示包含节点i的数目对的数量
        degree = defaultdict(int)
        # graph[i]表示节点i的所有祖先和后代的集合
        graph = defaultdict(set)
        for u, v in pairs:
            nodes |= {u, v}
            graph[u].add(v)
            graph[v].add(u)
            degree[u] += 1
            degree[v] += 1

        n = len(nodes)
        root = next((node for node, neighbours in graph.items() if len(neighbours) == n - 1), -1)
        if root == -1:
            return 0

        res = 1
        for node, neighbours in graph.items():
            if node == root:
                continue

            parent = -1
            parent_degree = float('inf')
            for neighbour in neighbours:
                # 找到degree大于degree[node]的节点为node祖先，其中最小值为node的父节点
                if degree[node] <= degree[neighbour] < parent_degree:
                    parent = neighbour
                    parent_degree = degree[neighbour]
            # 不存在这样的父节点或graph[node]不是graph[parent]的子集
            if parent == -1 or any(neighbour != parent and neighbour not in graph[parent] for neighbour in neighbours):
                return 0
            # 上面判断过已经是有效的父节点，并且这里满足数目对数量一致，那么父节点只有1个孩子node，可以互相交换
            if degree[node] == parent_degree:
                res = 2
        return res

    # https://leetcode.com/problems/number-of-ways-to-reconstruct-a-tree/discuss/1009238/Python-dfs-solution-explained
    def checkWays1(self, pairs: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in pairs:
            graph[u].append(v)
            graph[v].append(u)

        def helper(nodes):
            d = defaultdict(list)
            m = len(nodes) - 1
            for node in nodes:
                d[len(graph[node])].append(node)

            if len(d[m]) == 0:
                return 0
            root = d[m][0]

            for node in graph[root]:
                graph[node].remove(root)

            comps, seen, i = defaultdict(set), set(), 0
            def dfs(node, i):
                comps[i].add(node)
                seen.add(node)
                for nei in graph[node]:
                    if nei not in seen:
                        dfs(nei, i)

            for node in nodes:
                if node != root and node not in seen:
                    dfs(node, i)
                    i += 1

            candidates = [helper(val) for val in comps.values()]
            if 0 in candidates:
                return 0
            if 2 in candidates:
                return 2
            if len(d[m]) >= 2:
                return 2
            return 1

        return helper(set(graph.keys()))


def test_check_ways():
    solution = Solution()
    assert solution.checkWays([[3, 5], [4, 5], [2, 5], [1, 5], [1, 4], [2, 4]]) == 1, 'wrong result'
    assert solution.checkWays([[1, 2], [2, 3]]) == 1, 'wrong result'
    assert solution.checkWays([[1, 2], [2, 3], [1, 3]]) == 2, 'wrong result'
    assert solution.checkWays([[1, 2], [2, 3], [2, 4], [1, 5]]) == 0, 'wrong result'


if __name__ == '__main__':
    test_check_ways()
