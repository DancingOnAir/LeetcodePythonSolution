class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return '0'

        if k == (1 << n) // 2:
            return '1'
        elif k < (1 << n) // 2:
            return self.findKthBit(n - 1, k)
        else:
            return '1' if self.findKthBit(n - 1, (1 << n) - k) == '0' else '0'


def test_find_kth_bit():
    solution = Solution()
    assert solution.findKthBit(3, 5) == '0', 'wrong result'
    assert solution.findKthBit(3, 1) == '0', 'wrong result'
    assert solution.findKthBit(4, 11) == '1', 'wrong result'
    assert solution.findKthBit(1, 1) == '0', 'wrong result'
    assert solution.findKthBit(2, 3) == '1', 'wrong result'


if __name__ == '__main__':
    test_find_kth_bit()
