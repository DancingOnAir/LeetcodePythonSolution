from typing import List


class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        res = list()
        for r in range(ord(s[0]), ord(s[3]) + 1):
            for c in range(int(s[1]), int(s[4]) + 1):
                res.append(chr(r)+str(c))
        return res


def test_cells_in_range():
    solution = Solution()
    assert solution.cellsInRange("K1:L2") == ["K1","K2","L1","L2"], 'wrong result'
    assert solution.cellsInRange("A1:F1") == ["A1","B1","C1","D1","E1","F1"], 'wrong result'


if __name__ == '__main__':
    test_cells_in_range()
