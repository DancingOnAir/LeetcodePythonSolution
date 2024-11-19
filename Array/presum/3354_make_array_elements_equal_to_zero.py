from typing import List


class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        tot = sum(nums)
        pre = res = 0
        for x in nums:
            if x:
                pre += x
            else:
                if tot == pre * 2:
                    res += 2
                elif abs(tot - pre * 2) == 1:
                    res += 1
        return res

    def countValidSelections1(self, nums: List[int]) -> int:
        ps = []
        for x in nums:
            if not ps:
                ps.append(x)
            else:
                ps.append(ps[-1] + x)

        res = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                if ps[i] == ps[-1] - ps[i]:
                    res += 2
                elif abs(ps[-1] - ps[i] - ps[i]) == 1:
                    res += 1
        return res


def test_count_valid_selections():
    solution = Solution()
    assert solution.countValidSelections([16, 13, 10, 0, 0, 0, 10, 6, 7, 8, 7]) == 3, 'wrong result'
    assert solution.countValidSelections([1, 0, 2, 0, 3]) == 2, 'wrong result'
    assert solution.countValidSelections([2, 3, 4, 0, 4, 1, 0]) == 0, 'wrong result'


if __name__ == '__main__':
    test_count_valid_selections()
