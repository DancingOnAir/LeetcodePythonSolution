class Solution:
    def smallestIndex(self, nums: list[int]) -> int:
        for i, x in enumerate(nums):
            if i == sum(map(int, str(x))):
                return i
        return -1


def test_smallest_index():
    solution = Solution()
    assert solution.smallestIndex([1, 3, 2]) == 2, 'wrong result'
    assert solution.smallestIndex([1, 10, 11]) == 1, 'wrong result'
    assert solution.smallestIndex([1, 2, 3]) == -1, 'wrong result'


if __name__ == '__main__':
    test_smallest_index()
