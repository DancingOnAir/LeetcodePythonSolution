class Solution:
    def shadowPairs(self, nums: list[int]) -> int:
        stk = [[0, 0]]
        res = size = 0

        for x in nums:
            while stk[-1][0] > x:
                size -= stk.pop()[1]
            res += size
            if stk[-1][0] == x:
                res -= stk[-1][1]
                stk[-1][1] += 1
            else:
                stk.append([x, 1])
            size += 1
        return res


def test_shadow_pairs():
    solution = Solution()
    assert solution.shadowPairs([3, 1, 4, 1, 5]) == 3, 'wrong result'
    assert solution.shadowPairs([6, 7, 6, 6, 7]) == 4, 'wrong result'
    assert solution.shadowPairs([1, 2, 3, 4]) == 6, 'wrong result'


if __name__ == '__main__':
    test_shadow_pairs()
