class Solution:
    def numWays(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        n = len(s)
        if n < 3:
            return 0

        num_ones = sum(map(int, s))
        q, r = divmod(num_ones, 3)
        if r:
            return 0
        if not q:
            return ((n - 2) * (n - 1) // 2) % MOD

        def count_zeros(ss: str):
            ones = 0
            idx = 0
            while ones < q:
                ones += 1 if ss[idx] == '1' else 0
                idx += 1
            return ss.find('1', idx) - idx + 1

        l = count_zeros(s)
        r = count_zeros(s[::-1])
        return (l * r) % MOD


def test_num_ways():
    solution = Solution()
    # assert solution.numWays('10101') == 4, 'wrong result'
    # assert solution.numWays('1001') == 0, 'wrong result'
    assert solution.numWays('0000') == 3, 'wrong result'
    assert solution.numWays('100100010100110') == 12, 'wrong result'


if __name__ == '__main__':
    test_num_ways()
