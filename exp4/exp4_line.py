
#Author : Oliver Chang

import matplotlib.pyplot as plt
import numpy as np
import hashlib
import os

m = "pneumonoultramicroscopicsilicovolcanoconiosis"

def toggle_message_shamd5():
	mb = ''.join([bin(ord(c))[2:].rjust(8,'0') for c in m])
	file = open("test.txt", "w")
	file_1 = open("sha1.txt", "w")
	file_256 = open("sha256.txt", "w")
	file_md5 = open("md5.txt", "w")
	
	file.write(m + '\n')
	file_1.write(hashlib.sha1(m.encode()).hexdigest() + '\n')
	file_256.write(hashlib.sha256(m.encode()).hexdigest() + '\n')
	file_md5.write(hashlib.md5(m.encode()).hexdigest() + '\n')

	for x in range(len(m)*8):
		if (mb[x] == '1'):
			mb = list(mb)
			mb[x] = '0'
			mb = ''.join(mb)
			m_toggle = ''.join(chr(int(mb[i*8:i*8+8],2)) for i in range(len(mb)//8))
			file.write(m_toggle+'\n')
			file_1.write(hashlib.sha1(m_toggle.encode()).hexdigest() + '\n')
			file_256.write(hashlib.sha256(m_toggle.encode()).hexdigest() + '\n')
			file_md5.write(hashlib.md5(m_toggle.encode()).hexdigest() + '\n')
			mb = list(mb)
			mb[x] = '1'
			mb = ''.join(mb)
		else:
			mb = list(mb)
			mb[x] = '1'
			mb = ''.join(mb)
			m_toggle = ''.join(chr(int(mb[i*8:i*8+8],2)) for i in range(len(mb)//8))
			file.write(m_toggle+'\n')
			file_1.write(hashlib.sha1(m_toggle.encode()).hexdigest() + '\n')
			file_256.write(hashlib.sha256(m_toggle.encode()).hexdigest() + '\n')
			file_md5.write(hashlib.md5(m_toggle.encode()).hexdigest() + '\n')			
			mb = list(mb)
			mb[x] = '0'
			mb = ''.join(mb)	
	
	file.close()
	file_1.close()
	file_256.close()
	file_md5.close()

def hash():
	os.system("python ../Model/refresh.py 2")
	os.system("python ../Model/hashing.py test.txt out8.txt 2")	
	os.system("python ../Model/refresh.py 4")
	os.system("python ../Model/hashing.py test.txt out16.txt 4")	
	os.system("python ../Model/refresh.py 8")
	os.system("python ../Model/hashing.py test.txt out32.txt 8")
	os.system("python ../Model/refresh.py 16")
	os.system("python ../Model/hashing.py test.txt out64.txt 16")
	os.system("python ../Model/refresh.py 32")
	os.system("python ../Model/hashing.py test.txt out128.txt 32")	
	os.system("python ../Model/refresh.py 64")
	os.system("python ../Model/hashing.py test.txt out256.txt 64")	

def Hdr(file, size):
	hdr = []
	file = open(file, "r")
	h = file.read(size+1)
	h = int(h, 16)
	
	for x in range(len(m)*8):
		h1 = file.read(size+1)
		h1 = int(h1, 16)
		hdr += [bin(h ^ h1).count("1") / (size*4)*100]

	file.close()
	return hdr

def main():
	#toggle_message_shamd5()
	#hash()
	
	fig = plt.figure(1)
	fig.suptitle("Diffusion Test", ha="center", fontsize=19, fontweight="bold")
	fig.text(0.07, 0.53, "Hdr (%)", rotation='vertical', fontsize=15)
	fig.text(0.5, 0.04, "Position of changed bit in m", ha="center", fontsize=15)
	
	#SHA-1
	hdr = Hdr("sha1.txt", 40)
	p1 = plt.subplot(3, 3, 1)
	p1.set_title("SHA-1", fontsize=8)
	p1.set_yticks(np.arange(0, 101, 50))
	p1.set_xticks(np.arange(0, 361, 50))
	p1.tick_params(axis="both", labelsize=8)
	p1.set_ylim(0, 101)
	p1.plot(np.arange(len(m)*8), hdr, 0.0001, linewidth=1)

	#SHA-256
	hdr = Hdr("sha256.txt", 64)
	p2 = plt.subplot(3, 3, 2)
	p2.set_title("SHA-256", fontsize=8)
	p2.set_yticks(np.arange(0, 101, 50))
	p2.set_xticks(np.arange(0, 361, 50))
	p2.tick_params(axis="both", labelsize=8)
	p2.set_ylim(0, 101)
	p2.plot(np.arange(len(m)*8), hdr, 0.0001, linewidth=1)

	#MD5
	hdr = Hdr("md5.txt", 32)
	p3 = plt.subplot(3, 3, 3)
	p3.set_title("MD5", fontsize=8)
	p3.set_yticks(np.arange(0, 101, 50))
	p3.set_xticks(np.arange(0, 361, 50))
	p3.tick_params(axis="both", labelsize=8)
	p3.set_ylim(0, 101)
	p3.plot(np.arange(len(m)*8), hdr, 0.0001, linewidth=1)		

	#size 8
	hdr = Hdr("out8.txt", 8)
	p4 = plt.subplot(3, 3, 4)
	p4.set_title("n = 8 (32 bits)", fontsize=8)
	p4.set_yticks(np.arange(0, 101, 50))
	p4.set_xticks(np.arange(0, 361, 50))
	p4.tick_params(axis="both", labelsize=8)
	p4.set_ylim(0, 101)
	p4.plot(np.arange(len(m)*8), hdr, 0.0001, linewidth=1)
	
	#size 16
	hdr = Hdr("out16.txt", 16)
	p5 = plt.subplot(3, 3, 5)
	p5.set_title("n = 16 (64 bits)", fontsize=8)
	p5.set_yticks(np.arange(0, 101, 50))
	p5.set_xticks(np.arange(0, 361, 50))
	p5.tick_params(axis="both", labelsize=8)
	p5.set_ylim(0, 101)
	p5.plot(np.arange(len(m)*8), hdr, 0.0001, linewidth=1)

	#size 32
	hdr = Hdr("out32.txt", 32)
	p6 = plt.subplot(3, 3, 6)
	p6.set_title("n = 32 (128 bits)", fontsize=8)
	p6.set_yticks(np.arange(0, 101, 50))
	p6.set_xticks(np.arange(0, 361, 50))
	p6.tick_params(axis="both", labelsize=8)
	p6.set_ylim(0, 101)
	p6.plot(np.arange(len(m)*8), hdr, 0.0001, linewidth=1)

	#size 64
	hdr = Hdr("out64.txt", 64)
	p7 = plt.subplot(3, 3, 7)
	p7.set_title("n = 64 (256 bits)", fontsize=8)
	p7.set_yticks(np.arange(0, 101, 50))
	p7.set_xticks(np.arange(0, 361, 50))
	p7.tick_params(axis="both", labelsize=8)
	p7.set_ylim(0, 101)
	p7.plot(np.arange(len(m)*8), hdr, 0.0001, linewidth=1)

	#size 128
	hdr = Hdr("out128.txt", 128)
	p8 = plt.subplot(3, 3, 8)
	p8.set_title("n = 128 (512 bits)", fontsize=8)
	p8.set_yticks(np.arange(0, 101, 50))
	p8.set_xticks(np.arange(0, 361, 50))
	p8.tick_params(axis="both", labelsize=8)
	p8.set_ylim(0, 101)
	p8.plot(np.arange(len(m)*8), hdr, 0.0001, linewidth=1)

	#size 256
	hdr = Hdr("out256.txt", 256)
	p9 = plt.subplot(3, 3, 9)
	p9.set_title("n = 256 (1024 bits)", fontsize=8)
	p9.set_yticks(np.arange(0, 101, 50))
	p9.set_xticks(np.arange(0, 361, 50))
	p9.tick_params(axis="both", labelsize=8)
	p9.set_ylim(0, 101)
	p9.plot(np.arange(len(m)*8), hdr, 0.0001, linewidth=1)					

	plt.show()

main()