class Solution:
    def maxBuilding(self, n: int, restrictions: list[list[int]]) -> int:
        restrictions += [[1, 0], [n, float('inf')]]
        restrictions.sort(key=lambda x: x[0])

        m = len(restrictions)
        h = [0] * m
        for i in range(1, m):
            h[i] = min(h[i-1] + restrictions[i][0] - restrictions[i-1][0], restrictions[i][1])
        for i in range(m - 2, -1, -1):
            h[i] = min(h[i], h[i + 1] + restrictions[i + 1][0] - restrictions[i][0])
        return max(restrictions[i + 1][0] - restrictions[i][0] + h[i] + h[i + 1] for i in range(m - 1)) // 2


def test_max_building():
    solution = Solution()
    assert solution.maxBuilding(5, restrictions = [[2,1],[4,1]]) == 2, 'wrong result'
    assert solution.maxBuilding(6, restrictions = []) == 5, 'wrong result'
    assert solution.maxBuilding(10, restrictions = [[5,3],[2,5],[7,4],[10,3]]) == 5, 'wrong result'


if __name__ == '__main__':
    test_max_building()
