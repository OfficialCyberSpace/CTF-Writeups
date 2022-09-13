from pwn import *

def main():
	r = remote("104.197.118.147",10100)
	intro = r.recvuntil(b'choice:') # Round 1
	x = 3
	y = 3
	r.sendline(b'D\n')
	sending = "{0} {1}".format(x,y)
	r.sendafter(':', bytes(sending,'utf-8'))
	response = r.recvline()
	print("RESPONSE", response)
	print(r.recvline())
	r.recvline()
	x += 1
	while b'find an egg' not in response: # continue
		print(response)
		r.sendafter(b'choice:', b'D\n')
		r.sendafter(b':', str(x) + " " + str(y) + "\n")
		x += 1
		if x == 10:
			x = 0
			y += 1
		response = r.recvline()
	r.sendafter(b'choice:', b'S\n')

	for o in range(0 , 20): # Round 2
		guess = 500
		low = 0
		high = 1000	
		for i in range(0, 10):
			r.sendafter(b'choice: ',b'P\n')
			r.sendafter(b'(1-1000): ',bytes("{0}\n".format(guess), 'utf-8'))
			ans = r.recvline()
			print(ans)
			print(str(guess))
			if b'small' in ans:
				low = guess
				tmp = (high + low) / 2
				if tmp % 1 != 0:
					tmp -= .5
				guess = int(tmp)
			elif b'big' in ans:
				high = guess
				tmp = (high + low) / 2
				if tmp % 1 != 0:
					tmp -= .5
				guess = int(tmp)
			else:
				break
	u = 0
	v = 0
	r = 0
	for o in range(1, 25):
		r.sendafter(b'choice:', b'P\n')
		sending = str(u) + " " + str(v) + '\n'
		tmp 
		r.sendafter(b'space:',sending)
		print(r.recvline())
		
	r.sendafter(b'choice:',b'P\n')
	r.sendafter(b'space:',b'5354228880 0')
	r.interactive()
	print("DIDN'T get it")
	print(r.recvline())
	print(r.recvline())
	
while True:
	try:
		main()
	except:
		print('issue happened. Restarting')
