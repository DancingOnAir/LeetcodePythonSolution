class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        prem = 1 << (n - 1)
        if k > 3 * prem:
            return ""

        res = ['a', 'b', 'c'][(k - 1) // prem]
        while prem > 1:
            k = (k - 1) % prem + 1
            prem >>= 1
            res += ['a', 'b'][res[-1] == 'a'] if (k - 1) // prem == 0 else ['b', 'c'][res[-1] != 'c']
        return res


def test_et_happy_string():
    solution = Solution()

    assert solution.getHappyString(1, 3) == "c", 'wrong result'
    assert solution.getHappyString(1, 4) == "", 'wrong result'
    assert solution.getHappyString(3, 9) == "cab", 'wrong result'
    assert solution.getHappyString(2, 7) == "", 'wrong result'
    assert solution.getHappyString(10, 100) == "abacbabacb", 'wrong result'


if __name__ == '__main__':
    test_et_happy_string()
