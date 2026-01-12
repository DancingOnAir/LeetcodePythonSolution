class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - ord('a')] += 1

        MOD = 10 ** 9 + 7
        for _ in range(t):
            z_cnt = cnt[25]
            for i in range(25, 0, -1):
                cnt[i] = cnt[i - 1]
            cnt[0] = z_cnt
            cnt[1] = (cnt[1] + z_cnt) % MOD

        return sum(cnt) % MOD


def test_length_after_transformations():
    solution = Solution()
    assert solution.lengthAfterTransformations("abcyy", 2) == 7, 'wrong result'
    assert solution.lengthAfterTransformations("azbk", 1) == 5, 'wrong result'


if __name__ == '__main__':
    test_length_after_transformations()
