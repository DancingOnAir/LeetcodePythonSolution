from typing import List


class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        return sum(x if x < 10 else -x for x in nums) != 0

    def canAliceWin1(self, nums: List[int]) -> bool:
        single_digit_sum = 0
        total = 0
        for x in nums:
            if x < 10:
                single_digit_sum += x
            total += x
        return total != single_digit_sum * 2


def test_can_alice_win():
    solution = Solution()
    assert not solution.canAliceWin([1, 2, 3, 4, 10]), 'wrong result'
    assert solution.canAliceWin([1, 2, 3, 4, 5, 14]), 'wrong result'
    assert solution.canAliceWin([5, 5, 5, 25]), 'wrong result'


if __name__ == '__main__':
    test_can_alice_win()
