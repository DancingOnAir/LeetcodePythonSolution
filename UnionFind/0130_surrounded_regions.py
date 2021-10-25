class Solution:
    def solve(self, board: List[List[str]]) -> None:
        pass


def test_solve():
    solution = Solution()

    assert solution.solve([["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]) == [
        ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "O", "X", "X"]], 'wrong result'


if __name__ == '__main__':
    test_solve()
