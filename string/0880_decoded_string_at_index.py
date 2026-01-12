class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        sz = 0
        for i, ch in enumerate(s):
            if ch.isdigit():
                sz *= int(ch)
            else:
                sz += 1

            if sz >= k:
                break

        for j in range(i, -1, -1):
            ch = s[j]
            if ch.isdigit():
                sz //= int(ch)
                k %= sz
            else:
                if sz == k or 0 == k:
                    return ch
                sz -= 1
        return ""


def test_decode_at_index():
    solution = Solution()
    # assert solution.decodeAtIndex("leet2code3", 10) == "o", 'wrong result'
    assert solution.decodeAtIndex("ha22", 5) == "h", 'wrong result'
    assert solution.decodeAtIndex("a2345678999999999999999", 1) == "a", 'wrong result'


if __name__ == '__main__':
    test_decode_at_index()
