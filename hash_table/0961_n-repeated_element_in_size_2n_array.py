class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        m = set()
        for x in nums:
            if x in m:
                return x
            m.add(x)
        return -1


def test_repeated_n_times():
    solution = Solution()
    assert solution.repeatedNTimes([1, 2, 3, 3]) == 3, 'wrong result'
    assert solution.repeatedNTimes([2, 1, 2, 5, 3, 2]) == 2, 'wrong result'
    assert solution.repeatedNTimes([5, 1, 5, 2, 5, 3, 5, 4]) == 5, 'wrong result'


if __name__ == '__main__':
    test_repeated_n_times()
