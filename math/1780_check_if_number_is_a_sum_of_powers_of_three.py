class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n:
            if n % 3 == 0 or n % 3 == 1:
                n //= 3
            else:
                return False
        return True


def test_check_power_of_three():
    solution = Solution()
    assert solution.checkPowersOfThree(12), 'wrong result'
    assert solution.checkPowersOfThree(91), 'wrong result'
    assert not solution.checkPowersOfThree(21), 'wrong result'


if __name__ == '__main__':
    test_check_power_of_three()
