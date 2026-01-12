class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-', '').upper()[::-1]
        return '-'.join(s[i: i+k] for i in range(0, len(s), k))[::-1]

    def licenseKeyFormatting1(self, s: str, k: int) -> str:
        s = s.replace('-', '')
        q, r = divmod(len(s), k)
        cur = ''
        res = list()
        for c in s:
            if c.isdigit():
                cur += c
            elif c.isalpha():
                cur += c.upper()

            if len(cur) == r and len(res) == 0:
                res.append(cur)
                cur = ''
            elif len(cur) == k:
                res.append(cur)
                cur = ''
        return '-'.join(res)


def test_license_key_formatting():
    solution = Solution()

    assert solution.licenseKeyFormatting("--a-a-a-a--", 2) == "AA-AA", 'wrong result'
    assert solution.licenseKeyFormatting("5F3Z-2e-9-w", 4) == "5F3Z-2E9W", 'wrong result'
    assert solution.licenseKeyFormatting("2-5g-3-J", 2) == "2-5G-3J", 'wrong result'


if __name__ == '__main__':
    test_license_key_formatting()
