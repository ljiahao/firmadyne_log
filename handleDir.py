import subprocess
import os


def main():
	dir_set = [368, 100, 97, 61, 221, 504, 405, 358, 501, 39, 299, 450, 565, 547, 91, 188, 484, 367, 4, 165, 254, 108, 302, 402, 60, 446]
	#subprocess.call('mkdir res101', shell = True
	for d in dir_set:
		path = './' + str(d)
		file1 = path + "/qemu.initial.serial.log"
		file2 = path + "/qemu.final.serial.log"
		os.rename(file1, str(d) + '_initial.log')
		subprocess.call('cp ' + str(d) + '_initial.log' + ' ./firmadyne_log/8th/', shell = True)
		os.rename(file2, str(d) + "_final.log")
		subprocess.call('cp ' + str(d) + '_final.log' + ' ./firmadyne_log/8th/', shell = True)


if __name__ == '__main__':
	main()

