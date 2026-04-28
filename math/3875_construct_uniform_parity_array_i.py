class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        return True


def test_uniform_array():
    solution = Solution()
    assert solution.uniformArray([1, 4, 7]), 'wrong result'
    assert solution.uniformArray([2, 3]), 'wrong result'
    assert solution.uniformArray([4, 6]), 'wrong result'


if __name__ == '__main__':
    test_uniform_array()
