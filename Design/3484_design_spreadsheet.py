from collections import defaultdict


class Spreadsheet:
    def __init__(self, rows: int):
        self.m = defaultdict(int)

    def setCell(self, cell: str, value: int) -> None:
        self.m[cell] = value

    def resetCell(self, cell: str) -> None:
        self.m[cell] = 0

    def getValue(self, formula: str) -> int:
        res = 0
        for x in formula[1:].split('+'):
            if x.isdigit():
                res += int(x)
            else:
                res += self.m[x]
        return res


def test_spread_sheet():
    spreadSheet = Spreadsheet(3)
    assert spreadSheet.getValue("=5+7") == 12, 'wrong result'
    spreadSheet.setCell("A1", 10)
    assert spreadSheet.getValue("=A1+6") == 16, 'wrong result'
    spreadSheet.setCell("B2", 15)
    assert spreadSheet.getValue("=A1+B2") == 25, 'wrong result'
    spreadSheet.resetCell("A1")
    assert spreadSheet.getValue("=A1+B2") == 15, 'wrong result'


if __name__ == '__main__':
    test_spread_sheet()
