import subprocess
import os


def main():
	dir_set = [100, 76, 131, 75, 97, 61, 49, 96, 173, 142, 191, 118, 124, 129, 40, 73, 130, 39, 57, 134, 43, 146, 66, 3, 116, 28, 92, 198, 46, 8, 115, 145, 93, 65, 31, 88, 12, 171, 68, 69, 143, 5, 127, 53, 133, 90, 148, 14, 50, 160, 41, 177, 83, 27, 6, 58, 104, 106, 132, 59, 78, 32, 34]
	#subprocess.call('mkdir res101', shell = True
	for d in dir_set:
		path = './' + str(d)
		file1 = path + "/qemu.initial.serial.log"
		file2 = path + "/qemu.final.serial.log"
		os.rename(file1, str(d) + '_initial.log')
		subprocess.call('cp ' + str(d) + '_initial.log' + ' ./firmadyne_log/5th/', shell = True)
		os.rename(file2, str(d) + "_final.log")
		subprocess.call('cp ' + str(d) + '_final.log' + ' ./firmadyne_log/5th/', shell = True)


if __name__ == '__main__':
	main()

