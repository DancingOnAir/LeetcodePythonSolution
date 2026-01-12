class Solution:
    # dp
    def numberOfWays(self, s: str) -> int:
        dp = {'0': 0, '1': 0, '01': 0, '10': 0, '010': 0, '101': 0}
        for c in s:
            if c == '0':
                dp['0'] += 1
                dp['10'] += dp['1']
                dp['010'] += dp['01']
            else:
                dp['1'] += 1
                dp['01'] += dp['0']
                dp['101'] += dp['10']
        return dp['010'] + dp['101']

    def numberOfWays1(self, s: str) -> int:
        n = len(s)
        zeros = s.count('0')
        ones = s.count('1')

        left, right = [0] * n, [0] * n
        left_zero, left_one = 0, 0
        for i, c in enumerate(s):
            if c == '0':
                left[i] = left_one
                right[i] = ones - left_one
                left_zero += 1
            else:
                left[i] = left_zero
                right[i] = zeros - left_zero
                left_one += 1

        res = 0
        for i in range(n):
            res += left[i] * right[i]
        return res


def test_number_of_ways():
    solution = Solution()
    assert solution.numberOfWays("001101") == 6, 'wrong result'
    assert solution.numberOfWays("11100") == 0, 'wrong result'


if __name__ == '__main__':
    test_number_of_ways()
