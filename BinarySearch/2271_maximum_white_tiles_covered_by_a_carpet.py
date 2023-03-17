from typing import List


class Solution:
    # sliding window
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort()
        res = cover = i = j = 0
        while i < len(tiles) and res < carpetLen:
            if tiles[j][0] + carpetLen > tiles[i][1]:
                cover += tiles[i][1] - tiles[i][0] + 1
                res = max(res, cover)
                i += 1
            else:
                partial = max(0, tiles[j][0] + carpetLen - tiles[i][0])
                res = max(res, cover + partial)
                cover -= tiles[j][1] - tiles[j][0] + 1
                j += 1
        return res


def test_maximum_white_tiles():
    solution = Solution()
    assert solution.maximumWhiteTiles([[1, 5], [10, 11], [12, 18], [20, 25], [30, 32]], 10) == 9, 'wrong result'
    assert solution.maximumWhiteTiles([[10, 11], [1, 1]], 2) == 2, 'wrong result'


if __name__ == '__main__':
    test_maximum_white_tiles()
