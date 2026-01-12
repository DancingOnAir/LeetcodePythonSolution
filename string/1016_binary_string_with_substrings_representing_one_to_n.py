class Solution:
    # The solution can be improve a half by checking from N to N/2.
    # The reason is simply for every i < N/2, the binary string of 2*i will contain binary string of i. Thus we don't need to check for i < N/2
    def queryString(self, s: str, n: int) -> bool:
        return all(bin(i)[2:] in s for i in range(n, n // 2, -1))

    def queryString1(self, s: str, n: int) -> bool:
        for i in range(n, 0, -1):
            if '{0:b}'.format(i) not in s:
                return False
        return True


def test_query_string():
    solution = Solution()
    assert solution.queryString('0110', 3), 'wrong result'
    assert not solution.queryString('0110', 4), 'wrong result'


if __name__ == '__main__':
    test_query_string()
