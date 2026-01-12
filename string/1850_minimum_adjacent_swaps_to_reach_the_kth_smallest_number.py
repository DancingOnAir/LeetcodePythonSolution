from itertools import permutations
from typing import List


class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        def next_permutation(nums: List[int]) -> None:
            n = len(nums)
            i = n - 1
            while i > 0 and nums[i - 1] >= nums[i]:
                i -= 1
            if not i:
                nums.reverse()

            j = n - 1
            while j > i and nums[j] <= nums[i - 1]:
                j -= 1

            nums[i - 1], nums[j] = nums[j], nums[i - 1]

            j = n - 1
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        num_list = list(num)
        for _ in range(k):
            next_permutation(num_list)

        res = 0
        num = list(num)
        for i in range(len(num_list)):
            if num_list[i] != num[i]:
                j = i + 1
                while num[j] != num_list[i]:
                    j += 1
                num[i: j + 1] = [num[j]] + num[i: j]
                res += j - i
        return res


def test_get_min_swaps():
    solution = Solution()

    assert solution.getMinSwaps('5489355142', 4) == 2, 'wrong result'
    assert solution.getMinSwaps('11112', 4) == 4, 'wrong result'
    assert solution.getMinSwaps('00123', 1) == 1, 'wrong result'
    assert solution.getMinSwaps('059', 5) == 3, 'wrong result'


if __name__ == '__main__':
    test_get_min_swaps()
