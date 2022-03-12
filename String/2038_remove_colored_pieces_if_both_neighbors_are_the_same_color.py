from itertools import groupby


class Solution:
    def winnerOfGame(self, colors: str) -> bool:
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
