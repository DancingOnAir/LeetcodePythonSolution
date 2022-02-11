from typing import List


class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        def get_num_instruction(s):
            # x, y
            moves = [0, 0]
            for i, ch in enumerate(s):
                if ch == 'R':
                    moves[0] += 1
                elif ch == 'L':
                    moves[0] -= 1
                elif ch == 'U':
                    moves[1] += 1
                else:
                    moves[1] -= 1

                if (moves[0] > 0 and moves[0] > limits[0]) or (moves[0] < 0 and abs(moves[0]) > limits[2]) or (moves[1] > 0 and moves[1] > limits[3]) or (moves[1] < 0 and abs(moves[1]) > limits[1]):
                    return i

            return len(s)
        # RDLU
        limits = [n - 1 - startPos[1], n - 1 - startPos[0], startPos[1], startPos[0]]
        res = list()
        for i in range(len(s)):
            res.append(get_num_instruction(s[i:]))
        return res


def test_execute_instructions():
    solution = Solution()
    assert solution.executeInstructions(3, [0, 1], 'RRDDLU') == [1, 5, 4, 3, 1, 0], 'wrong result'
    assert solution.executeInstructions(2, [1, 1], 'LURD') == [4, 1, 0, 0], 'wrong result'
    assert solution.executeInstructions(1, [0, 0], 'LRUD') == [0, 0, 0, 0], 'wrong result'


if __name__ == '__main__':
    test_execute_instructions()
