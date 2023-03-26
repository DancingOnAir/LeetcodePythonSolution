from typing import List


class SummaryRanges:

    def __init__(self):

    def addNum(self, value: int) -> None:

    def getIntervals(self) -> List[List[int]]:


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
