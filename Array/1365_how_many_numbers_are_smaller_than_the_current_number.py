from typing import List
import bisect


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        indices = {}
        for i, val in enumerate(sorted(nums)):
            indices.setdefault(val, i)
        return [indices[i] for i in nums]

    def smallerNumbersThanCurrent2(self, nums: List[int]) -> List[int]:
        return [*map(sorted(nums).index, nums)]

    def smallerNumbersThanCurrent1(self, nums: List[int]) -> List[int]:
        record, res = [], [0] * len(nums)
        for i, val in enumerate(nums):
            record.append([val, i])
        record.sort()
        for i in range(len(record)):
            pos = bisect.bisect_left(record, [record[i][0], 0])
            res[record[i][1]] = pos
        return res


def test_smaller_number_than_current():
    solution = Solution()

    nums1 = [8, 1, 2, 2, 3]
    print(solution.smallerNumbersThanCurrent(nums1))

    nums2 = [6, 5, 4, 8]
    print(solution.smallerNumbersThanCurrent(nums2))

    nums3 = [7, 7, 7, 7]
    print(solution.smallerNumbersThanCurrent(nums3))


if __name__ == '__main__':
    test_smaller_number_than_current()
