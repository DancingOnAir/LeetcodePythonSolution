class Solution:
    def isRectangleOverlap(self, rec1: list[int], rec2: list[int]) -> bool:
        return not (rec1[0] >= rec2[2] or rec1[1] >= rec2[3] or rec1[2] <= rec2[0] or rec1[3] <= rec2[1])


def test_is_rectangle_overlap():
    solution = Solution()
    assert solution.isRectangleOverlap([0, 0, 2, 2], rec2=[1, 1, 3, 3]), 'wrong result'
    assert not solution.isRectangleOverlap([0, 0, 1, 1], rec2=[1, 0, 2, 1]), 'wrong result'
    assert not solution.isRectangleOverlap([0, 0, 1, 1], rec2=[2, 2, 3, 3]), 'wrong result'


if __name__ == '__main__':
    test_is_rectangle_overlap()
