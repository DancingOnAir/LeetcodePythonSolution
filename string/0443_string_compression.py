from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        res = i = 0
        while i < len(chars):
            ch, sz = chars[i], 1
            while i + 1 < len(chars) and ch == chars[i + 1]:
                sz += 1
                i += 1

            chars[res] = ch
            if sz > 1:
                str_sz = str(sz)
                chars[res + 1: res + 1 + len(str_sz)] = str_sz
                res += len(str_sz)

            res += 1
            i += 1
        return res


def test_compress():
    solution = Solution()
    assert solution.compress(["a", "a", "a", "b", "b", "a", "a"]) == 6, 'wrong result'
    assert solution.compress(["a", "a", "b", "b", "c", "c", "c"]) == 6, 'wrong result'
    assert solution.compress(["a"]) == 1, 'wrong result'
    assert solution.compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]) == 4, 'wrong result'


if __name__ == '__main__':
    test_compress()
