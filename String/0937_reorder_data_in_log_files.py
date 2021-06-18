from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = list()
        digit_logs = list()

        for log in logs:
            log_list = log.split()
            identifier = log_list[0]
            content = ' '.join(log_list[1:])
            if content[0].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append([identifier, content])

        letter_logs = sorted(letter_logs, key=lambda x: (x[1], x[0]))
        return [' '.join(x) for x in letter_logs] + digit_logs


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
