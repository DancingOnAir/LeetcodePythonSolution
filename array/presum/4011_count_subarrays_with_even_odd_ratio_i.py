class Solution:
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
        n = len(nums)
        cnt_x = [0] * (n + 1)
        cnt_y = [0] * (n + 1)
        for i, x in enumerate(nums):
            if x & 1:
                cnt_y[i + 1] = cnt_y[i] + 1
                cnt_x[i + 1] = cnt_x[i]
            else:
                cnt_x[i + 1] = cnt_x[i] + 1
                cnt_y[i + 1] = cnt_y[i]

        res = 0
        for i in range(n):
            for j in range(i, n):
                if (cnt_y[j + 1] - cnt_y[i]) * a - (cnt_x[j + 1] - cnt_x[i]) * b >= 0:
                    res += 1
        return res


def test_count_ratio_subarrays():
    solution = Solution()
    assert solution.countRatioSubarrays([1, 2, 1, 2], a=3, b=2) == 7, 'wrong result'
    assert solution.countRatioSubarrays([2, 2, 1], a=2, b=1) == 3, 'wrong result'
    assert solution.countRatioSubarrays([2, 2, 2], a=1, b=1) == 0, 'wrong result'


if __name__ == '__main__':
    test_count_ratio_subarrays()
