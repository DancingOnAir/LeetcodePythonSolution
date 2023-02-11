class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        return bin((a | b) ^ c).count('1') + bin(a & b & ((a | b) ^ c)).count('1')

    def minFlips2(self, a: int, b: int, c: int) -> int:
        ab, s, res = a | b, (a | b) ^ c, 0
        for i in range(31):
            mask = 1 << i
            if s & mask > 0:
                res += 2 if (a & mask) == (b & mask) and (c & mask) == 0 else 1

        return res

    def minFlips1(self, a: int, b: int, c: int) -> int:
        s = bin(((a | b) ^ c))[2:][::-1]
        res = 0
        for i, v in enumerate(s):
            if v == '1':
                if (c & (1 << i)) > 0:
                    res += 1
                else:
                    if (a & (1 << i)) > 0:
                        res += 1
                    if (b & (1 << i)) > 0:
                        res += 1
        return res


def test_min_flips():
    solution = Solution()
    assert solution.minFlips(10, 9, 1) == 3, 'wrong result'
    assert solution.minFlips(2, 6, 5) == 3, 'wrong result'
    assert solution.minFlips(4, 2, 7) == 1, 'wrong result'
    assert solution.minFlips(1, 2, 3) == 0, 'wrong result'


if __name__ == '__main__':
    test_min_flips()
