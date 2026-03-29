from collections import Counter


class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        cnt = Counter(nums)
        for x in nums:
            if x % 2 == 0 and cnt[x] == 1:
                return x
        return -1


def test_first_unique_even():
    solution = Solution()
    assert solution.firstUniqueEven([3, 4, 2, 5, 4, 6]) == 2, 'wrong result'
    assert solution.firstUniqueEven([4, 4]) == -1, 'wrong result'


if __name__ == '__main__':
    test_first_unique_even()
