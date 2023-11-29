class Solution:
    # presum
    def beautifulSubstrings(self, s: str, k: int) -> int:
        ps = [0]
        for c in s:
            ps.append(ps[-1] + (1 if c in 'aeiou' else 0))

        n = len(s)
        res = 0
        for i in range(n):
            for j in range(i, n):
                v = ps[j+1] - ps[i]
                c = j - i + 1 - v
                if v == c and (c * v) % k == 0:
                    res += 1
        return res

    # brute force
    def beautifulSubstrings1(self, s: str, k: int) -> int:
        n = len(s)
        res = 0
        m = {'a', 'e', 'i', 'o', 'u'}
        for i in range(n):
            c = v = 0
            for j in range(i, n):
                if s[j] in m:
                    v += 1
                else:
                    c += 1

                if c == v and (c * v) % k == 0:
                    res += 1
        return res


def test_beautiful_substrings():
    solution = Solution()
    assert solution.beautifulSubstrings("baeyh", 2) == 2, 'wrong result'
    assert solution.beautifulSubstrings("abba", 1) == 3, 'wrong result'


if __name__ == '__main__':
    test_beautiful_substrings()
