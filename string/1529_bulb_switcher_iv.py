from itertools import groupby


class Solution:
    def minFlips(self, target: str) -> int:
        res = 2 * target.count('10')
        if target[-1] == '1':
            res += 1
        return res

    def minFlips2(self, target: str) -> int:
        return len(list(groupby('0' + target))) - 1

    def minFlips1(self, target: str) -> int:
        res = flip = 0
        for c in target:
            if flip ^ int(c):
                flip ^= 1
                res += 1

        return res


def test_min_filps():
    solution = Solution()
    assert solution.minFlips('10111') == 3, 'wrong result'
    assert solution.minFlips('101') == 3, 'wrong result'
    assert solution.minFlips('00000') == 0, 'wrong result'
    assert solution.minFlips('001011101') == 5, 'wrong result'


if __name__ == '__main__':
    test_min_filps()
