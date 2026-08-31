from bisect import bisect_left, bisect_right


class Solution:
    def findDisappearedNumbers(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        nums = sorted(set(nums))
        pre = lower - 1
        res = []
        for x in nums:
            if x < lower:
                continue
            if x > upper:
                break
            if x > pre + 1:
                res.append([pre + 1, x - 1])
            pre = x

        if pre < upper:
            res.append([pre + 1, upper])
        return res

    def findDisappearedNumbers1(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        nums.sort()
        if lower > nums[-1] or upper < nums[0]:
            return [[lower, upper]]

        l = bisect_left(nums, lower)
        r = bisect_right(nums, upper)

        res = []
        for i in range(l, r + 1):
            if i == l:
                if lower < nums[i]:
                    res.append([lower, min(upper, nums[i] - 1)])
            elif i == r:
                if upper > nums[r - 1]:
                    res.append([nums[r - 1] + 1, upper])
            else:
                if nums[i -1] < nums[i] - 1:
                    res.append([nums[i - 1] + 1, nums[i] - 1])
        return res


def test_find_disappeared_numbers():
    solution = Solution()
    assert solution.findDisappearedNumbers([6,966], 316, 456) ==[[316,456]], 'wrong result'
    assert solution.findDisappearedNumbers([2,219], 80, 489) == [[80, 218], [220, 489]], 'wrong result'
    assert solution.findDisappearedNumbers([3, 9, 7], lower=1, upper=12) == [[1, 2], [4, 6], [8, 8], [10, 12]], 'wrong result'
    assert solution.findDisappearedNumbers([1, 1], lower=5, upper=7) == [[5, 7]], 'wrong result'
    assert solution.findDisappearedNumbers([2, 3, 5], lower=2, upper=3) == [], 'wrong result'


if __name__ == '__main__':
    test_find_disappeared_numbers()
