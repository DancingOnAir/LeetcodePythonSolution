class Solution:
    def sliding_window(self, s: list[int]) -> list[list[int]]:
        res = [[0] * 26 for _ in s]
        for k in range(1, 27):
            cnt = [0] * 26
            kinds = 0
            left = 0
            for i, c in enumerate(s):
                if cnt[c] == 0:
                    kinds += 1
                cnt[c] += 1
                while kinds >= k:
                    cnt[s[left]] -= 1
                    if cnt[s[left]] == 0:
                        kinds -= 1
                    left += 1
                # 右端点为i的合法子串个数; 右端点为 i 时，不同字符种类数 >= k 的子串总数。
                res[i][k - 1] = left
            if left == 0:
                break

        for cnt in res:
            # 至少j种 - 至少j + 1种 = 恰好j种
            for j in range(25):
                if cnt[j + 1] == 0:
                    break
                cnt[j] -= cnt[j + 1]
        return res

    def countMagicalPairs(self, s: str) -> int:
        s = [ord(c) - ord('a') for c in s]
        pre = self.sliding_window(s)
        s.reverse()
        suf = self.sliding_window(s)
        suf.reverse()

        res = 0
        for i in range(len(pre) - 1):
            for p, s in zip(pre[i], suf[i + 1]):
                # 做完差分后，res[i][k - 1] 存储的就是右端点为 i、不同字符种类数恰好为 k 的子串数。
                # 对于一个以固定位置为端点的子串，其所能构成的字符种数 k 必然是从 1 开始的连续整数区间 [1, Kmax]：
                # 当 k <= Kmax 时，方案数 > 0；一旦 k > Kmax，方案数必定恒等于 0。因此：
                # 一旦 p == 0，说明左边子串种类已经达到上限，后续所有更大的 k 对应的 p 必全为 0。
                # 一旦 s == 0，说明右边子串种类已经达到上限，后续所有更大的 k对应的 s 必全为 0
                if p == 0 or s == 0:
                    break
                res += p * s
        return res


def test_count_magical_pairs():
    solution = Solution()
    assert solution.countMagicalPairs("aba") == 2, 'wrong result'
    assert solution.countMagicalPairs("kkk") == 4, 'wrong result'
    assert solution.countMagicalPairs("abcac") == 7, 'wrong result'


if __name__ == '__main__':
    test_count_magical_pairs()
