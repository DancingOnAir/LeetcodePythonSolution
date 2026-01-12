class Solution:
    # TLE
    def sumOfNumberAndReverse(self, num: int) -> bool:
        return num in {x + int(str(x)[::-1]) for x in range(100001)}

    def sumOfNumberAndReverse1(self, num: int) -> bool:
        return any(x + int(str(x)[::-1]) == num for x in range(num // 2, num + 1))


def test_sum_of_number_and_reverse():
    solution = Solution()
    assert solution.sumOfNumberAndReverse(443), 'wrong result'
    assert not solution.sumOfNumberAndReverse(63), 'wrong result'
    assert solution.sumOfNumberAndReverse(181), 'wrong result'


if __name__ == '__main__':
    test_sum_of_number_and_reverse()
