class Solution:
    # stack
    def minLength(self, s: str) -> int:
        stk = []
        for c in s:
            if stk and ((c == 'B' and stk[-1] == 'A') or (c == 'D' and stk[-1] == 'C')):
                stk.pop()
            else:
                stk.append(c)
        return len(stk)

    # simulate
    def minLength1(self, s: str) -> int:
        while "AB" in s or "CD" in s:
            s = s.replace("AB", "")
            s = s.replace("CD", "")
        return len(s)


def test_min_length():
    solution = Solution()
    assert solution.minLength("ABFCACDB") == 2, 'wrong result'
    assert solution.minLength("ACBBD") == 5, 'wrong result'


if __name__ == '__main__':
    test_min_length()
