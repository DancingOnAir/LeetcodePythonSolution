import re


class Solution:
    def entityParser(self, text: str) -> str:
        entity_symbol_list = [('&quot;', '\"'), ('&apos;', '\''), ('&gt;', '>'), ('&lt;', '<'), ('&frasl;', '/'), ('&amp;', '&')]
        for pat, rep in entity_symbol_list:
            text = re.sub(pat, rep, text)
        return text

    def entityParser1(self, text: str) -> str:
        entity_symbol_dict = dict()
        entity_symbol_dict['&quot;'] = "\""
        entity_symbol_dict['&apos;'] = "'"
        entity_symbol_dict['&amp;'] = '&'
        entity_symbol_dict['&gt;'] = '>'
        entity_symbol_dict['&lt;'] = '<'
        entity_symbol_dict['&frasl;'] = '/'

        # for k, v in entity_symbol_dict.items():
        #     if k in text:
        #         text = text.replace(k, v)

        n = len(text)
        if n < 3:
            return text

        res = ''
        i = 0
        while i < n:
            if text[i] == '&':
                j = i + 1
                while j < n and text[j] != ';' and text[j] != '&':
                    j += 1

                if j == n:
                    res += text[i: j + 1]
                    return res
                elif text[j] == ';':
                    if text[i: j + 1] in entity_symbol_dict:
                        res += entity_symbol_dict[text[i: j + 1]]
                    else:
                        res += text[i: j + 1]
                    i = j + 1
                elif text[j] == '&':
                    res += text[i: j]
                    i = j
            else:
                res += text[i]
                i += 1

        return res


def test_entity_parser():
    solution = Solution()
    # assert solution.entityParser("&amp; is an HTML entity but &ambassador; is not.") == "& is an HTML entity but &ambassador; is not.", 'wrong result'
    # assert solution.entityParser("and I quote: &quot;...&quot;") == "and I quote: \"...\"", "wrong result"
    # assert solution.entityParser("Stay home! Practice on Leetcode :)") == "Stay home! Practice on Leetcode :)", "wrong result"
    # assert solution.entityParser("x &gt; y &amp;&amp; x &lt; y is always false") == "x > y && x < y is always false", "wrong result"
    # assert solution.entityParser("leetcode.com&frasl;problemset&frasl;all") == "leetcode.com/problemset/all", "wrong result"
    # assert solution.entityParser("&amp;gt;") == "&gt;", "wrong result"
    assert solution.entityParser("&&gt;") == "&>", "wrong result"


if __name__ == '__main__':
    test_entity_parser()
