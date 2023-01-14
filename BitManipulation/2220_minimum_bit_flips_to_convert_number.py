class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # return sum(int(x) ^ int(y) for x, y in zip(bin(start)[2:], bin(goal)[2:]))
        res = 0
        a = bin(start)[2:]
        b = bin(goal)[2:]
        if len(a) > len(b):
            b = '0' * (len(a) - len(b)) + b
        elif len(a) < len(b):
            a = '0' * (len(b) - len(a)) + a
        for x, y in zip(a, b):
            res += (int(x) ^ int(y))
        return res


def test_min_bit_flips():
    solution = Solution()
    assert solution.minBitFlips(10, 7) == 3, 'wrong result'
    assert solution.minBitFlips(3, 4) == 3, 'wrong result'


if __name__ == '__main__':
    test_min_bit_flips()
