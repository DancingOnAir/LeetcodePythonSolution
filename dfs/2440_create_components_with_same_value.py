from typing import List


class Solution:
    # 下面方法的优化版本
    def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:
        g = [[] for _ in nums]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        # post-order
        def dfs(u, p):
            res = nums[u]
            for v in g[u]:
                if v != p:
                    res += dfs(v, u)
            return 0 if res == cand else res

        total = sum(nums)
        for cand in range(max(nums), total // 2 + 1):
            if total % cand == 0 and dfs(0, -1) == 0:
                return total // cand - 1
        return 0

    # max(nums) 是最小能分割出的子树的值, 那么sum(nums) // max(nums) 就是最大能分割出的子树数量
    # 从sum(nums) // max(nums) 遍历到 0
    # dfs的思路，如果子树是符合target值的，那么可以将它视为值为0的连通块，连通其他子树
    def componentValue1(self, nums: List[int], edges: List[List[int]]) -> int:
        g = [[] for _ in nums]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        def dfs(node, pa):
            val = nums[node]
            for child in g[node]:
                if child != pa:
                    res = dfs(child, node)
                    if res < 0:
                        return -1
                    val += res
            if val > target:
                return -1
            return val if val < target else 0

        total = sum(nums)
        for i in range(total // max(nums), 1, -1):
            if total % i == 0:
                target = total // i
                if dfs(0, -1) == 0:
                    return i - 1
        return 0


def test_component_value():
    solution = Solution()
    assert solution.componentValue([6, 2, 2, 2, 6], [[0, 1], [1, 2], [1, 3], [3, 4]]) == 2, 'wrong result'
    assert solution.componentValue([2], []) == 0, 'wrong result'


if __name__ == '__main__':
    test_component_value()
