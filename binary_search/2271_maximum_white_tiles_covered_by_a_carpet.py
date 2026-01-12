from typing import List
from bisect import bisect_right


class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort(key=lambda x: x[0])
        start_pos = [s for s, _ in tiles]
        pre_sum = [0]
        for i in range(1, len(tiles) + 1):
            pre_sum.append(pre_sum[-1] + (tiles[i - 1][1] - tiles[i - 1][0] + 1))

        res = 0
        for i in range(len(tiles)):
            s, e = tiles[i]
            if e >= s + carpetLen - 1:
                return carpetLen

            cur = bisect_right(start_pos, s + carpetLen - 1) - 1
            compensate = 0
            if tiles[cur][1] > s + carpetLen - 1:
                compensate = tiles[cur][1] - s - carpetLen + 1
            res = max(res, pre_sum[cur + 1] - pre_sum[i] - compensate)
        return res

    # sliding window
    def maximumWhiteTiles1(self, tiles: List[List[int]], carpetLen: int) -> int:
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
