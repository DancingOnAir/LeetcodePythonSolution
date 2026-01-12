class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) == len(str2):
            return str1 if str1 == str2 else ''
        else:
            if len(str1) < len(str2):
                str1, str2 = str2, str1
            if str1[:len(str2)] == str2:
                return self.gcdOfStrings(str1[len(str2):], str2)
            else:
                return ''

    def gcdOfStrings2(self, str1: str, str2: str) -> str:
        def gcd(a, b):
            if a < b:
                a, b = b, a

            while a % b != 0:
                a, b = b, a % b
            return b

        i = gcd(len(str1), len(str2))
        return str1[:i] if str1 + str2 == str2 + str1 else ''

    def gcdOfStrings1(self, str1: str, str2: str) -> str:
        def gcd(a: int, b: int) -> int:
            if a < b:
                a, b = b, a
            while a % b != 0:
                a, b = b, a%b
            return b

        l1 = len(str1)
        l2 = len(str2)
        x = gcd(l1, l2)

        for i in range(x, 0, -1):
            res = str1[:i]
            if res * (l1 // i) == str1 and res * (l2 // i) == str2:
                return res
        return ''


def test_gcd_of_strings():
    solution = Solution()

    assert solution.gcdOfStrings('ABCABC', 'ABC') == 'ABC', 'wrong result'
    assert solution.gcdOfStrings('ABABAB', 'ABAB') == 'AB', 'wrong result'
    assert solution.gcdOfStrings('LEET', 'CODE') == '', 'wrong result'
    assert solution.gcdOfStrings('ABCDEF', 'ABC') == '', 'wrong result'


if __name__ == '__main__':
    test_gcd_of_strings()
