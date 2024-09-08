from typing import List
from math import log10
from collections import defaultdict, Counter


class Solution:
    def countPairs(self, nums: List[int]) -> int:
        def swap(x):
            res = {x}
            x = list(x)
            for i in range(8):
                for j in range(i + 1, 8):
                    x[i], x[j] = x[j], x[i]
                    res.add(''.join(x))
                    x[i], x[j] = x[j], x[i]
            return res

        ss = map(lambda x: str(x).zfill(8), nums)
        cnt = Counter()
        res = 0
        for s in ss:
            cur = set()
            for v in swap(s):
                cur |= swap(v)
            for v in cur:
                res += cnt[v]
            cnt[s] += 1
        return res

    def countPairs1(self, nums: List[int]) -> int:
        # 从小到大排序，因为100能转变成1,不予处理的话1不能转成100
        nums.sort()
        res = 0
        cnt = defaultdict(int)
        for x in nums:
            st = {x}
            s = list(str(x))
            m = len(s)
            for i in range(m):
                for j in range(i + 1, m):
                    s[i], s[j] = s[j], s[i]
                    st.add(int(''.join(s)))
                    for p in range(i + 1, m):
                        for q in range(i + 1, m):
                            s[p], s[q] = s[q], s[p]
                            st.add(int(''.join(s)))
                            s[p], s[q] = s[q], s[p]
                    s[i], s[j] = s[j], s[i]
            res += sum(cnt[k] for k in st)
            cnt[x] += 1

        return res


def test_count_pairs():
    solution = Solution()
    assert solution.countPairs([1023, 2310, 2130, 213]) == 4, 'wrong result'
    assert solution.countPairs([1, 10, 100]) == 3, 'wrong result'


if __name__ == '__main__':
    test_count_pairs()
