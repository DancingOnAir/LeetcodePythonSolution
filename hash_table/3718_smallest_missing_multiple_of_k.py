class Solution:
    def missingMultiple(self, nums: list[int], k: int) -> int:
        m = set(nums)
        res = k
        while res in m:
            res += k
        return res


def test_missing_multiple():
    solution = Solution()
    assert solution.missingMultiple([8,2,3,4,6], k = 2) == 10, 'wrong result'
    assert solution.missingMultiple([1,4,7,10,15], k = 5) == 5, 'wrong result'


if __name__ == '__main__':
    test_missing_multiple()

