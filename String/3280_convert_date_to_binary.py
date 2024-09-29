class Solution:
    def convertDateToBinary(self, date: str) -> str:
        arr = date.split('-')
        return '-'.join(map(lambda x: bin(int(x))[2:], arr))

    def convertDateToBinary1(self, date: str) -> str:
        return "{0:b}-{1:b}-{2:b}".format(int(date[:4]), int(date[5:7]), int(date[8:]))


def test_convert_date_to_binary():
    solution = Solution()
    assert solution.convertDateToBinary("2080-02-29") == "100000100000-10-11101", 'wrong result'
    assert solution.convertDateToBinary("1900-01-01") == "11101101100-1-1", 'wrong result'


if __name__ == '__main__':
    test_convert_date_to_binary()
