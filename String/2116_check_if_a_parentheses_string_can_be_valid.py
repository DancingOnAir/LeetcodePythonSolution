class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n & 0b1:
            return False
        total_zeros = locked.count('0')
        left = [0] * n
        right = [0] * n
        zeros = 0
        stk = list()
        for i in range(n):
            if locked[i] == '0':
                zeros += 1
            else:
                if s[i] == '(':
                    stk.append((i, s[i]))
                else:
                    if stk and stk[-1][1] == '(':
                        stk.pop()
            left[i] = zeros
            right[i] = total_zeros - zeros

        left_zero_cost = 0
        for i, val in stk:
            if val == ')':
                if left[i] > left_zero_cost:
                    left_zero_cost += 1
                else:
                    return False

        right_zero_cost = 0
        for i, val in stk[::-1]:
            if val == '(':
                if right[i] > right_zero_cost:
                    right_zero_cost += 1
                else:
                    return False
        return True


def test_can_be_valid():
    solution = Solution()
    assert solution.canBeValid("))()))", "010100"), 'wrong result'
    assert solution.canBeValid("()()", "0000"), 'wrong result'
    assert not solution.canBeValid(")", "0"), 'wrong result'


if __name__ == '__main__':
    test_can_be_valid()

