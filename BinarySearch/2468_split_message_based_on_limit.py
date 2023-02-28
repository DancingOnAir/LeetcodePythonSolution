from typing import List


class Solution:
    # 此题不能用二分，因为不是一个增量的问题，当分割次数少可能不够分，分割次数多可能占用的字符数多，也不够分。
    # 二分错误解法如下
    def splitMessage(self, message: str, limit: int) -> List[str]:
        def possible(x):
            # 1-9, 10-99, 100-999, 1000-9999
            # pre_sum = [9, 90*2, 900*3, 9000*4]
            if len(str(x)) * 2 + 3 >= limit:
                return False

            if x > 9999:
                m = 38889 + (x - 9999) * 5
            elif x > 999:
                m = 2889 + (x - 999) * 4
            elif x > 99:
                m = 189 + (x - 99) * 3
            elif x > 9:
                m = 9 + (x - 9) * 2
            else:
                m = x
            return limit * x >= n + (3 + len(str(x))) * x + m

        if limit < 6:
            return []

        n = len(message)
        left, right = n // (limit - 5), n
        while left <= right:
            mid = left + (right - left) // 2
            if possible(mid):
                right = mid - 1
            else:
                left = mid + 1

        if left > n:
            return []

        res = list()
        i = 0
        for j in range(1, left + 1):
            d = limit - len(str(j)) - len(str(left)) - 3
            res.append('%s<%s/%s>' % (message[i: i + d], j, left))
            i += d
        return res


def test_split_message():
    solution = Solution()
    assert solution.splitMessage("bab aba baaaba", 7) == ["ba<1/7>","b <2/7>","ab<3/7>","a <4/7>","ba<5/7>","aa<6/7>","ba<7/7>"], 'wrong result'
    assert solution.splitMessage("abbababbbaaa aabaa a", 8) == ["abb<1/7>","aba<2/7>","bbb<3/7>","aaa<4/7>"," aa<5/7>","baa<6/7>"," a<7/7>"], 'wrong result'
    assert solution.splitMessage("boxpn", 5) == [], 'wrong result'
    assert solution.splitMessage("this is really a very awesome message", 9) == ["thi<1/14>", "s i<2/14>", "s r<3/14>",
                                                                                 "eal<4/14>", "ly <5/14>", "a v<6/14>",
                                                                                 "ery<7/14>", " aw<8/14>", "eso<9/14>",
                                                                                 "me<10/14>", " m<11/14>", "es<12/14>",
                                                                                 "sa<13/14>",
                                                                                 "ge<14/14>"], 'wrong result'
    assert solution.splitMessage("short message", 15) == ["short mess<1/2>", "age<2/2>"], 'wrong result'


if __name__ == '__main__':
    test_split_message()
