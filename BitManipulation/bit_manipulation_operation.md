1. 位运算公式总结
   1. lowbit(i) 即i & -i, 返回i的最后一位1 
   2. n>>k & 1, 求n的第k位数字 
   3. x | (1 << k), 将x第k位 置为1 
   4. x ^ (1 << k), 将x第k位取反 
   5. x & (x - 1), 将x最右边的1置为0(去掉最右边的1)
   6. x | (x + 1), 将x最右边的0置为1 
   7. x & 1, 判断奇偶性 真为奇，假为偶
   
2. 运算符的性质 
   1. ^运算符 
      1. 任何数异或0是它本身, a ^ 0 = a 
      2. 两个相同的数异或为0, a ^ a = 0 
      3. 异或满足结合律交换律（异或符号也可以用⊕表示）, a ^ (b ^ c) = (a ^ b) ^ c, a ^ b = b ^ a 
   2. |运算符 
      1. 一个数或0还是这个数, a | 0 = a 
      2. 相关运算, a | ~a = 1（此时的a只代表0和1）, a | a = a 
      3. 满足结合律和交换律, ( a | b ) | c = a | ( b | c), a | b = b | a 
   3. &运算符 
      1. 一个数与0为0, a & 0 = 0 
      2. a & ~a = 0 
      3. a & a = a 
      4. 满足交换律和结合律, a & b = b & a, ( a & b ) & c = a & ( b & c )
   4. 组合性质 
      1. 分配律
         1. a & ( b | c ) = ( a & b ) | ( a & c )
         2. a ^ ( b | c ) = ( a ^ b) | (a ^ c)
      2. 其它性质 
         1. a | ( a & b ) = a 
         2. a & ( a | b ) = a


3. bit mask
   1. To set a bit to 1: mask = mask | (1 << bitIndex)
   2. To set a bit to 0: mask = mask & ~(1 << bitIndex)
   3. To get a bit (to be able to check it): (mask & (1 << bitIndex)) != 0
