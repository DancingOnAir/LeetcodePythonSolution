from typing import List
from math import comb
from collections import defaultdict


class Solution:
    def waysToBuildRooms(self, prevRoom: List[int]) -> int:
        connect = defaultdict(list)
        for i, num in enumerate(prevRoom):
            connect[num].append(i)

        def dfs(idx):
            nodes, res = 0, 1
            for sub_nodes in connect[idx]:
                nodes_, res_ = dfs(sub_nodes)
                nodes += nodes_
                res = (res * comb(nodes, nodes_) * res_) % (10 ** 9 + 7)
            return nodes + 1, res
        return dfs(0)[1]


def test_ways_to_build_rooms():
    solution = Solution()
    assert solution.waysToBuildRooms([-1, 0, 1]) == 1, 'wrong result'
    assert solution.waysToBuildRooms([-1, 0, 0, 1, 2]) == 6, 'wrong result'


if __name__ == '__main__':
    test_ways_to_build_rooms()
