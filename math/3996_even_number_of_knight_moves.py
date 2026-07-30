class Solution:
    # 每次马跳的目的点坐标和出发点坐标马科夫距离为3，是个奇数。如果要跳到的最终点和起始点的马科夫距离为偶数，那么需要跳偶数次，否则为奇数次。
    def canReach(self, start: list[int], target: list[int]) -> bool:
        return (abs(target[0] - start[0]) + abs(target[1] - start[1])) % 2 == 0


def test_can_reach():
    solution = Solution()
    assert solution.canReach([1,1], target = [2,2]), 'wrong result'
    assert not solution.canReach([4,5], target = [6,6]), 'wrong result'


if __name__ == '__main__':
    test_can_reach()
