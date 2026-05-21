from collections import Counter


class Solution:
    def countWordOccurrences(self, chunks: list[str], queries: list[str]) -> list[int]:
        s = "".join(chunks).replace("--", " ")
        cnt = Counter(w.strip('-') for w in s.split())
        return [cnt[q] for q in queries]

    def countWordOccurrences1(self, chunks: list[str], queries: list[str]) -> list[int]:
        s = []
        for i, chunk in enumerate(chunks):
            for j, c in enumerate(chunk):
                if c == '-':
                    pre = (j > 0 and chunk[j - 1].islower()) or (j == 0 and i > 0 and chunks[i - 1][-1].islower())
                    suf = (j < len(chunk) - 1 and chunk[j + 1].islower()) or (j == len(chunk) - 1 and i < len(chunks) - 1 and chunks[i + 1][0].islower())
                    if pre and suf:
                        s.append(c)
                    else:
                        s.append(' ')
                else:
                    s.append(c)

        cnt = Counter(''.join(s).split())
        res = []
        for q in queries:
            res.append(cnt[q])
        return res


def test_count_word_occurrences():
    solution = Solution()
    # assert solution.countWordOccurrences(["hello wor", "ld hello"], queries=["hello", "world", "wor"]) == [2, 1, 0], 'wrong result'
    assert solution.countWordOccurrences(["a-b a--b ", "a-", "b"], queries=["a-b", "a", "b"]) == [2, 1, 1], 'wrong result'
    assert solution.countWordOccurrences(["-cat dog- mouse"], queries=["cat", "dog", "mouse", "cat-dog"]) == [1, 1, 1, 0], 'wrong result'


if __name__ == '__main__':
    test_count_word_occurrences()
