from typing import List


class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        def cost(x):
            return sum(abs(a - x) for a in nums)

        nums.sort()
        mid = nums[len(nums) // 2]
        decease = increase = mid
        while str(decease) != str(decease)[::-1]:
            decease -= 1
        while str(increase) != str(increase)[::-1]:
            increase += 1

        return min(cost(decease), cost(increase))


def test_minimum_cost():
    solution = Solution()
    assert solution.minimumCost([4, 3, 1]) == 3, 'wrong result'
    assert solution.minimumCost([1, 2, 3, 4, 5]) == 6, 'wrong result'
    assert solution.minimumCost([10, 12, 13, 14, 15]) == 11, 'wrong result'
    assert solution.minimumCost([22, 33, 22, 33, 22]) == 22, 'wrong result'


if __name__ == '__main__':
    test_minimum_cost()
