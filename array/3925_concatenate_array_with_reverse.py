class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        return nums + nums[::-1]


def test_concat_with_reverse():
    solution = Solution()
    assert solution.concatWithReverse([1, 2, 3]) == [1, 2, 3, 3, 2, 1], 'wrong result'
    assert solution.concatWithReverse([1]) == [1, 1], 'wrong result'


if __name__ == '__main__':
    test_concat_with_reverse()
