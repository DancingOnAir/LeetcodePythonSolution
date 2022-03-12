from typing import List
from itertools import product, chain
from collections import Counter


class Solution:
    # https://leetcode.com/problems/number-of-valid-move-combinations-on-chessboard/discuss/1549465/If-you-are-confused-by-the-description...
    def countCombinations(self, pieces: List[str], positions: List[List[int]]) -> int:
        def valid(x, y):
            return 0 <= x < 8 and 0 <= y < 8

        def fill(i, x, y, dirs):
            for dir in dirs:
                nx, ny = x + dir[0], y + dir[1]
                t = 1

                while valid(nx, ny):
                    self.moves[i].append([dir[0], dir[1], t])
                    nx += dir[0]
                    ny += dir[1]
                    t += 1

        def check(pos1, new_pos1, pos2, new_pos2):
            t1 = new_pos1[-1]
            t2 = new_pos2[-1]
            for i in range(1, max(t1, t2) + 1):
                if i <= t1:
                    pos1[0] += new_pos1[0]
                    pos1[1] += new_pos1[1]

                if i <= t2:
                    pos2[0] += new_pos2[0]
                    pos2[1] += new_pos2[1]

                if pos1 == pos2:
                    return False
            return True

        def dfs(cur, new_pos, pos):
            if cur >= len(self.moves):
                self.res += 1
                return

            for m in self.moves[cur]:
                ok = True
                for i in range(len(new_pos)):
                    if not check(pos[i], new_pos[i], pos[cur], m):
                        ok = False
                        break

                if not ok:
                    continue

                new_pos.append(m)
                dfs(cur + 1, new_pos, pos)
                new_pos.pop()

        direction_line = ((0, 1), (1, 0), (0, -1), (-1, 0))
        direction_diagonal = ((1, 1), (-1, 1), (-1, -1), (1, -1))
        n = len(pieces)
        self.moves = [[] for _ in range(n)]

        for p in positions:
            p[0] -= 1
            p[1] -= 1

        for i in range(n):
            x, y = positions[i][0], positions[i][1]
            self.moves[i].append([0, 0, 0])

            if pieces[i] == 'rook':
                fill(i, x, y, direction_line)
            elif pieces[i] == 'bishop':
                fill(i, x, y, direction_diagonal)
            else:
                fill(i, x, y, direction_line)
                fill(i, x, y, direction_diagonal)

        new_pos = list()
        self.res = 0
        dfs(0, new_pos, positions)
        return self.res

    def countCombinations1(self, pieces: List[str], positions: List[List[int]]) -> int:
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
