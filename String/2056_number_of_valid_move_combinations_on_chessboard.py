from typing import List
from itertools import product, chain
from collections import Counter


class Solution:
    def countCombinations(self, pieces: List[str], positions: List[List[int]]) -> int:
        def dfs(pos, dirs, stopped_mask):
            if stopped_mask == 0:
                return
            self.res.add(tuple(pos))
            for active in range(1 << len(dirs)):
                if stopped_mask & active != active:
                    continue
                new_pos = list(pos)
                new_mask = stopped_mask ^ active

                for i in range(len(new_pos)):
                    new_pos[i] = (new_pos[i][0] + dirs[i][0] * ((new_mask >> i) & 1), new_pos[i][1] + dirs[i][1] * ((new_mask >> i) & 1))

                if len(Counter(new_pos)) < len(dirs):
                    continue

                all_c = list(chain(*new_pos))
                # check whether new pos is out of board
                if min(all_c) <= 0 or max(all_c) > 8:
                    continue
                dfs(new_pos, dirs, new_mask)

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
