from collections import Counter


class Solution:
    def reorderSpaces(self, text: str) -> str:
        space_count = Counter(text)[' ']
        words = str.split(text)
        n = len(words)

        if n > 1:
            q, r = divmod(space_count, n - 1)
            return (' ' * q).join(words) + ' ' * r
        elif space_count > 0:
            return words[0] + ' ' * space_count
        else:
            return text


def test_reorder_spaces():
    solution = Solution()
    assert solution.reorderSpaces("  this   is  a sentence ") == "this   is   a   sentence", 'wrong result'
    assert solution.reorderSpaces(" practice   makes   perfect") == "practice   makes   perfect ", 'wrong result'
    assert solution.reorderSpaces("hello   world") == "hello   world", 'wrong result'
    assert solution.reorderSpaces("  walks  udp package   into  bar a") == "walks  udp  package  into  bar  a ", 'wrong result'
    assert solution.reorderSpaces("a") == "a", 'wrong result'


if __name__ == '__main__':
    test_reorder_spaces()
