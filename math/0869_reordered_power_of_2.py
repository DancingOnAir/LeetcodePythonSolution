class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def helper(x):
            return ''.join(sorted(str(x), reverse=True))

        n = helper(n)
        mx = int(n)
        i = 1
        while i <= mx:
            if helper(i) == n:
                return True
            i <<= 1
        return False


def test_reordered_power_of_2():
    solution = Solution()
    assert solution.reorderedPowerOf2(1), 'wrong result'
    assert not solution.reorderedPowerOf2(10), 'wrong result'


if __name__ == '__main__':
    test_reordered_power_of_2()
