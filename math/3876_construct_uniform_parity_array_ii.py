class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        if min(nums1) & 1:
            return True
        for x in nums1:
            if x & 1:
                return False
        return True

    def uniformArray1(self, nums1: list[int]) -> bool:
        cnt_odd = cnt_even = 0
        min_odd = float('inf')
        min_even = float('inf')
        for x in nums1:
            if x & 1:
                cnt_odd += 1
                min_odd = min(min_odd, x)
            else:
                cnt_even += 1
                min_even = min(min_even, x)
        return cnt_odd == len(nums1) or cnt_even == len(nums1) or (cnt_odd > 0 and cnt_even > 0 and min_even > min_odd)


def test_uniform_array():
    solution = Solution()
    assert solution.uniformArray([1, 4, 7]), 'wrong result'
    assert not solution.uniformArray([2, 3]), 'wrong result'
    assert solution.uniformArray([4, 6]), 'wrong result'


if __name__ == '__main__':
    test_uniform_array()
