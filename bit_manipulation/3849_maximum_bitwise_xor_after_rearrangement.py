class Solution:
    def maximumXor(self, s: str, t: str) -> str:
        zeros = t.count("0")
        ones = len(t) - zeros

        res = []
        for c in s:
            if (c == '0' and ones) or (c == '1' and zeros):
                res.append('1')
                ones -= (c == '0')
                zeros -= (c == '1')
            else:
                res.append('0')
                ones -= (c == '1')
                zeros -= (c == '0')

        return ''.join(res)

    def maximumXor1(self, s: str, t: str) -> str:
        n = len(s)
        ones = t.count('1')
        new_t = ["0"] * n
        for i in range(n):
            if s[i] == '0' and ones > 0:
                new_t[i] = '1'
                ones -= 1
        i = n - 1
        while ones > 0:
            while new_t[i] == '1':
                i -= 1
            new_t[i] = '1'
            ones -= 1
        return format(int(s, 2) ^ int(''.join(new_t), 2), '0' + str(n) + 'b')


def test_maximum_xor():
    solution = Solution()
    assert solution.maximumXor("11", "11") == "00", 'wrong result'
    assert solution.maximumXor("101", "011") == "110", 'wrong result'
    assert solution.maximumXor("0110", "1110") == "1101", 'wrong result'
    assert solution.maximumXor("0101", "1001") == "1111", 'wrong result'


if __name__ == '__main__':
    test_maximum_xor()
