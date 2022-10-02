from typing import List


class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        def helper(flag: int):
            stk = list()
            s = set()
            for i in range(len(nums))[::flag]:
                if len(stk) >= k:
                    s.add(i)
                if stk and nums[i] > stk[-1]:
                    stk.clear()
                stk.append(nums[i])
            return s

        return sorted(helper(1) & helper(-1))


def test_good_indices():
    solution = Solution()
    assert solution.goodIndices([878724, 201541, 179099, 98437, 35765, 327555, 475851, 598885, 849470, 943442], 4) == [4, 5], 'wrong result'
    assert solution.goodIndices([2, 1, 1, 1, 3, 4, 1], 2) == [2, 3], 'wrong result'
    assert solution.goodIndices([2, 1, 1, 2], 2) == [], 'wrong result'


if __name__ == '__main__':
    test_good_indices()
