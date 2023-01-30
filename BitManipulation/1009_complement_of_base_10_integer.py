class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return (1 << (len(bin(n)) - 2)) - n - 1


def test_bitwise_complement():
    solution = Solution()
    assert solution.bitwiseComplement(5) == 2, 'wrong result'
    assert solution.bitwiseComplement(7) == 0, 'wrong result'
    assert solution.bitwiseComplement(10) == 5, 'wrong result'


if __name__ == '__main__':
    test_bitwise_complement()
