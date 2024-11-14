from typing import List


class Solution:
    # https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/solutions/6028775/java-c-python-one-pass-o-1-space/
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        pre_increase, increase = 0, 1
        res = 0
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                increase += 1
            else:
                pre_increase = increase
                increase = 1
            res = max(res, min(pre_increase, increase), increase // 2)
        return res >= k

    def hasIncreasingSubarrays1(self, nums: List[int], k: int) -> bool:
        stk = []
        cnt = 0
        for i, x in enumerate(nums):
            if stk and stk[-1] >= x:
                if len(stk) >= k:
                    if cnt == 1 or len(stk) >= 2 * k:
                        return True
                    else:
                        cnt = 1
                else:
                    cnt = 0
                stk = [x]
            else:
                stk.append(x)
                if len(stk) >= 2 * k:
                    return True
        return cnt == 1 and len(stk) >= k


def test_has_increasing_subarrays():
    solution = Solution()
    assert solution.hasIncreasingSubarrays([19, 5], 1), 'wrong result'
    assert solution.hasIncreasingSubarrays([2, 5, 7, 8, 9, 2, 3, 4, 3, 1], 3), 'wrong result'
    assert not solution.hasIncreasingSubarrays([1, 2, 3, 4, 4, 4, 4, 5, 6, 7], 5), 'wrong result'


if __name__ == '__main__':
    test_has_increasing_subarrays()
