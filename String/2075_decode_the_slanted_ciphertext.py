class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        n = len(encodedText)
        cols = n // rows

        res = ''
        for i in range(0, cols - rows + 3):
            for j in range(0, rows):
                if j * cols + i + j < n:
                    res += encodedText[j * cols + i + j]

        return res.rstrip()


def test_decode_ciphertext():
    solution = Solution()

    assert solution.decodeCiphertext("ch   ie   pr", 3) == "cipher", 'wrong result'
    assert solution.decodeCiphertext("iveo    eed   l te   olc", 4) == "i love leetcode", 'wrong result'
    assert solution.decodeCiphertext("coding", 1) == "coding", 'wrong result'


if __name__ == '__main__':
    test_decode_ciphertext()
