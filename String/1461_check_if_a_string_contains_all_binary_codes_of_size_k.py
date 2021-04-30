class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        if n <= k:
            return False

        for i in range(1 << k):
            cur_binary = '{:b}'.format(i)
            cur_binary = '0' * (k - len(cur_binary)) + cur_binary
            if cur_binary not in s:
                return False
        return True


def test_has_all_codes():
    solution = Solution()
    assert solution.hasAllCodes('00110110', 2), 'wrong result'
    assert solution.hasAllCodes('00110', 2), 'wrong result'
    assert solution.hasAllCodes('0110', 1), 'wrong result'
    assert not solution.hasAllCodes('0110', 2), 'wrong result'
    assert not solution.hasAllCodes('0000000001011100', 4), 'wrong result'


if __name__ == '__main__':
    test_has_all_codes()
