from typing import List


class Solution:
    def averageValue(self, nums: List[int]) -> int:
        cnt = 0
        res = 0
        for x in nums:
            if x % 2 == 0 and x % 3 == 0:
                cnt += 1
                res += x
        return res // cnt if cnt else 0

    def averageValue1(self, nums: List[int]) -> int:
        res = [x for x in nums if x % 6 == 0]
        return sum(res) // len(res) if res else 0


def test_average_value():
    solution = Solution()
    assert solution.averageValue([1, 3, 6, 10, 12, 15]) == 9, 'wrong result'
    assert solution.averageValue([1, 2, 4, 7, 10]) == 0, 'wrong result'


if __name__ == '__main__':
    test_average_value()
