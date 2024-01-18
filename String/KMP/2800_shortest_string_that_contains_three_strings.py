class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:
        def merge(s1, s2):
            if s2 in s1:
                return s1

            for i in range(len(s1)):
                if s2.startswith(s1[i:]):
                    return s1[:i] + s2

            return s1 + s2

        return sorted([merge(merge(a, b), c), merge(merge(b, a), c), merge(merge(c, b), a), merge(merge(b, c), a), merge(merge(a, c), b), merge(merge(c, a), b)], key=lambda x: (len(x), x))[0]


def test_minimum_string():
    solution = Solution()
    assert solution.minimumString("ca", "a", "a") == "ca", 'wrong result'
    assert solution.minimumString("abc", "bca", "aaa") == "aaabca", 'wrong result'
    assert solution.minimumString("ab", "ba", "aba") == "aba", 'wrong result'


if __name__ == '__main__':
    test_minimum_string()
