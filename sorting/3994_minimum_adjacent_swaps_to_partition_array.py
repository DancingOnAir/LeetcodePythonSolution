class Solution:
    def minAdjacentSwaps(self, nums: list[int], a: int, b: int) -> int:
        res = cnt1 = cnt2 = 0
        for x in nums:
            if x < a:
                res += cnt1 + cnt2
            elif x <= b:
                res += cnt2
                cnt1 += 1
            else:
                cnt2 += 1
        return res % 1_000_000_007


def test_min_adjacent_swaps():
    solution = Solution()
    assert solution.minAdjacentSwaps([1, 3, 2, 4, 5, 6], a=3, b=4) == 1, 'wrong result'
    assert solution.minAdjacentSwaps([9, 7, 5, 3], a=4, b=8) == 5, 'wrong result'
    assert solution.minAdjacentSwaps([3, 7, 5, 9], a=4, b=8) == 0, 'wrong result'


if __name__ == '__main__':
    test_min_adjacent_swaps()
