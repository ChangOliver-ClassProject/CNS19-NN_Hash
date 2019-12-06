
#Author: Oliver Chang

import matplotlib.pyplot as plt
import numpy as np
import hashlib

m = "A cryptographic hash function is a special class of hash function that has certain properties which make it suitable for use in cryptography. It is a mathematical algorithm that maps data of arbitrary size to a bit string of a fixed size (a hash) and is designed to be a one-way function, that is, a function which is infeasible to invert. The only way to recreate the input data from an ideal cryptographic hash function's output is to attempt a brute-force search of possible inputs to see if they produce a match, or use a rainbow table of matched hashes. Bruce Schneier has called one-way hash functions \"the workhorses of modern cryptography\". The input data is often called the message, and the output (the hash value or hash) is often called the message digest or simply the digest."
#8_size = "40b26dc2"
#16_size = "fd1159a6e15bc3d1"
size_32 = "6d417dc870157e41432239d61d346160"
size_64 = "cfa33f0e6fba92388e8d96133ad1de00a5f1570016a446689efce32568f4dbb6"
size_128 = "71eddf8fa38917dfc05ad83a29e78c7583e74bf2a8d8379fa55da6ac3669ac8d172c155b537f6dd0bd34423671c73466d5e09c6cd72e2ea41505d7264f72e1da"
size_256 = "274c3cde512c84091018b3a09e7b3b77d07929dbd14c85193369c8ef5b4cd6e92fc656447e88d8cae4d8a5496d9516959b1a8843d6ec3810778f5809acfb4fbd9457837fa7f5dbc912b015d274f054f8244ac1c2378894bb45c3ab6488624b41a094e51f84bb18698b20c7e9c5ac331e604061f4e8c73cfe793910ce575ba3e2"
#size_512 = "c462beee6b2c8702d6d04adb3f6031a3c3c3999a3e44220b9dbd38d0e71baf0e914cafc94d777eb5c0226920d0934016282374b3401e6032d333ad65666a4507247b8595c5fa66d6820b687133c6b09db95a70a0481d85b73dfccb99bacf4caa61a6af88b1cecbc546ba8c67e4045c9dc172d85bbee63d82bbf7437478f3de506cb9b50e4626e2b1ca2fb6035886a79a773e11475f68e1d86f60e2629373a7fdde92a137434f1676a5d1b05eaf2add8d7398c7bd2884d444271edce673e86155e3d3e71653454c8ed4662a6a2e6f4a819ca72bef6edb2c8a490f2c99355f852f82a296d3d7114461c9f3937841639cccdb37930b5128e6783671e161c793481d"
sha1 = hashlib.sha1(m.encode()).hexdigest()
sha256 = hashlib.sha256(m.encode()).hexdigest()
md5 = hashlib.md5(m.encode()).hexdigest()

def main():

	fig = plt.figure(1)
	fig.suptitle("Distribution Test", ha="center", fontsize=19, fontweight="bold")
	fig.text(0.5, 0.04, "Position", ha="center", fontsize=10)

	#message ASCII distribution
	p1 = plt.subplot(2, 2, 1)
	for i in range(len(m)):
		p1.scatter(i, ord(m[i]), s=5, c='b')
	p1.set_title("Message", fontsize=12, fontweight="bold")
	p1.set_ylabel("ASCII", fontsize=10)
	p1.tick_params(axis="both", labelsize=8)
	p1.set_ylim((0, 255))

	#MD5 distribution
	p2 = plt.subplot(2, 2, 2)
	for i in range(len(md5)):
		p2.scatter(i, int(md5[i], 16), s=5, c='b')
	p2.set_title("MD5", fontsize=12, fontweight="bold")
	p2.set_ylabel("Hex", fontsize=10)
	p2.set_xticks(np.arange(0, 33, 10))
	p2.set_yticks(np.arange(0, 18, 2))	
	p2.tick_params(axis="both", labelsize=8)
	p2.set_ylim(-1, 18)

	#SHA-1 distribution
	p3 = plt.subplot(2, 2, 3)
	for i in range(len(sha1)):
		p3.scatter(i, int(sha1[i], 16), s=5, c='b')
	p3.set_title("SHA-1", fontsize=12, fontweight="bold")
	p3.set_ylabel("Hex", fontsize=10)
	p3.set_xticks(np.arange(0, 41, 10))
	p3.set_yticks(np.arange(0, 18, 2))	
	p3.tick_params(axis="both", labelsize=8)
	p3.set_ylim(-1, 18)
	
	#SHA-256 distribution
	p4 = plt.subplot(2, 2, 4)
	for i in range(len(sha256)):
		p4.scatter(i, int(sha256[i], 16), s=5, c='b')
	p4.set_title("SHA-256", fontsize=12, fontweight="bold")
	p4.set_ylabel("Hex", fontsize=10)
	p4.set_xticks(np.arange(0, 65, 10))
	p4.set_yticks(np.arange(0, 18, 2))	
	p4.tick_params(axis="both", labelsize=8)
	p4.set_ylim(-1, 18)


	fig = plt.figure(2)
	fig.suptitle("Distribution Test", ha="center", fontsize=19, fontweight="bold")
	fig.text(0.5, 0.04, "Position", ha="center", fontsize=10)

	#32 size hex distribution
	p2 = plt.subplot(2, 2, 1)
	for i in range(len(size_32)):
		p2.scatter(i, int(size_32[i], 16), s=5, c='b')
	p2.set_title("n = 32 (128 bits)", fontsize=12, fontweight="bold")
	p2.set_ylabel("Hex", fontsize=10)
	p2.set_xticks(np.arange(0, 33, 10))
	p2.set_yticks(np.arange(0, 18, 2))
	p2.tick_params(axis="both", labelsize=8)
	p2.set_ylim(-1, 18)
	
	#64 size hex distribution
	p2 = plt.subplot(2, 2, 2)
	for i in range(len(size_64)):
		p2.scatter(i, int(size_64[i], 16), s=5, c='b')
	p2.set_title("n = 64 (256 bits)", fontsize=12, fontweight="bold")
	p2.set_ylabel("Hex", fontsize=10)
	p2.set_xticks(np.arange(0, 65, 10))
	p2.set_yticks(np.arange(0, 18, 2))
	p2.tick_params(axis="both", labelsize=8)
	p2.set_ylim(-1, 18)

	#128 size hex distribution
	p3 = plt.subplot(2, 2, 3)
	for i in range(len(size_128)):
		p3.scatter(i, int(size_128[i], 16), s=5, c='b')
	p3.set_title("n = 128 (512 bits)", fontsize=12, fontweight="bold")
	p3.set_xticks(np.arange(0, 129, 10))
	p3.set_yticks(np.arange(0, 18, 2))
	p3.tick_params(axis="both", labelsize=8)
	p3.set_ylim(-1, 18)

	#256 size hex distribution
	p4 = plt.subplot(2, 2, 4)
	for i in range(len(size_256)):
		p4.scatter(i, int(size_256[i], 16), s=5, c='b')
	p4.set_title("n = 256 (1024 bits)", fontsize=12, fontweight="bold")
	p4.set_xticks(np.arange(0, 257, 20))
	p4.set_yticks(np.arange(0, 18, 2))
	p4.tick_params(axis="both", labelsize=8)
	p4.set_ylim(-1, 18)
	
	plt.show()

main()