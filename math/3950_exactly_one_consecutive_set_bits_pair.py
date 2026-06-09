class Solution:
    def consecutiveSetBits(self, n: int) -> bool:
        b = bin(n)[2:]
        cnt = 0
        for i in range(1, len(b)):
            if b[i - 1] == b[i] == '1':
                cnt += 1
        return cnt == 1


def test_consecutive_set_bits():
    solution = Solution()
    assert solution.consecutiveSetBits(6), 'wrong result'
    assert not solution.consecutiveSetBits(5), 'wrong result'


if __name__ == '__main__':
    test_consecutive_set_bits()
