class Solution:
    def countConsistent(self, nums: list[int]) -> int:
        res = 0
        return res


def test_count_consistent():
    solution = Solution()
    assert solution.countConsistent([5, 3, 1, 2]) == 6, 'wrong result'
    assert solution.countConsistent([1, 1, 1]) == 6, 'wrong result'
    assert solution.countConsistent([0]) == 1, 'wrong result'


if __name__ == '__main__':
    test_count_consistent()
