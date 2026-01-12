class Solution:
    def minimumChairs(self, s: str) -> int:
        stk = []
        res = 0
        for c in s:
            if c == 'E':
                stk.append(c)
            else:
                if stk:
                    stk.pop()
            res = max(res, len(stk))
        return res


def test_minimum_chairs():
    solution = Solution()
    assert solution.minimumChairs("EEEEEEE") == 7, 'wrong result'
    assert solution.minimumChairs("ELELEEL") == 2, 'wrong result'
    assert solution.minimumChairs("ELEELEELLL") == 3, 'wrong result'


if __name__ == '__main__':
    test_minimum_chairs()
