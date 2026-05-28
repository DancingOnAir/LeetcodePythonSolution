class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        cnt_zero = 0
        suf_zero = []
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 0:
                cnt_zero += 1
            suf_zero.append(cnt_zero)
        return cnt_zero - suf_zero[cnt_zero - 1]


def test_minimum_swaps():
    solution = Solution()
    assert solution.minimumSwaps([0, 1, 0, 3, 12]) == 2, 'wrong result'
    assert solution.minimumSwaps([0, 1, 0, 2]) == 1, 'wrong result'
    assert solution.minimumSwaps([1, 2, 0]) == 0, 'wrong result'


if __name__ == '__main__':
    test_minimum_swaps()
