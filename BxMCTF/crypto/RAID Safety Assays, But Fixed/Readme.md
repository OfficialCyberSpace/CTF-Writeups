#Description :
```
Author: cg

The flag to this challenge is all lowercase, with no underscores.

e = 65537
n = 4629059450272139917534568159172903078573041591191268130667
c = 6743459147531103219359362407406880068975344190794689965016

main.py:

from Crypto.Util.number import *
import random

p = getPrime(96)
q = getPrime(96)
n = p*q
e = 65537

flag = b'ctf{0000000000000000}'
flag = str(pow(bytes_to_long(flag), e, n))

perm = list(range(10))
random.shuffle(perm)
perm = list(map(str, perm))

c = ''.join([perm[int(x)] for x in flag])

print(f'e = {e}')
print(f'n = {n}')
print(f'c = {c}')
```

Analysing the script I realized that the value given was not the correct value of c, but a mere projection of the perm list randomly generated.
It is possible to solve this pretty fast since the length of the perm list is only ten by bruteforcing all possible permutations of the perm list.

#Solution :

```py
from Crypto.Util.number import *
from pwn import *
import random
import itertools
n = 4629059450272139917534568159172903078573041591191268130667
e = 65537
c = 6743459147531103219359362407406880068975344190794689965016

# Factorize n to obtain p and q
p, q = 62682123970325402653307817299, 73849754237166590568543300233
e = 65537
phi = (p-1)*(q-1)
d = inverse(e, phi)
lst = list(range(10))
for perm in itertools.permutations(lst):
    perm = list(map(str, perm))
    b = ''.join([perm[int(x)] for x in str(c)])
    # Decrypt the ciphertext
    m = pow(int(b), d, n)
    if long_to_bytes(m).startswith(b'ctf'):
        print(long_to_bytes(m))
```
