from itertools import groupby


class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        res = 0
        for i in range(1, len(colors) - 1):
            if colors[i - 1] == colors[i] == colors[i + 1]:
                if colors[i] == 'A':
                    res += 1
                else:
                    res -= 1
        return res > 0

    def winnerOfGame1(self, colors: str) -> bool:
        group = [(k, len(list(v))) for k, v in groupby(colors)]

        res = 0
        for g in group:
            if g[0] == 'A' and g[1] > 2:
                res += g[1] - 2
            elif g[0] == 'B' and g[1] > 2:
                res -= g[1] - 2

        return res > 0


def test_winner_of_game():
    solution = Solution()
    assert solution.winnerOfGame('AAABABB'), 'wrong result'
    assert not solution.winnerOfGame('AA'), 'wrong result'
    assert not solution.winnerOfGame('ABBBBBBBAAA'), 'wrong result'


if __name__ == '__main__':
    test_winner_of_game()
