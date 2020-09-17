import subprocess
import os


def main():
	dir_set = [294, 324, 575, 259, 197, 556, 97, 447, 219, 325, 49, 288, 128, 539, 432, 296, 577, 186, 463, 79, 374, 508, 210, 111, 442, 94, 70, 56, 279, 205, 105, 482, 211, 20, 54, 389, 473, 413, 494, 286, 268, 209, 7, 386, 297, 394, 328, 472, 145, 93, 267, 2, 12, 421, 420, 350, 136, 400, 175, 77, 137, 99, 584, 590, 562, 101, 329, 567, 593, 108, 29, 321, 536, 542, 14, 141, 50, 468, 300, 41, 496, 373, 532, 456, 255, 78, 17, 339, 38, 443, 382, 206, 566, 404, 392, 370, 277]
	#subprocess.call('mkdir res101', shell = True
	for d in dir_set:
		path = './' + str(d)
		file1 = path + "/qemu.initial.serial.log"
		file2 = path + "/qemu.final.serial.log"
		os.rename(file1, str(d) + '_initial.log')
		subprocess.call('cp ' + str(d) + '_initial.log' + ' ./firmadyne_log/6th/', shell = True)
		os.rename(file2, str(d) + "_final.log")
		subprocess.call('cp ' + str(d) + '_final.log' + ' ./firmadyne_log/6th/', shell = True)


if __name__ == '__main__':
	main()

