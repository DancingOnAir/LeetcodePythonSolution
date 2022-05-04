from typing import List
from collections import defaultdict, Counter


class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        tree = [[] for _ in parents]
        for i, x in enumerate(parents):
            if x >= 0:
                tree[x].append(i)

        freq = defaultdict(int)

        # 求以x为根节点的树的所有结点数
        def helper(x):
            left = right = 0
            if tree[x]:
                # 假定第一个是左子树
                left = helper(tree[x][0])
            if len(tree[x]) > 1:
                # 如果有第二个儿子，那么是右子树
                right = helper(tree[x][1])

            score = (left or 1) * (right or 1) * (len(parents) - 1 - left - right or 1)
            freq[score] += 1

            return left + right + 1

        helper(0)
        return freq[max(freq)]


def test_count_highest_score_nodes():
    solution = Solution()
    assert solution.countHighestScoreNodes([-1, 2, 0, 2, 0]) == 3, 'wrong result'
    assert solution.countHighestScoreNodes([-1, 2, 0]) == 2, 'wrong result'


if __name__ == '__main__':
    test_count_highest_score_nodes()
