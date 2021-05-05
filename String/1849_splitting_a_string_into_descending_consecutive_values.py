class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)
        if n < 2:
            return False

        for i in range(0, n):
            cur = int(s[:i + 1])
            if not cur or i == n - 1:
                continue
            l = r = i + 1

            while r < n:
                if int(s[l:]) == cur - 1:
                    return True

                r += 1
                if int(s[l: r]) == cur - 1:
                    cur -= 1
                    l = r

            if l == n and r == n:
                return True

        return False


def test_split_string():
    solution = Solution()
    assert not solution.splitString('1234'), 'wrong result'
    assert solution.splitString('050043'), 'wrong result'
    assert not solution.splitString('9080701'), 'wrong result'
    assert solution.splitString('10009998'), 'wrong result'
    assert solution.splitString("200100"), 'wrong result'


if __name__ == '__main__':
    test_split_string()
