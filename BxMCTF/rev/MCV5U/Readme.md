##Description :

```
Author: Ryzon

Ryzon, who just finished his ICS5U class, forgets that he also needs to finish his final MCV5U assignment, which is due on the same day!

Unfortunately, all of Ryzon's brain cells are destroyed due to how scuffed ICS5U is, and he begs you, his friend, to help him finish this assignment for him.

SPECIAL NOTE, PLEASE READ

The flag format for this problem is different from the rest, it is: ctf{[!-z]{6,128}} (the part inside the bracket can be any string of 6-128 printable ASCII characters, including letters, numbers, and symbols).
```

##Python code:

```py
import math
import hashlib
import sys
SIZE = int(3e5)
VERIFY_KEY = "46e1b8845b40bc9d977b8932580ae44c"
def getSequence(A, B, n, m):
    ans = [0] * (n + m - 1)
    for x in range(n):
        for y in range(m):
            ans[x + y] += A[x] * B[y]
    return ans
A = [0] * SIZE
B = [0] * SIZE

document1 = open("Document 1.txt", "r")
nums1 = document1.readlines()
idx = 0
for num in nums1:
    A[idx] = int(num.strip())
    idx += 1
document2 = open("Document 2.txt", "r")
nums2 = document2.readlines()
idx = 0
for num in nums2:
    B[idx] = int(num.strip())
    idx += 1
sequence = getSequence(A, B, SIZE, SIZE)
val = 0
for num in sequence:
    val = (val + num)
val = str(val)
val_md5 = hashlib.md5(val.encode()).hexdigest()
if val_md5 != VERIFY_KEY:
    print("Wrong solution.")
    sys.exit(1)
key = str(hashlib.sha256(val.encode()).digest())
flag = "ctf{" + "".join(list([x for x in key if x.isalpha() or x.isnumeric()])) + "}"
print(flag)
```

## Solution :
Obviously there is a problem with the time excecution, so we need to find a way to read the data independantly from the calls and loops.
After restructuring the program, I was able to find a python function named Convolve() from the numpy library. 

```py
#!/usr/bin/env python3
import numpy as np
import hashlib
import sys
SIZE = int(3e5)
VERIFY_KEY = "46e1b8845b40bc9d977b8932580ae44c"
#define the sequence using the numpy library convolve function
def getSequence(A, B):
    return np.convolve(A, B)
A = np.zeros(SIZE)
B = np.zeros(SIZE)
# Load the values from the input files
with open("Document 1.txt", "r") as document1:
    nums1 = document1.readlines()
    A[:len(nums1)] = [int(num.strip()) for num in nums1]
with open("Document 2.txt", "r") as document2:
    nums2 = document2.readlines()
    B[:len(nums2)] = [int(num.strip()) for num in nums2]
# Perform the sequence multiplication using the updated getSequence function
sequence = getSequence(A, B)
val = int(np.sum(sequence))
# Check the verification key
val_md5 = hashlib.md5(str(val).encode()).hexdigest()
if val_md5 != VERIFY_KEY:
    print("Wrong solution.")
    sys.exit(1)
obj = ""
key = str(hashlib.sha256(str(val).encode()).digest())
print(key)
# extract the flag
flag = "ctf{" + "".join(list([x for x in key if x.isalpha() or x.isnumeric()])) + "}"
print(flag)
```
