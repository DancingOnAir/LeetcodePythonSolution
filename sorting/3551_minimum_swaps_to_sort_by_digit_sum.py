from collections import defaultdict


class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        xid = {x: i for i, x in enumerate(nums)}
        sorted_nums = sorted(nums, key= lambda x: (sum(map(int, str(x))), x))
        res = 0
        for i, x in enumerate(sorted_nums):
            j = xid[x]
            if i == j:
                continue

            xid[x] = i
            xid[nums[i]] = j
            nums[i], nums[j] = nums[j], nums[i]
            res += 1

        return res


def test_min_swaps():
    solution = Solution()
    assert solution.minSwaps([37, 100]) == 1, 'wrong result'
    assert solution.minSwaps([22, 14, 33, 7]) == 0, 'wrong result'
    assert solution.minSwaps([18, 43, 34, 16]) == 2, 'wrong result'


if __name__ == '__main__':
    test_min_swaps()
