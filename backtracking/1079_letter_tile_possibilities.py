from collections import Counter


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        c = Counter(tiles)

        def dfs(i):
            if i == 0:
                return 1

            res = 1
            for ch in c:
                if c[ch] > 0:
                    c[ch] -= 1
                    res += dfs(i - 1)
                    c[ch] += 1
            return res

        return dfs(len(tiles)) - 1


def test_num_tile_possibilities():
    solution = Solution()
    assert solution.numTilePossibilities("AAB") == 8, 'wrong result'
    assert solution.numTilePossibilities("AAABBC") == 188, 'wrong result'
    assert solution.numTilePossibilities("V") == 1, 'wrong result'


if __name__ == '__main__':
    test_num_tile_possibilities()
