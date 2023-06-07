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
