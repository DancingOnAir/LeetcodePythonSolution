from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if not k:
            return [0] * len(code)

        res = []
        n = len(code)
        if k > 0:
            for i in range(n):
                if i + k < n:
                    res.append(sum(code[i + 1:i + k + 1]))
                else:
                    res.append(sum(code[i+1:] + code[:(i+k) % n + 1]))
        else:
            for i in range(n):
                if i + k >= 0:
                    res.append(sum(code[i+k:i]))
                else:
                    res.append(sum(code[:i] + code[i+k:]))
        return res


def test_decrypt():
    solution = Solution()

    code1 = [5, 7, 1, 4]
    k1 = 3
    res1 = [12, 10, 16, 13]
    assert solution.decrypt(code1, k1) == res1, "wrong result"

    code2 = [1, 2, 3, 4]
    k2 = 0
    res2 = [0, 0, 0, 0]
    assert solution.decrypt(code2, k2) == res2, "wrong result"

    code3 = [2, 4, 9, 3]
    k3 = -2
    res3 = [12, 5, 6, 13]
    assert solution.decrypt(code3, k3) == res3, "wrong result"


if __name__ == '__main__':
    test_decrypt()

