class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()

    def toLowerCase1(self, s: str) -> str:
        return ''.join(chr(ord(ch) + (32 if 64 < ord(ch) < 91 else 0)) for ch in s)
