from typing import List


class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        return max(int(s) if s.isdigit() else len(s) for s in strs)

    def maximumValue1(self, strs: List[str]) -> int:
        res = 0
        for s in strs:
            if s.isdigit():
                res = max(res, int(s))
            else:
                res = max(res, len(s))
        return res


def test_maximum_value():
    solution = Solution()
    assert solution.maximumValue(["alic3", "bob", "3", "4", "00000"]) == 5, 'wrong result'
    assert solution.maximumValue(["1", "01", "001", "0001"]) == 1, 'wrong result'


if __name__ == '__main__':
    test_maximum_value()
