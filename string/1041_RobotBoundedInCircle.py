class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y, dx, dy = 0, 0, 0, 1
        for i in instructions:
            if i == 'R':
                dx, dy = dy, -dx
            elif i == 'L':
                dx, dy = -dy, dx
            else:
                x, y = x + dx, y + dy
        return (x, y) == (0, 0) or (dx, dy) != (0, 1)

    def isRobotBounded1(self, instructions: str) -> bool:
        pos = [0, 0]
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        direction_idx = 0
        for i in instructions:
            if i == 'G':
                pos[0] += direction[direction_idx][0]
                pos[1] += direction[direction_idx][1]
            elif i == 'L':
                direction_idx -= 1
            elif i == 'R':
                direction_idx += 1

            direction_idx %= 4

        if pos == [0, 0] or direction_idx != 0:
            return True
        return False


def test_is_robot_bounded():
    solution = Solution()

    assert solution.isRobotBounded("RLLGLRRRRGGRRRGLLRRR"), 'wrong result'
    assert not solution.isRobotBounded("GLGLGGLGL"), 'wrong result'
    assert solution.isRobotBounded("GGLLGG"), 'wrong result'
    assert not solution.isRobotBounded("GG"), 'wrong result'
    assert solution.isRobotBounded("GL"), 'wrong result'


if __name__ == '__main__':
    test_is_robot_bounded()
