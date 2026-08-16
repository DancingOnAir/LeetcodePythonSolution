class Solution:
    def weightedSum(self, parent: list[int], nums: list[int]) -> int:
        n = len(parent)
        depth = [-1] * n
        depth[0] = 1

        def get_depth(node: int) -> int:
            if depth[node] != -1:
                return depth[node]
            depth[node] = get_depth(parent[node]) + 1
            return depth[node]

        # 计算所有节点的深度
        for i in range(n):
            get_depth(i)

        h = max(depth)

        res = 0
        for i, x in enumerate(nums):
            res += x * (h - depth[i] + 1)
        return res


def test_weighted_sum():
    solution = Solution()
    assert solution.weightedSum([-1, 0, 0, 0, 2, 2], nums=[5, 2, 3, 1, 4, 6]) == 37, 'wrong result'
    assert solution.weightedSum([-1, 0, 1, 2], nums=[1, 2, 3, 4]) == 20, 'wrong result'


if __name__ == '__main__':
    test_weighted_sum()
