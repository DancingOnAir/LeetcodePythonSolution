class Solution:
    def maxTotal(self, nums: list[int], s: str) -> int:
        res = 0
        mi = float('inf')
        for i, x in enumerate(nums):
            if s[i] == '1':
                res += x
                mi = min(mi, x)
                # 遍历到了段的末尾
                if i == len(nums) - 1 or s[i + 1] == '0':
                    res -= mi
            # 011...111段的开头
            elif i < len(nums) - 1 and s[i + 1] == '1':
                res += x
                mi = x
        return res


def test_max_total():
    solution = Solution()
    assert solution.maxTotal([9,2,6,1], s = "0101") == 15
    assert solution.maxTotal([5,1,4], s = "001") == 4
    assert solution.maxTotal([9,3,5], s = "011") == 14


if __name__ == '__main__':
    test_max_total()

