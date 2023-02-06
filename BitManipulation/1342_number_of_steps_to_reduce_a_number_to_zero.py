class Solution:
    def numberOfSteps(self, num: int) -> int:
        return sum(2 if x == '1' else 1 for x in bin(num)[2:]) - 1

    def numberOfSteps1(self, num: int) -> int:
        res = 0
        while num:
            if num & 1:
                num -= 1
            else:
                num >>= 1
            res += 1
        return res


def test_number_of_steps():
    solution = Solution()
    # 1110
    assert solution.numberOfSteps(14) == 6, 'wrong result'
    # 1000
    assert solution.numberOfSteps(8) == 4, 'wrong result'
    # 0111 1011
    assert solution.numberOfSteps(123) == 12, 'wrong result'


if __name__ == '__main__':
    test_number_of_steps()
