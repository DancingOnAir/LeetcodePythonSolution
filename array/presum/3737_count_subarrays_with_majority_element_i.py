from sortedcontainers import SortedList


class Solution:
    def countMajoritySubarrays(self, nums: list[int], target: int) -> int:
        sl = SortedList([0])
        tot = res = 0
        for i, x in enumerate(nums):
            tot += 1 if x == target else -1
            res += sl.bisect_left(tot)
            sl.add(tot)
        return res


def test_count_majority_subarrays():
    solution = Solution()
    assert solution.countMajoritySubarrays([1,2,2,3], target = 2) == 5, 'wrong result'
    assert solution.countMajoritySubarrays([1,1,1,1], target = 1) == 10, 'wrong result'
    assert solution.countMajoritySubarrays([1,2,3], target = 4) == 0, 'wrong result'


if __name__ == '__main__':
    test_count_majority_subarrays()

