import subprocess
import os


def main():
	dir_set = [294, 488, 388, 556, 219, 430, 478, 128, 550, 432, 178, 296, 522, 561, 221, 85, 283, 425, 579, 109, 316, 509, 501, 341, 507, 389, 543, 576, 164, 448, 174, 460, 586, 412, 293, 239, 115, 391, 486, 437, 375, 540, 167, 475, 469, 559, 298, 38, 264]
	#subprocess.call('mkdir res101', shell = True
	for d in dir_set:
		path = './' + str(d)
		file1 = path + "/qemu.initial.serial.log"
		file2 = path + "/qemu.final.serial.log"
		os.rename(file1, str(d) + '_initial.log')
		subprocess.call('cp ' + str(d) + '_initial.log' + ' ./firmadyne_log/3th/', shell = True)
		os.rename(file2, str(d) + "_final.log")
		subprocess.call('cp ' + str(d) + '_final.log' + ' ./firmadyne_log/3th/', shell = True)


if __name__ == '__main__':
	main()

