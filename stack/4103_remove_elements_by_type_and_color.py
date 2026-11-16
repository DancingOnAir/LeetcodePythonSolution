class Solution:
    def canRemoveAll(self, types: list[int], colors: list[int], groupSize: list[int]) -> bool:
        stk = []
        for t, c in zip(types, colors):
            if stk and stk[-1][0] == t and stk[-1][1] == c:
                stk[-1][2] += 1
            else:
                # type, color, cnt
                stk.append([t, c, 1])

            if groupSize[stk[-1][0]] == stk[-1][2]:
                stk.pop()

        return not stk


def test_can_remove_all():
    solution = Solution()
    assert solution.canRemoveAll([0,1,1,0], colors = [5,3,3,5] , groupSize = [2,2]), 'wrong result'
    assert not solution.canRemoveAll([0,1,0], colors = [9,9,9], groupSize = [3,2]), 'wrong result'
    assert not solution.canRemoveAll([2,0,1,2], colors = [7,5,4,7], groupSize = [3,1,2]), 'wrong result'


if __name__ == '__main__':
    test_can_remove_all()
