from typing import List


class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        res, l, r = 0, 0, len(nums) - 1
        while l <= r:
            if l == r:
                res += nums[l]
            else:
                res += int(str(nums[l]) + str(nums[r]))
            l += 1
            r -= 1
        return res


def test_find_the_array_conc_val():
    solution = Solution()
    assert solution.findTheArrayConcVal([7, 52, 2, 4]) == 596, 'wrong result'
    assert solution.findTheArrayConcVal([5, 14, 13, 8, 12]) == 673, 'wrong result'


if __name__ == '__main__':
    test_find_the_array_conc_val()
