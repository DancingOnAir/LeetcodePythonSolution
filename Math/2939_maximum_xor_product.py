class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        if a < b:
            a, b = b, a
        mask = (1 << n) - 1
        ax = a & ~mask
        bx = b & ~mask
        a = a & mask
        b = b & mask

        left = a ^ b
        one = mask ^ left
        ax |= one
        bx |= one

        if left > 0 and ax == bx:
            high_bit = 1 << (left.bit_length() - 1)
            ax |= high_bit
            left ^= high_bit
        bx |= left
        return ax * bx % (10 ** 9 + 7)


def test_maximum_xor_product():
    solution = Solution()
    assert solution.maximumXorProduct(12, 5, 4) == 98, 'wrong result'
    assert solution.maximumXorProduct(6, 7, 5) == 930, 'wrong result'
    assert solution.maximumXorProduct(1, 6, 3) == 12, 'wrong result'


if __name__ == '__main__':
    test_maximum_xor_product()
