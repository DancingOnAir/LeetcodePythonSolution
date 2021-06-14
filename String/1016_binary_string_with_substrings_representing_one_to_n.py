class Solution:
    def queryString(self, s: str, n: int) -> bool:
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
