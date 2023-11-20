class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        res, l, cnt = len(blocks), 0, 0
        for r, ch in enumerate(blocks):
            if ch == 'W':
                cnt += 1
            if r - l + 1 == k:
                res = min(res, cnt)
                cnt -= blocks[l] == 'W'
                l += 1

        return res


def test_minimum_recolors():
    solution = Solution()
    assert solution.minimumRecolors("WBBWWBBWBW", 7) == 3, 'wrong result'
    assert solution.minimumRecolors("WBWBBBW", 2) == 0, 'wrong result'


if __name__ == '__main__':
    test_minimum_recolors()
