from typing import List
from math import log2


class TreeAncestor:
    # self.dp[][] whose i, jth element indicates the ith node's 2^j
    def __init__(self, n: int, parent: List[int]):
        depth = 1 + int(log2(n))
        self.dp = [[-1] * depth for _ in range(n)]
        for j in range(n):
            for i in range(depth):
                if j == 0:
                    self.dp[i][0] = parent[i]
                elif self.dp[i][j - 1] != -1:
                    self.dp[i][j] = self.dp[self.dp[i][j - 1]][j - 1]

    def getKthAncestor(self, node: int, k: int) -> int:
        while k > 0 and node != -1:
            i = int(log2(k))
            node = self.dp[node][i]
            k -= (1 << i)
        return node


# Your TreeAncestor object will be instantiated and called as such:
def test_tree_ancestor():
    obj = TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2])
    assert obj.getKthAncestor(3, 1) == 1, 'wrong result'
    assert obj.getKthAncestor(5, 2) == 0, 'wrong result'
    assert obj.getKthAncestor(6, 3) == -1, 'wrong result'