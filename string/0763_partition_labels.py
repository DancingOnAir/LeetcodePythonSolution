from typing import List
from collections import Counter


class Solution:
    # last position
    def partitionLabels(self, s: str) -> List[int]:
        last = {c: i for i, c in enumerate(s)}

        res = []
        cnt, mx = 0, 0
        for i, c in enumerate(s):
            cnt += 1
            mx = max(mx, last[c])
            if mx == i:
                res.append(cnt)

                cnt = 0
                mx = 1
        return res

    # Counter
    def partitionLabels1(self, s: str) -> List[int]:
        c = Counter(s)
        cnt = 0
        m = set()
        res = []
        for i, ch in enumerate(s):
            c[ch] -= 1
            m.add(ch)
            cnt += 1

            if all(c[x] == 0 for x in m):
                res.append(cnt)
                cnt = 0
                m.clear()

        return res


def test_partition_labels():
    solution = Solution()
    assert solution.partitionLabels("caedbdedda") == [1, 9], 'wrong result'
    assert solution.partitionLabels("ababcbacadefegdehijhklij") == [9,7,8], 'wrong result'
    assert solution.partitionLabels("eccbbbbdec") == [10], 'wrong result'


if __name__ == '__main__':
    test_partition_labels()
