class Solution:
    def isPathCrossing(self, path: str) -> bool:
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
