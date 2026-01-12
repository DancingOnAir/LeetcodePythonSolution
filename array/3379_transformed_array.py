from typing import List


class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        for i, x in enumerate(nums):
            if x == 0:
                res.append(x)
            else:
                res.append(nums[(i + x) % n])

        return res


def test_construct_transformed_array():
    solution = Solution()
    assert solution.constructTransformedArray([3,-2,1,1]) == [1,1,1,3], 'wrong result'
    assert solution.constructTransformedArray([-1,4,-1]) == [-1,-1,4], 'wrong result'


if __name__ == '__main__':
    test_construct_transformed_array()
