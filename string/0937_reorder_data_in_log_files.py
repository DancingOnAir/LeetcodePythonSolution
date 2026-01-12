from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = list()
        digit_logs = list()

        for log in logs:
            if log.split()[1].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append(log)

        letter_logs = sorted(letter_logs, key=lambda x: (x.split()[1:], x.split()[0]))
        return letter_logs + digit_logs


def test_reorder_log_files():
    solution = Solution()

    assert solution.reorderLogFiles(
        ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]) == ["let1 art can",
                                                                                               "let3 art zero",
                                                                                               "let2 own kit dig",
                                                                                               "dig1 8 1 5 1",
                                                                                               "dig2 3 6"], 'wrong result'
    assert solution.reorderLogFiles(["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]) == [
        "g1 act car", "a8 act zoo", "ab1 off key dog", "a1 9 2 3 1", "zo4 4 7"], 'wrong result'


if __name__ == '__main__':
    test_reorder_log_files()
