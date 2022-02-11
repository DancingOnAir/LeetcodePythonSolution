from typing import List


class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        return [1, 5, 4, 3, 1, 0]


def test_execute_instructions():
    solution = Solution()
    assert solution.executeInstructions(3, [0, 1], 'RRDDLU') == [1, 5, 4, 3, 1, 0], 'wrong result'
    assert solution.executeInstructions(2, [1, 1], 'LURD') == [4, 1, 0, 0], 'wrong result'
    assert solution.executeInstructions(1, [0, 0], 'LRUD') == [0, 0, 0, 0], 'wrong result'


if __name__ == '__main__':
    test_execute_instructions()
