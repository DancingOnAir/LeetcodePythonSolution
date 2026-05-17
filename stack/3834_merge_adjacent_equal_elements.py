class Solution:
    def mergeAdjacent(self, nums: list[int]) -> list[int]:
        stk = []
        for x in nums:
            while stk and stk[-1] == x:
                x += stk.pop()
            stk.append(x)
        return stk


def test_merge_adjacent():
    solution = Solution()
    assert solution.mergeAdjacent([3, 1, 1, 2]) == [3, 4], 'wrong result'
    assert solution.mergeAdjacent([2, 2, 4]) == [8], 'wrong result'
    assert solution.mergeAdjacent([3, 7, 5]) == [3, 7, 5], 'wrong result'


if __name__ == '__main__':
    test_merge_adjacent()
