from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        d = {"--X": -1, "X--": -1, "++X": 1, "X++": 1}
        res = 0
        for op in operations:
            res += d[op]
        return res


def test_final_value_after_operations():
    solution = Solution()

    assert solution.finalValueAfterOperations(["--X", "X++", "X++"]) == 1
    assert solution.finalValueAfterOperations(["++X", "++X", "X++"]) == 3
    assert solution.finalValueAfterOperations(["X++", "++X", "--X", "X--"]) == 0


if __name__ == '__main__':
    test_final_value_after_operations()
