class Solution:
    def countGoodRotations(self, nums: list[int]) -> int:
        n = len(nums)
        m = n // 2
        res = sum1 = sum2 = 0
        for i in range(m, n * 2 - 1):
            sum1 += nums[(i - m) % n]
            sum2 += nums[i % n]

            left = i - n + 1
            if left < 0:
                continue
            if sum1 > sum2:
                res += 1

            sum1 -= nums[left]
            sum2 -= nums[(left + m) % n]
        return res


def test_count_good_rotations():
    solution = Solution()
    assert solution.countGoodRotations([1, 2, 3, 4, 5, 6]) == 3, 'wrong result'
    assert solution.countGoodRotations([1, 2, 1, 2]) == 0, 'wrong result'


if __name__ == '__main__':
    test_count_good_rotations()
