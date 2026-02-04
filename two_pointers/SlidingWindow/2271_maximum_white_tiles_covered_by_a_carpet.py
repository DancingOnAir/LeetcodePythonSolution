from typing import List


class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort()
        res = left = cover = 0
        for right in range(len(tiles)):
            cover += tiles[right][1] - tiles[right][0] + 1
            while tiles[left][1] < tiles[right][1] - carpetLen + 1:
                cover -= tiles[left][1] - tiles[left][0] + 1
                left += 1

            uncover = max(0, tiles[right][1] - carpetLen + 1 - tiles[left][0])
            res = max(res, cover - uncover)
        return res


def test_maximum_white_tiles():
    solution = Solution()
    assert solution.maximumWhiteTiles([[1, 5], [10, 11], [12, 18], [20, 25], [30, 32]], 10) == 9, 'wrong result'
    assert solution.maximumWhiteTiles([[10, 11], [1, 1]], 2) == 2, 'wrong result'


if __name__ == '__main__':
    test_maximum_white_tiles()
