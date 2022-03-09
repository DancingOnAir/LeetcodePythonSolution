from typing import List
from itertools import product


class Solution:
    def countCombinations(self, pieces: List[str], positions: List[List[int]]) -> int:
        def dfs(pos, dirs, stopped_mask):
            print(dirs)
            if stopped_mask == 0:
                return
            self.res.add(tuple(pos))
            for active in range(1 << len(dirs)):

            pass

        moves = dict()
        moves['rook'] = ((1, 0), (-1, 0), (0, 1), (0, -1))
        moves['queen'] = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1))
        moves['bishop'] = ((1, 1), (1, -1), (-1, 1), (-1, -1))

        positions = [tuple(p) for p in positions]
        self.res = set()
        for dirs in product(*(moves[p] for p in pieces)):
            dfs(positions, dirs, (1 << len(pieces)) - 1)
        return len(self.res)


def test_count_combinations():
    solution = Solution()
    assert solution.countCombinations(["rook"], [[1, 1]]) == 15, 'wrong result'
    assert solution.countCombinations(["queen"], [[1, 1]]) == 22, 'wrong result'
    assert solution.countCombinations(["bishop"], [[4, 3]]) == 12, 'wrong result'


if __name__ == '__main__':
    test_count_combinations()
