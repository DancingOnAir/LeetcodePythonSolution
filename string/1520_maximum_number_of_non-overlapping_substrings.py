from typing import List


class Solution:
    # https://en.wikipedia.org/wiki/Interval_scheduling
    # https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/discuss/744420/C%2B%2BJavaPython-Interval-Scheduling-Maximization-(ISMP)
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        left = {c: i for i, c in reversed(list(enumerate(s)))}
        right = {c: i for i, c in enumerate(s)}

        res = list()
        pre = -1
        for i in sorted(right.values()):
            l, r = left[s[i]], right[s[i]]
            j = r
            while j >= l > pre and r == i:
                l = min(l, left[s[j]])
                r = max(r, right[s[j]])
                j -= 1

            if l > pre and r == i:
                res.append(s[l: r+1])
                pre = r
        return res

    def maxNumOfSubstrings1(self, s: str) -> List[str]:
        d = dict()
        for i, c in enumerate(s):
            if c not in d:
                d[c] = [i, i]
            else:
                d[c][1] = i
        indexes = list(d.values())

        # after expanding left & right, no more partial overlap
        def expand(l, r):
            seen = set()
            left, right = l, r
            for i in range(l, r+1):
                if s[i] not in seen:
                    seen.add(s[i])
                    left = min(left, d[s[i]][0])
                    right = max(right, d[s[i]][1])
            return left, right

        for i, [l, r] in enumerate(indexes):
            left, right = l, r
            while (left, right) != expand(left, right):
                left, right = expand(left, right)
            indexes[i] = (left, right)
        # clear duplicates
        indexes = sorted(list(set(indexes)))

        i = 1
        while i < len(indexes):
            # coz no partial overlap & no duplicates, after sorting, there are 2 situations:
            # case 1. indexes[i-1][0] < indexes[i][0] <= indexes[i][1] < indexes[i][1]
            # case 2. indexes[i - 1] is part of indexes[i]
            if indexes[i][0] > indexes[i - 1][1]:
                i += 1
            else:
                indexes.pop(i - 1)

        res = [s[l:r+1] for l, r in indexes]
        return res


def test_max_num_of_substrings():
    solution = Solution()

    assert sorted(solution.maxNumOfSubstrings('bbcacbaba')) == sorted(["bbcacbaba"]), 'wrong result'
    assert sorted(solution.maxNumOfSubstrings('adefaddaccc')) == sorted(["e", "f", "ccc"]), 'wrong result'
    assert sorted(solution.maxNumOfSubstrings('abbaccd')) == sorted(["d", "bb", "cc"]), 'wrong result'


if __name__ == '__main__':
    test_max_num_of_substrings()
