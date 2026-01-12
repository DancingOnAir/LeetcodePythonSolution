class Solution:
    def stringHash(self, s: str, k: int) -> str:
        res = []
        cur = 0
        for i, c in enumerate(s):
            cur += (ord(c) - 97)
            if (i + 1) % k == 0:
                res.append(chr((cur % 26) + 97))
                cur = 0
        return ''.join(res)


def test_string_hash():
    solution = Solution()
    assert solution.stringHash("abcd", 2) == 'bf', 'wrong result'
    assert solution.stringHash("mxz", 3) == 'i', 'wrong result'


if __name__ == '__main__':
    test_string_hash()
