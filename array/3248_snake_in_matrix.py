from typing import List


class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        res = 0
        for d in commands:
            if d == "UP":
                res -= n
            elif d == "DOWN":
                res += n
            elif d == "LEFT":
                res -= 1
            else:
                res += 1
        return res


def test_final_position_of_snake():
    solution = Solution()
    assert solution.finalPositionOfSnake(2, ["RIGHT", "DOWN"]) == 3, 'wrong result'
    assert solution.finalPositionOfSnake(3, ["DOWN", "RIGHT", "UP"]) == 1, 'wrong result'


if __name__ == '__main__':
    test_final_position_of_snake()
