class Solution:
    def judgeCircle(self, moves: str) -> bool:
        res = [0, 0]
        for move in moves:
            if move == 'U':
                res[0] += 1
            elif move == 'D':
                res[0] -= 1
            elif move == 'L':
                res[1] += 1
            else:
                res[1] -= 1
        return res[0] == res[1] == 0


def test_judge_circle():
    solution = Solution()
    assert solution.judgeCircle("UD"), 'wrong result'
    assert not solution.judgeCircle("LL"), 'wrong result'


if __name__ == '__main__':
    test_judge_circle()
