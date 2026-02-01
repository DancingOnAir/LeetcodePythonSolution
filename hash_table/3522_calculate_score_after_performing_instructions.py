from typing import List


class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        seen = set()
        res = i = 0
        while 0 <= i < len(instructions):
            if i in seen:
                break
            seen.add(i)
            if instructions[i] == 'add':
                res += values[i]
                i += 1
            else:
                i += values[i]

        return res


def test_calculate_score():
    solution = Solution()
    assert solution.calculateScore(["jump", "add", "add", "jump", "add", "jump"], [2, 1, 3, 1, -2, -3]) == 1, 'wrong result'
    assert solution.calculateScore(["jump", "add", "add"], [3, 1, 1]) == 0, 'wrong result'
    assert solution.calculateScore(["jump"], [0]) == 0, 'wrong result'


if __name__ == '__main__':
    test_calculate_score()
