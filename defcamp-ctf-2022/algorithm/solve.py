
def polinom(n, m):
   i = 0
   z = []
   s = 0
   while n > 0:
   	if n % 2 != 0:
   		z.append(2 - (n % 4)) # 2, 1, 0, -1
   	else:
   		z.append(0)
   	n = (n - z[i])/2
   	i = i + 1
   z = z[::-1]
   l = len(z)
   for i in range(0, l):
       s += z[i] * m ** (l - 1 - i) #
   return s



daem = dict()
for i in range(1, 99):
    daem[str(int(polinom(i, 3)))] = str(i).rjust(2, '0')



r = 242712673639869973827786401934639193473972235217215301

# can be optimized using dp, but don't care rn.
def recurse(r, carry, res):
    
    if r == '':
        if carry not in daem:
            pass
        else:
            # Brute last character to avoid mistake if odd len
            for i in range(99):
                try:
                    print((hex(int(res+str(i)))[2:-1]).decode('hex'))
                except:
                    pass
           
    elif len(carry) > 5:
        pass
    else:
        if carry in daem:
            recurse(r[1:], r[0], res + daem[carry])
        recurse(r[1:], carry + r[0], res)


recurse(str(r), '', '')
