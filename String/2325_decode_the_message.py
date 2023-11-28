class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        m = {}
        i = 97
        for ch in key:
            if ch != ' ' and ch not in m:
                m[ch] = i
                i += 1

        return ''.join(ch if ch == ' ' else chr(m[ch]) for ch in message)


def test_decode_message():
    solution = Solution()
    assert solution.decodeMessage("the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv") == "this is a secret", 'wrong result'
    assert solution.decodeMessage("eljuxhpwnyrdgtqkviszcfmabo", "zwx hnfx lqantp mnoeius ycgk vcnjrdb") == "the five boxing wizards jump quickly", 'wrong result'


if __name__ == '__main__':
    test_decode_message()
