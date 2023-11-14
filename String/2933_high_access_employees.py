from typing import List
from collections import defaultdict


class Solution:
    # change str into num
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        res = []
        m = defaultdict(list)
        for name, time in access_times:
            m[name].append(int(time))

        for k, v in m.items():
            if len(v) < 3:
                continue

            v.sort()
            for i in range(len(v) - 2):
                if v[i + 2] - v[i] < 100:
                    res.append(k)
                    break
        return res

    # str manipulate
    def findHighAccessEmployees1(self, access_times: List[List[str]]) -> List[str]:
        res = []
        m = defaultdict(list)
        for name, time in access_times:
            m[name].append(time)

        for k, v in m.items():
            if len(v) < 3:
                continue

            v.sort()
            for i in range(len(v) - 2):
                if str(int(v[i][:2]) + 1).zfill(2) + v[i][2:] > v[i + 2]:
                    res.append(k)
                    break
        return res


def test_find_high_access_employees():
    solution = Solution()
    assert solution.findHighAccessEmployees(
        [["a", "0549"], ["b", "0457"], ["a", "0532"], ["a", "0621"], ["b", "0540"]]) == ["a"], 'wrong result'
    assert solution.findHighAccessEmployees(
        [["d", "0002"], ["c", "0808"], ["c", "0829"], ["e", "0215"], ["d", "1508"], ["d", "1444"], ["d", "1410"],
         ["c", "0809"]]) == ["d", "c"], 'wrong result'
    assert solution.findHighAccessEmployees(
        [["cd", "1025"], ["ab", "1025"], ["cd", "1046"], ["cd", "1055"], ["ab", "1124"], ["ab", "1120"]]) == ["ab",
                                                                                                              "cd"], 'wrong result'


if __name__ == '__main__':
    test_find_high_access_employees()
