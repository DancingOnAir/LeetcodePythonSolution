class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        n = len(s)
        k %= n
        return (s * 2)[k: k + n]


def test_get_encrypted_string():
    solution = Solution()
    assert solution.getEncryptedString("dart", 3) == "tdar"
    assert solution.getEncryptedString("aaa", 1) == "aaa"


if __name__ == '__main__':
    test_get_encrypted_string()
