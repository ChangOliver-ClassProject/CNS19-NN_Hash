import matplotlib.pyplot as plt
import numpy as np
import os

def toggle_message(m):
	mb = ''.join([bin(ord(c))[2:].rjust(8,'0') for c in m])
	file = open("test.txt", "w")
	file.write(m + '\n')

	for x in range(len(m)*8):
		if (mb[x] == '1'):
			mb = list(mb)
			mb[x] = '0'
			mb = ''.join(mb)
			m_toggle = ''.join(chr(int(mb[i*8:i*8+8],2)) for i in range(len(mb)//8))
			file.write(m_toggle+'\n')
			mb = list(mb)
			mb[x] = '1'
			mb = ''.join(mb)
		else:
			mb = list(mb)
			mb[x] = '1'
			mb = ''.join(mb)
			m_toggle = ''.join(chr(int(mb[i*8:i*8+8],2)) for i in range(len(mb)//8))
			file.write(m_toggle+'\n')
			mb = list(mb)
			mb[x] = '0'
			mb = ''.join(mb)	
	
	file.close()

def find_collision(m, block_size):
	
	toggle_message(m)
	os.system("python refresh.py 16 {}".format(block_size))
	os.system("python hashing.py test.txt 16 {}".format(block_size))

	read_file = open("output.txt", "r")

	s = set()
	cnt = 0
	for msg in read_file:
		s.add(msg)
		if (len(s) == cnt):
			print(msg, end = '')
			print("blocksize {} find collision!".format(block_size))
			return
		else:
			cnt += 1

	print("blocksize {} no collision!".format(block_size))

	read_file.close()

def main():
	'''
	m = "A cryptographic hash function is a special class of hash function that has certain properties which make it suitable for use in cryptography. It is a mathematical algorithm that maps data of arbitrary size to a bit string of a fixed size (a hash) and is designed to be a one-way function, that is, a function which is infeasible to invert. The only way to recreate the input data from an ideal cryptographic hash function's output is to attempt a brute-force search of possible inputs to see if they produce a match, or use a rainbow table of matched hashes. Bruce Schneier has called one-way hash functions \"the workhorses of modern cryptography\". The input data is often called the message, and the output (the hash value or hash) is often called the message digest or simply the digest.A cryptographic hashA cryptographic hashA cryptographic A cryptographic hash function is a special class of hash function that has certain properties which make it suitable for use in cryptography.A cryptographic hash function is a special class of hash function that has certain properties which make it suitable for use in cryptography.np.arange(len(m)*8), hdr, 0.0001, linewidth=1"
	m = m+m+m+m
	print(len(m))
	find_collision(m, 20480)
'''
	x = [32, 64, 96, 128, 160, 192, 224, 256, 288, 320, 352, 384, 416, 448, 480, 512, 1024, 1120, 1152, 2048]
	y = [60, 92, 121, 149, 163, 196, 229, 261, 253, 281, 309, 337, 366, 392, 422, 426, 615, 737, 844, 1144]
	
	#poly = np.polyfit(x,y,5)
	#poly_y = np.poly1d(poly)(x)
	#plt.plot(x, poly_y, 0.0001, linewidth=3)
	plt.plot(x, y, 0.0001, linewidth=3)
	plt.xlabel("Block size", fontsize=12, ha="center")
	plt.ylabel("Word count", fontsize=12, ha="center")
	plt.xticks(np.arange(32, 2048, 64), fontsize=8)
	plt.yticks(fontsize=8)
	plt.show()

main()