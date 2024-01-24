from collections import Counter


class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = sorted(Counter(word).values(), reverse=True)
        return sum(freq[:8] + freq[8: 16] * 2 + freq[16: 24] * 3 + freq[24:] * 4)

    def minimumPushes1(self, word: str) -> int:
        freq = sorted(Counter(word).items(), key=lambda x: -x[1])
        res, cnt = 0, 0
        for k, v in freq:
            cnt += 1
            if cnt < 9:
                res += v
            elif cnt < 17:
                res += v * 2
            elif cnt < 25:
                res += v * 3
            else:
                res += v * 4
        return res


def test_minimum_pushes():
    solution = Solution()
    assert solution.minimumPushes("abcde") == 5, 'wrong result'
    assert solution.minimumPushes("xyzxyzxyzxyz") == 12, 'wrong result'
    assert solution.minimumPushes("aabbccddeeffgghhiiiiii") == 24, 'wrong result'


if __name__ == '__main__':
    test_minimum_pushes()
