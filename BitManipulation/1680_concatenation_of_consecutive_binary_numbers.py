class Solution:
    def concatenatedBinary(self, n: int) -> int:
        return int(''.join(bin(x)[2:] for x in range(1, n+1)), 2) % (10 ** 9 + 7)


def test_concatenated_binary():
    solution = Solution()
    assert solution.concatenatedBinary(1) == 1, 'wrong result'
    assert solution.concatenatedBinary(3) == 27, 'wrong result'
    assert solution.concatenatedBinary(12) == 505379714, 'wrong result'


if __name__ == '__main__':
    test_concatenated_binary()
