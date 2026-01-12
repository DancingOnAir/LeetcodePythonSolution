class Solution:
    def splitString(self, s: str) -> bool:
        def helper(s, pre):
            if pre != -1 and int(s) == pre - 1:
                return True
            for i in range(1, len(s)):
                cur = int(s[:i])
                if pre == -1 or cur == pre - 1:
                    if helper(s[i:], cur):
                        return True
            return False

        return helper(s, -1)

    def splitString3(self, s: str, pre: int = None) -> bool:
        if pre and int(s) == pre - 1:
            return True

        for i in range(1, len(s)):
            cur = int(s[: i])
            if pre is None or cur == pre - 1:
                if self.splitString(s[i:], cur):
                    return True
        return False

    def splitString2(self, s: str) -> bool:
        def helper(s: str, idx: int, length: int, pre: int, splits: int)-> bool:
            if idx == len(s) and splits > 1:
                return True

            while idx + length <= len(s):
                cur = int(s[idx: idx+length])
                length += 1

                if pre != -1 and cur != pre - 1:
                    continue
                if helper(s, idx + length - 1, 1, cur, splits + 1):
                    return True
            return False

        return helper(s, 0, 1, -1, 0)

    def splitString1(self, s: str) -> bool:
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
