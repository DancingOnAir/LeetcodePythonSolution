class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:
        return min(int(str(nums[i]) + str(nums[i + 1])) for i in range(0, len(nums), 2))


def test_min_merged_integers():
    solution = Solution()
    assert solution.minMergedInteger([23, 55, 42, 21]) == 2355, 'wrong result'
    assert solution.minMergedInteger([34, 7, 11, 11]) == 347, 'wrong result'
    assert solution.minMergedInteger([9, 20]) == 920, 'wrong result'


if __name__ == '__main__':
    test_min_merged_integers()
