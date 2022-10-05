from typing import List


class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        pass


def test_match_players_and_trainers():
    solution = Solution()
    assert solution.matchPlayersAndTrainers([4, 7, 9], [8, 2, 5, 8]) == 2, 'wrong result'
    assert solution.matchPlayersAndTrainers([1, 1, 1], [10]) == 1, 'wrong result'


if __name__ == '__main__':
    test_match_players_and_trainers()

