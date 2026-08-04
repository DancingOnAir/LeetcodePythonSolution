class Solution:
    def scoreDifference(self, nums: list[int]) -> int:
        res = 0
        flag = 1
        for i, x in enumerate(nums):
            if x & 1:
                flag *= -1
            if i % 6 == 5:
                flag *= -1
            res += x * flag
        return res


def test_score_difference():
    solution = Solution()
    assert solution.scoreDifference([1, 2, 3]) == 0, 'wrong result'
    assert solution.scoreDifference([2, 4, 2, 1, 2, 1]) == 4, 'wrong result'
    assert solution.scoreDifference([1]) == -1, 'wrong result'


if __name__ == '__main__':
    test_score_difference()
