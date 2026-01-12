class Solution:
    def reformatDate(self, date: str) -> str:
        M = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        date = date.split()
        date[0] = date[0][:-2].zfill(2)
        date[1] = str(M.index(date[1]) + 1).zfill(2)
        date[0], date[2] = date[2], date[0]

        return '-'.join(date)


def test_reformat_date():
    solution = Solution()
    assert solution.reformatDate("20th Oct 2052") == "2052-10-20", 'wrong result'
    assert solution.reformatDate("6th Jun 1933") == "1933-06-06", 'wrong result'
    assert solution.reformatDate("26th May 1960") == "1960-05-26", 'wrong result'


if __name__ == '__main__':
    test_reformat_date()
