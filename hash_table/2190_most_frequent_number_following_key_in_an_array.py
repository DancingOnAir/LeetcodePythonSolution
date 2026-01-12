from typing import List


class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        cnt = [0] * 1001
        res = mx = 0
        for i in range(len(nums) - 1):
            if nums[i] == key:
                cnt[nums[i + 1]] += 1
                if mx < cnt[nums[i + 1]]:
                    mx = cnt[nums[i + 1]]
                    res = nums[i + 1]
        return res


def test_most_frequent():
    solution = Solution()
    assert solution.mostFrequent([1, 100, 200, 1, 100], key=1) == 100, 'wrong result'
    assert solution.mostFrequent([2, 2, 2, 2, 3], key=2) == 2, 'wrong result'


if __name__ == '__main__':
    test_most_frequent()
