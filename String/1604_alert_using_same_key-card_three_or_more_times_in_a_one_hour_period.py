from typing import List


class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        d = dict()
        for name, time in zip(keyName, keyTime):
            if name not in d:
                d[name] = [time]
            else:
                d[name].append(time)

        res = []
        for k in d:
            d[k].sort()
            for i in range(len(d[k]) - 2):
                t = d[k][i]
                t_after_one_hour = '%02d' % (int(t[:2]) + 1) + t[2:]

                if d[k][i + 2] <= t_after_one_hour:
                    res.append(k)
                    break

        res.sort()
        return res


def test_alert_names():
    solution = Solution()

    # keyName1 = ["daniel", "daniel", "daniel", "luis", "luis", "luis", "luis"]
    # keyTime1 = ["10:00", "10:40", "11:00", "09:00", "11:00", "13:00", "15:00"]
    # assert solution.alertNames(keyName1, keyTime1) == ["daniel"], 'wrong result'
    #
    # keyName2 = ["alice", "alice", "alice", "bob", "bob", "bob", "bob"]
    # keyTime2 = ["12:01", "12:00", "18:00", "21:00", "21:20", "21:30", "23:00"]
    # assert solution.alertNames(keyName2, keyTime2) == ["bob"], 'wrong result'
    #
    # keyName3 = ["john", "john", "john"]
    # keyTime3 = ["23:58", "23:59", "00:01"]
    # assert solution.alertNames(keyName3, keyTime3) == [], 'wrong result'
    #
    # keyName4 = ["leslie", "leslie", "leslie", "clare", "clare", "clare", "clare"]
    # keyTime4 = ["13:00", "13:20", "14:00", "18:00", "18:51", "19:30", "19:49"]
    # assert solution.alertNames(keyName4, keyTime4) == ["clare", "leslie"], 'wrong result'

    keyName5 = ["a", "a", "a", "a", "a", "b", "b", "b", "b", "b", "b"]
    keyTime5 = ["23:20", "11:09", "23:30", "23:02", "15:28", "22:57", "23:40", "03:43", "21:55", "20:38", "00:19"]
    assert solution.alertNames(keyName5, keyTime5) == ["a"], 'wrong result'


if __name__ == '__main__':
    test_alert_names()
