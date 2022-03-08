class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        nums = [int(w) for w in s.split() if w.isdigit()]
        return all(a < b for a, b in zip(nums, nums[1:]))

    def areNumbersAscending1(self, s: str) -> bool:
        prev = -1
        for w in s.split():
            if w[0].isdigit():
                if int(w) <= prev:
                    return False
                prev = int(w)
        return True


def test_are_numbers_ascending():
    solution = Solution()

    assert solution.areNumbersAscending("1 box has 3 blue 4 red 6 green and 12 yellow marbles"), 'wrong result'
    assert not solution.areNumbersAscending("hello world 5 x 5"), 'wrong result'
    assert not solution.areNumbersAscending("sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s"), 'wrong result'


if __name__ == '__main__':
    test_are_numbers_ascending()
