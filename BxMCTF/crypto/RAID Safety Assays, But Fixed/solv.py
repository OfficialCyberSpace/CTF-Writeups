from Crypto.Util.number import *
from pwn import *
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
