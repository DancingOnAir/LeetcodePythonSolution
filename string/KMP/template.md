## reference
https://www.cnblogs.com/zzuuoo666/p/9028287.html
https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/solutions/732461/dai-ma-sui-xiang-lu-kmpsuan-fa-xiang-jie-mfbs/

## 各种含义
next数组各值的含义：代表当前字符之前的字符串中，有多大长度的相同前缀后缀。例如如果next[j] = k，代表j之前的字符串中有最大长度为k的相同前缀后缀。
eg. 在字符串"abcabd"中，最后的字符d的next值为2，因为它前面的字符串"abcab"最长的相同前缀后缀为"ab"，长度为2
