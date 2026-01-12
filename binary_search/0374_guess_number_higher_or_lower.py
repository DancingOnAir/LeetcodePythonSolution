from bisect import bisect_left


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    if num > 6:
        return -1
    elif num < 6:
        return 1
    return 0


class Solution:
    # for python 3.10
    def guessNumber(self, n: int) -> int:
        return bisect_left(range(n), 1, key=lambda x: -guess(x))

    def guessNumber1(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = left + (right - left) // 2
            if guess(mid) > 0:
                left = mid + 1
            elif guess(mid) < 0:
                right = mid - 1
            else:
                return mid
        return -1


def test_guess_number():
    solution = Solution()
    assert solution.guessNumber(10) == 6, 'wrong result'


if __name__ == '__main__':
    test_guess_number()
