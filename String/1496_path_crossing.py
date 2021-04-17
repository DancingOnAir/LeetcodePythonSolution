from operator import add


class Solution:
    # math the coordinate is represented by a complex number x + yj
    def isPathCrossing(self, path: str) -> bool:
        dir = {'N': 1j, 'S': -1j, 'E': 1, 'W': -1}
        cur = 0
        memo = {0}

        for c in path:
            cur += dir[c]
            if cur in memo:
                return True
            memo.add(cur)
        return False


    def isPathCrossing2(self, path: str) -> bool:
        cur = (0, 0)
        dir = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}
        memo = {cur}
        for c in path:
            cur = tuple(map(add, cur, dir[c]))
            if cur in memo:
                return True
            memo.add(cur)
        return False


    def isPathCrossing1(self, path: str) -> bool:
        origin = [0, 0]
        memo = {(0, 0)}

        for i, c in enumerate(path):
            if c == 'N':
                origin[1] += 1
            elif c == 'S':
                origin[1] -= 1
            elif c == 'E':
                origin[0] += 1
            else:
                origin[0] -= 1

            if tuple(origin) in memo:
                return True
            memo.add(tuple(origin))

        return False


def test_is_path_crossing():
    solution = Solution()
    # assert not solution.isPathCrossing('NES'), 'wrong result'
    assert solution.isPathCrossing('NESWW'), 'wrong result'


if __name__ == '__main__':
    test_is_path_crossing()
