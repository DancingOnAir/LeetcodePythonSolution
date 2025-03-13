from typing import List


class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        g = [0] * len(edges)
        for i, x in enumerate(edges):
            g[x] += i
        # return sorted((-x, i) for i, x in enumerate(g))[0][1]
        return g.index((max(g)))


def test_edge_score():
    solution = Solution()
    assert solution.edgeScore([1, 0, 0, 0, 0, 7, 7, 5]) == 7, 'wrong result'
    assert solution.edgeScore([2, 0, 0, 2]) == 0, 'wrong result'


if __name__ == '__main__':
    test_edge_score()
