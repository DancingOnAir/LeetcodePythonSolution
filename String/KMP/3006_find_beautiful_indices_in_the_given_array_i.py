from typing import List


class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        def get_next(ss):
            nxt = [0] * len(ss)
            j = 0
            for i in range(1, len(ss)):
                while j > 0 and ss[i] != ss[j]:
                    j = nxt[j - 1]
                if ss[i] == s[j]:
                    j += 1
                nxt[i] = j
            return nxt

        nxt_a = get_next(a)
        nxt_b = get_next(b)

        ja, jb = 0, 0
        pa, pb = [], []
        la, lb = len(a), len(b)
        for i in range(len(s)):
            while ja > 0 and s[i] != a[ja]:
                ja = nxt_a[ja - 1]
            if s[i] == a[ja]:
                ja += 1
            if ja == la:
                pa.append(i - la + 1)
                ja = 0

            while jb > 0 and s[i] != b[jb]:
                jb = nxt_b[jb - 1]
            if s[i] == b[jb]:
                jb += 1
            if jb == lb:
                pb.append(i - lb + 1)
                jb = 0

        res = []
        for x in pa:
            for y in pb:
                if y > x + k:
                    break
                if (x - k) <= y <= (x + k):
                    res.append(x)
                    break
        return res


def test_beautiful_indices():
    solution = Solution()
    assert solution.beautifulIndices("isawsquirrelnearmysquirrelhouseohmy", "my", "squirrel", 15) == [16, 33], 'wrong result'
    assert solution.beautifulIndices("abcd", "a", "a", 4) == [0], 'wrong result'


if __name__ == '__main__':
    test_beautiful_indices()
