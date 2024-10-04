# RSA

- Category: Crypto
- Points: 50
- Solves: 282

## Description
[https://en.wikipedia.org/wiki/RSA_(cryptosystem)](https://en.wikipedia.org/wiki/RSA_(cryptosystem))

[rsa.py](rsa.py)

## Solve
When looking at this challenge, I realized that I could simply reuse a script I used in [twin-prime-rsa](../../buckeyectf-2022/twin-prime-rsa/solve.md) in buckeyeCTF 2022. The write up for that challenge goes in depth on how the encryption process for rsa works.

I went through the exact same steps, finding the p & q values and ran them through the script

```python
import math
import Crypto.Util.number as cun
n= 66082519841206442253261420880518905643648844231755824847819839195516869801231
c = 19146395818313260878394498164948015155839880044374872805448779372117637653026

p = 213055785127022839309619937270901673863
q = 310165339100312907369816767764432814137

e = 65537

phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)

m = pow(c, d, n)
flag = cun.long_to_bytes(m)
print(flag)
```

The flag produced was `bctf{f4c70r1z3_b3773r_4d3b35e4}`


Flag found!