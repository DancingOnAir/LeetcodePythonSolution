class Solution:
    # sliding window
    def countGoodSubstrings(self, s: str) -> int:
        repeat = res = 0
        cnt = [0] * 26

        for i, c in enumerate(s):
            if cnt[ord(c) - 97] == 1:
                repeat += 1
            cnt[ord(c) - 97] += 1

            if i >= 3:
                if cnt[ord(s[i-3]) - 97] == 2:
                    repeat -= 1
                cnt[ord(s[i-3]) - 97] -= 1

            if i >= 2 and repeat == 0:
                res += 1

        return res

    # set
    def countGoodSubstrings1(self, s: str) -> int:
        n = len(s)
        if n < 3:
            return 0

        res = 0
        for i in range(n - 2):
            if len(set(s[i: i+3])) == 3:
                res += 1
        return res


def test_count_good_substrings():
    solution = Solution()
    assert solution.countGoodSubstrings('xyzzaz') == 1, 'wrong result'
    assert solution.countGoodSubstrings('aababcabc') == 4, 'wrong result'


if __name__ == '__main__':
    test_count_good_substrings()
