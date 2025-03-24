class Solution:
    # math
    # https://leetcode.com/problems/determine-the-minimum-sum-of-a-k-avoiding-array/solutions/3934958/java-c-python-easy-math-o-1/
    def minimumSum(self, n: int, k: int) -> int:
        a = min(n, k // 2)
        b = n - a
        return (a + 1) * a // 2 + (k + k + b - 1) * b // 2

    # hashtable
    def minimumSum1(self, n: int, k: int) -> int:
        m = set()
        i = 1
        res = 0
        while n:
            if i not in m:
                m.add(k - i)
                res += i
                n -= 1
            i += 1

        return res


def test_minimum_sum():
    solution = Solution()
    assert solution.minimumSum(5, 4) == 18, 'wrong result'
    assert solution.minimumSum(2, 6) == 3, 'wrong result'


if __name__ == '__main__':
    test_minimum_sum()
