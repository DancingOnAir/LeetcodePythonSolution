class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        return ["." + "#" * (n - 1)] * (m - 1) + ["." * n]


def test_create_grid():
    solution = Solution()
    assert solution.createGrid(2, 3)[0][0] == '.', 'wrong result'


if __name__ == '__main__':
    test_create_grid()
