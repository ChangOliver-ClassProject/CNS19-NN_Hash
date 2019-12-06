
#Author: Oliver Chang

import matplotlib.pyplot as plt
import numpy as np
import hashlib

m = "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
#8_size = "40b26dc2"
#16_size = "fd1159a6e15bc3d1"
size_32 = "6d417dc870157e41432239d61d346160"
size_64 = "e0b3870b673929871baeab24a6c7cdde91801ed8c7513846655d1449960612ef"
size_128 = "393e618f57eca0da8198e394205b2231990ccff5e14f9c009fbbe6963406a3efd90664078f877e59561e5a9938979f7468fa4a6d595b71a16239969ee62bd1e3"
size_256 = "347f45bbb38a6c298002b4ab26566fef1667c600e1ab9843e5a040dfe895c0238a71c7a18b9bc714c555a14e45bd78aec62b4202daeb924ad8a35e87149e95b557886f483b4697aac6d75ddb91a8596aca5adc384d443ae476d3a5477bfc61487e911e6e6ade7fad404c46a884e0bacb164fd7e84c7eaf6faba882d8c819c35e"
#size_512 = "559133d5bfd7dbb96754b4934f806b6626ad40703193a0eb869ec513e67c9543ae0c5eaa87ed544edd84e2a67a4bd52b2dfb7183794a33d1a7ba4f06869c7065c9c67fa3333e123b87df884ebe236f4f2917924aa1d76331a7ec237983408f3fc1b7ddbd895971cb1765cbaf85a93dc88b2f4690e6d5b955da90ccf41cc7af7f21f1628ddf30acedd7ca26febdeb95127737d3d995021838869be5a070bf116d815a77b2f4a3cfe87c65d66a1c3a6cb56ca4c185a9b7d94970239443ae197b6fbef63a61c8702ec5954f300c1211d40063e9ce5b1606d367b189465c6bafd3bfc1a84fcd7a8adbda97b5a799103c1e03e5ee374fd893dcdd8e73620a770272a3"
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