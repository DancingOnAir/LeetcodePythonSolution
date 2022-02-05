class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n & 1:
            return False

        tot = op = cl = 0
        for i in range(n):
            if locked[i] == '0':
                tot += 1
            elif s[i] == '(':
                op += 1
            elif s[i] == ')':
                cl += 1

            if tot + op - cl < 0:
                return False

        tot = op = cl = 0
        for i in range(n-1, -1, -1):
            if locked[i] == '0':
                tot += 1
            elif s[i] == '(':
                op += 1
            elif s[i] == ')':
                cl += 1

            if tot + cl - op < 0:
                return False

        return True

def test_can_be_valid():
    solution = Solution()
    assert solution.canBeValid("))()))", "010100"), 'wrong result'
    assert solution.canBeValid("()()", "0000"), 'wrong result'
    assert not solution.canBeValid(")", "0"), 'wrong result'


if __name__ == '__main__':
    test_can_be_valid()

