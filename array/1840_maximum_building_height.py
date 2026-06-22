class Solution:
    def maxBuilding(self, n: int, restrictions: list[list[int]]) -> int:
        res = 0
        return res


def test_max_building():
    solution = Solution()
    assert solution.maxBuilding(5, restrictions = [[2,1],[4,1]])==2, 'wrong result'
    assert solution.maxBuilding(6, restrictions = [])==5, 'wrong result'
    assert solution.maxBuilding(10, restrictions = [[5,3],[2,5],[7,4],[10,3]])==5, 'wrong result'


if __name__ == '__main__':
    test_max_building()

