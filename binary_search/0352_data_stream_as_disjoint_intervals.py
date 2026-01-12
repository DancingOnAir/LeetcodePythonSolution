from typing import List
from bisect import bisect_left, insort_left


# binary search
# python数组技巧 a[i:j] = []表示删除i到j-1里的元素, a[i:i] = x表示在i的位置插入x
class SummaryRanges:
    def __init__(self):
        # 添加哨兵，注意开头结尾不要设[-1, -1]和[10001, 10001]，因为value可能为0, 当header = -1，有可能区间连起来.
        self.intervals = [[-10, -10], [10010, 10010]]

    def addNum(self, value: int) -> None:
        left, right = 0, len(self.intervals) - 2
        while left <= right:
            mid = left + (right - left) // 2
            if self.intervals[mid][0] == value:
                return
            elif self.intervals[mid][0] < value:
                left = mid + 1
            else:
                right = mid - 1

        cur = [value, value]
        pre = self.intervals[left - 1]
        nxt = self.intervals[left]
        if pre[0] <= value <= pre[1] or nxt[0] <= value <= nxt[1]:
            return
        elif pre[1] + 1 == value and value == nxt[0] - 1:
            pre[1] = nxt[1]
            self.intervals[left: left + 1] = []
        elif pre[1] + 1 == value:
            pre[1] = value
        elif nxt[0] - 1 == value:
            nxt[0] = value
        else:
            self.intervals[left:left] = [cur]

    def getIntervals(self) -> List[List[int]]:
        return self.intervals[1:-1]


# bisect.insort_left
class SummaryRanges1:
    def __init__(self):
        self.stream = list()

    def addNum(self, value: int) -> None:
        insort_left(self.stream, value)

    def getIntervals(self) -> List[List[int]]:
        res = list()
        start = -1
        for i in range(len(self.stream)):
            if start == -1:
                start = self.stream[i]

            if i < len(self.stream) - 1 and self.stream[i] == self.stream[i + 1]:
                continue

            if i < len(self.stream) - 1 and self.stream[i] + 1 == self.stream[i + 1]:
                continue

            res.append([start, self.stream[i]])
            if i < len(self.stream) - 1:
                start = self.stream[i + 1]
        return res


def test_summary_ranges():
    obj = SummaryRanges()
    obj.addNum(1)
    print(obj.getIntervals())
    obj.addNum(3)
    print(obj.getIntervals())
    obj.addNum(7)
    print(obj.getIntervals())
    obj.addNum(2)
    print(obj.getIntervals())
    obj.addNum(6)
    print(obj.getIntervals())


if __name__ == '__main__':
    test_summary_ranges()
