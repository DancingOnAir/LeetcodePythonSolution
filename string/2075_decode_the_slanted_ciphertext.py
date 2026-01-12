class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        cols = len(encodedText) // rows
        res = list()
        for i in range(cols):
            while i < len(encodedText):
                res.append(encodedText[i])
                i += cols + 1

        return ''.join(res).rstrip()

    def decodeCiphertext1(self, encodedText: str, rows: int) -> str:
        n = len(encodedText)
        cols = n // rows

        res = list()
        for i in range(0, cols - rows + 3):
            for j in range(0, rows):
                if j * cols + i + j < n:
                    res.append(encodedText[j * cols + i + j])

        return ''.join(res).rstrip()




def test_decode_ciphertext():
    solution = Solution()

    assert solution.decodeCiphertext("ch   ie   pr", 3) == "cipher", 'wrong result'
    assert solution.decodeCiphertext("iveo    eed   l te   olc", 4) == "i love leetcode", 'wrong result'
    assert solution.decodeCiphertext("coding", 1) == "coding", 'wrong result'


if __name__ == '__main__':
    test_decode_ciphertext()
