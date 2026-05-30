class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        res = []
        pre = -1
        cnt = 0
        for x in nums:
            if pre == -1 or pre != x:
                cnt = 1
            else:
                cnt += 1
            if cnt <= k:
                res.append(x)
            pre = x
        return res


def test_limit_occurrences():
    solution = Solution()
    assert solution.limitOccurrences([1, 1, 1, 2, 2, 3], k=2) == [1, 1, 2, 2, 3], 'wrong result'
    assert solution.limitOccurrences([1, 2, 3], k=1) == [1, 2, 3], 'wrong result'


if __name__ == '__main__':
    test_limit_occurrences()
