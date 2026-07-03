class Solution:
    def countValidSubarrays(self, nums: list[int], x: int) -> int:
        res = 0
        for i in range(len(nums)):
            tot = 0
            for v in nums[i:]:
                tot += v
                if tot % 10 != x:
                    continue
                cur = tot
                while cur > 9:
                    cur //= 10
                if cur == x:
                    res += 1
        return res


def test_count_valid_subarrays():
    solution = Solution()
    assert solution.countValidSubarrays([1,100,1], x = 1) == 4, 'wrong result'
    assert solution.countValidSubarrays([1], x = 2) == 0, 'wrong result'


if __name__ == '__main__':
    test_count_valid_subarrays()
