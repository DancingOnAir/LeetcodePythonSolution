class Solution:
    # https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/discuss/1184352/JavaPython-Clean-and-Concise-Clear-Explanation-O(N)
    def numSteps(self, s: str) -> int:
        res = carry = 0
        for c in s[:0:-1]:
            if int(c) + carry == 1:
                carry = 1
                res += 2
            else:
                res += 1
        return res + carry

    def numSteps1(self, s: str) -> int:
        # num = 0
        # for i, c in enumerate(s[::-1]):
        #     num += 2 ** i * (c == '1')
        num = int(s, 2)
        res = 0
        while num != 1:
            if num & 1:
                num += 1
            else:
                num >>= 1
            res += 1

        return res


def test_num_steps():
    solution = Solution()
    assert solution.numSteps('1101') == 6, 'wrong result'
    assert solution.numSteps('10') == 1, 'wrong result'
    assert solution.numSteps('1') == 0, 'wrong result'


if __name__ == '__main__':
    test_num_steps()
