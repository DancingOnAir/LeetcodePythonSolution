class Solution:
    def sortVowels(self, s: str) -> str:
        m = []
        st = set()
        for i, c in enumerate(s):
            if c.lower() in 'aeiou':
                m.append([i, c])
                st.add(i)
        m.sort(key=lambda x: x[1], reverse=True)

        res = []
        for i, c in enumerate(s):
            if i in st:
                res.append(m[-1][1])
                m.pop()
            else:
                res.append(c)
        return ''.join(res)


def test_sort_vowels():
    solution = Solution()
    assert solution.sortVowels("lEetcOde") == 'lEOtcede', 'wrong result'
    assert solution.sortVowels("lYmpH") == 'lYmpH', 'wrong result'


if __name__ == '__main__':
    test_sort_vowels()
