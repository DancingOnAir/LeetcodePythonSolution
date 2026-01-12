class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return '0'
        k = -2
        res = []
        while n != 0:
            n, r = divmod(n, k)
            if r < 0:
                res.append(str(r - k))
                n += 1
            else:
                res.append(str(r))
        return ''.join(res[::-1])


def test_base_neg2():
    solution = Solution()
    assert solution.baseNeg2(2) == "110", 'wrong result'
    assert solution.baseNeg2(3) == "111", 'wrong result'
    assert solution.baseNeg2(4) == "100", 'wrong result'


if __name__ == '__main__':
    test_base_neg2()
