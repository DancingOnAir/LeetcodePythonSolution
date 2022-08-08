from typing import List


class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        def changes(cells):
            res = [0] * len(cells)
            for i in range(1, len(cells) - 1):
                if cells[i - 1] == cells[i + 1]:
                    res[i] = 1
            return res

        seen = dict()
        i = 0
        while n:
            cells = changes(cells)
            n -= 1

            if cells in seen.values():
                repeat = len(seen)
                n %= repeat
                return seen[n]
            seen[i] = cells
            i += 1

        return cells


def test_prison_after_n_days():
    solution = Solution()
    assert solution.prisonAfterNDays([0, 1, 0, 1, 1, 0, 0, 1], 7) == [0, 0, 1, 1, 0, 0, 0, 0], 'wrong result'
    assert solution.prisonAfterNDays([1, 0, 0, 1, 0, 0, 1, 0], 1000000000) == [0, 0, 1, 1, 1, 1, 1, 0], 'wrong result'


if __name__ == '__main__':
    test_prison_after_n_days()
