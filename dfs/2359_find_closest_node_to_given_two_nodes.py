from typing import List


class Solution:
    # 这个题目的意思是找到1个点，node1, node2都能到这个点，到达的距离为d1, d2, 使max(d1, d2)的值最小
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n, min_dis, res = len(edges), len(edges), -1

        def dfs(x):
            dis = [n] * n
            depth = 0
            while x >= 0 and dis[x] == n:
                dis[x] = depth
                depth += 1
                x = edges[x]
            return dis

        for i, d in enumerate(map(max, zip(dfs(node1), dfs(node2)))):
            if d < min_dis:
                res, min_dis = i, d
        return res


def test_closest_meeting_node():
    solution = Solution()
    assert solution.closestMeetingNode([4, 4, 8, -1, 9, 8, 4, 4, 1, 1], 5, 6) == 1, 'wrong result'
    assert solution.closestMeetingNode([4, 3, 0, 5, 3, -1], 4, 0) == 4, 'wrong result'
    assert solution.closestMeetingNode([2, 2, 3, -1], 0, 1) == 2, 'wrong result'
    assert solution.closestMeetingNode([1, 2, -1], 0, 2) == 2, 'wrong result'


if __name__ == '__main__':
    test_closest_meeting_node()
