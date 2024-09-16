class Solution:
    def compressedString(self, word: str) -> str:
        res = []
        i = -1
        for j, ch in enumerate(word):
            if j == len(word) - 1 or word[j] != word[j + 1]:
                sz = j - i
                r, q = divmod(sz, 9)
                res.append(('9' + ch) * r)
                if q != 0:
                    res.append(str(q) + ch)

                i = j
        return ''.join(res)


def test_compressed_string():
    solution = Solution()
    assert solution.compressedString("aaaaaaaaay") == "9a1y", 'wrong result'
    assert solution.compressedString("abcde") == "1a1b1c1d1e", 'wrong result'
    assert solution.compressedString("aaaaaaaaaaaaaabb") == "9a5a2b", 'wrong result'


if __name__ == '__main__':
    test_compressed_string()
