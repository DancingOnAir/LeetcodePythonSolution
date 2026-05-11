class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [0] * n
        odds = evens = 0
        for i in range(n - 1, -1, -1):
            if nums[i] & 1:
                res[i] = evens
                odds += 1
            else:
                res[i] = odds
                evens += 1
        return res


def test_count_opposite_parity():
    solution = Solution()
    assert solution.countOppositeParity([1, 2, 3, 4]) == [2, 1, 1, 0], 'wrong result'
    assert solution.countOppositeParity([1]) == [0], 'wrong result'


if __name__ == '__main__':
    test_count_opposite_parity()
