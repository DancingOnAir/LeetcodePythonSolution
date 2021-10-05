class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        pass


def test_num_tile_possibilities():
    solution = Solution()

    assert solution.numTilePossibilities("AAB") == 8, 'wrong result'
    assert solution.numTilePossibilities("AAABBC") == 188, 'wrong result'
    assert solution.numTilePossibilities("V") == 1, 'wrong result'


if __name__ == '__main__':
    test_num_tile_possibilities()
